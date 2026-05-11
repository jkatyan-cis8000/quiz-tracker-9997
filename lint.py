# Quiz-tracker Linter

# This linter enforces the layered architecture rules for the quiz-tracker project.

import ast
import sys
from pathlib import Path


LAYER_ORDER = ["types", "config", "repo", "providers", "utils", "service", "runtime", "ui"]
VALID_LAYER_IMPORTS = {
    "types": ["types"],
    "config": ["types", "config"],
    "repo": ["types", "config", "repo"],
    "providers": ["types", "config", "utils", "providers"],
    "utils": ["utils"],
    "service": ["types", "config", "repo", "providers", "service"],
    "runtime": ["types", "config", "repo", "service", "providers", "runtime"],
    "ui": ["types", "config", "service", "runtime", "providers", "ui"],
}


def get_layer_from_path(file_path: Path) -> str | None:
    """Get the layer name from a file's path."""
    src_root = Path(__file__).parent / "src"
    try:
        rel_path = file_path.relative_to(src_root)
        parts = rel_path.parts
        if parts:
            return parts[0]
    except ValueError:
        pass
    return None


def check_import_rules(file_path: Path, tree: ast.AST) -> list[tuple[int, str]]:
    """Check import statements against layer rules."""
    violations = []
    layer = get_layer_from_path(file_path)
    if layer is None:
        return violations

    valid_imports = VALID_LAYER_IMPORTS.get(layer, [])

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                import_name = alias.name.split(".")[0]
                if import_name in LAYER_ORDER and import_name not in valid_imports:
                    violations.append(
                        (node.lineno, f"Import '{alias.name}' from '{import_name}' not allowed in '{layer}' layer")
                    )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                import_name = node.module.split(".")[0]
                if import_name in LAYER_ORDER and import_name not in valid_imports:
                    violations.append(
                        (node.lineno, f"Import from '{node.module}' not allowed in '{layer}' layer")
                    )

    return violations


def check_line_count(file_path: Path, content: str) -> list[tuple[int, str]]:
    """Check if file exceeds 300 lines."""
    lines = content.split("\n")
    if len(lines) > 300:
        return [(1, f"File exceeds 300 lines ({len(lines)} lines)")]
    return []


def check_all_files() -> list[tuple[str, int, str]]:
    """Check all source files for violations."""
    violations = []
    src_dir = Path(__file__).parent / "src"

    for file_path in src_dir.rglob("*.py"):
        if file_path.name.startswith("_") and file_path.parent == src_dir:
            continue  # Skip __init__.py at src root

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            tree = ast.parse(content, filename=str(file_path))

            # Check line count
            violations.extend((str(file_path), line, msg) for line, msg in check_line_count(file_path, content))

            # Check import rules
            violations.extend((str(file_path), line, msg) for line, msg in check_import_rules(file_path, tree))

        except SyntaxError as e:
            violations.append((str(file_path), e.lineno or 0, f"Syntax error: {e}"))

    return violations


def main():
    """Run linter and report results."""
    violations = check_all_files()

    if violations:
        print("Linting failed:")
        for file_path, line_num, message in violations:
            print(f"  {file_path}:{line_num}: {message}")
        sys.exit(1)

    print("Linting passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()

# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/types/__init__.py: Quiz, Question, Answer, Score types
- src/config/__init__.py: Config class for quiz settings
- src/repo/__init__.py: QuestionRepository interface and in-memory implementation
- src/service/__init__.py: QuizService for game logic
- src/providers/logger.py: Simple logging provider
- src/utils/__init__.py: parse_int, format_score utility functions
- src/runtime/__init__.py: AppContext and runtime setup
- src/ui/__init__.py: CLI interface for quiz presentation

## Interfaces

### Types (src/types/__init__.py)
- `class Question`: id: int, text: str, options: List[str] | None, correct_answer: str | int, category: str
- `class QuizState`: questions: List[Question], current_index: int, score: int, answers: List[str]
- `class QuizConfig`: show_correct_answers: bool, max_questions: int

### Config (src/config/__init__.py)
- `class Config`: load_from_env() -> Config, get_setting(key: str) -> Any

### Repo (src/repo/__init__.py)
- `interface QuestionRepository`: get_all() -> List[Question], get_by_category(category: str) -> List[Question]
- `class InMemoryRepository`: implements QuestionRepository with sample data

### Service (src/service/__init__.py)
- `class QuizService`: __init__(repo, config), start_quiz(), answer_question(index, answer), get_score(), finish_quiz() -> QuizResult
- `class QuizResult`: total_questions: int, correct_count: int, correct_answers_list: List[Question]

### Providers (src/providers/logger.py)
- `class Logger`: info(msg), debug(msg), error(msg)

### Utils (src/utils/__init__.py)
- `parse_int(value: str) -> int | None`: safe string to int conversion
- `format_score(score: int, total: int) -> str`: formatted display

### UI (src/ui/__init__.py)
- `class QuizUI`: present_question(question, index), get_user_answer(), display_results(result)

## Shared Data Structures

```python
# Question types
class Question(TypedDict):
    id: int
    text: str
    options: List[str] | None  # None for short-answer
    correct_answer: str | int  # int for multiple-choice index, str for short-answer
    category: str

class QuizState(TypedDict):
    questions: List[Question]
    current_index: int
    score: int
    answers: List[str]

class QuizResult(TypedDict):
    total_questions: int
    correct_count: int
    correct_answers_list: List[Question]
```

## External Dependencies

- No external dependencies required. This is a pure Python CLI application.

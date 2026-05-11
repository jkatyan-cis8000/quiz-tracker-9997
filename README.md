# Quiz Tracker

A trivia quiz application following a layered architecture pattern.

## Architecture

This project uses a layered architecture with strict import rules:

```
src/
├── types/        # Pure type definitions
├── config/       # Configuration and settings
├── repo/         # Data access layer
├── service/      # Business logic
├── providers/    # Cross-cutting concerns
├── utils/        # Pure helper functions
├── runtime/      # App lifecycle and orchestration
└── ui/           # User interface (CLI)
```

## Setup

No external dependencies required. Run with Python 3.8+.

## Running

```bash
python -m runtime
```

## Linting

```bash
python lint.py
```

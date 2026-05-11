import os
from typing import Any


class Config:
    def __init__(self) -> None:
        self._settings: dict[str, Any] = {}

    def load_from_env(self) -> "Config":
        self._settings["quiz_max_questions"] = int(os.getenv("QUIZ_MAX_QUESTIONS", "10"))
        self._settings["show_correct_answers"] = os.getenv("SHOW_CORRECT_ANSWERS", "true").lower() == "true"
        return self

    def get_setting(self, key: str) -> Any:
        return self._settings.get(key)

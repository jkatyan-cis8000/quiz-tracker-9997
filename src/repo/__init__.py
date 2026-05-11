from typing import List
from src.types import Question


class QuestionRepository:
    def get_all(self) -> List[Question]:
        raise NotImplementedError

    def get_by_category(self, category: str) -> List[Question]:
        raise NotImplementedError


class InMemoryRepository(QuestionRepository):
    def __init__(self) -> None:
        self._questions: List[Question] = [
            {
                "id": 1,
                "text": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct_answer": 2,
                "category": "geography",
            },
            {
                "id": 2,
                "text": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": 1,
                "category": "science",
            },
            {
                "id": 3,
                "text": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "correct_answer": 1,
                "category": "math",
            },
            {
                "id": 4,
                "text": "Who wrote 'Hamlet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
                "correct_answer": 1,
                "category": "literature",
            },
            {
                "id": 5,
                "text": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "O2", "NaCl"],
                "correct_answer": 0,
                "category": "science",
            },
        ]

    def get_all(self) -> List[Question]:
        return self._questions.copy()

    def get_by_category(self, category: str) -> List[Question]:
        return [q for q in self._questions if q["category"] == category]

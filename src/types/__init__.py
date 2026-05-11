from typing import TypedDict, List


class Question(TypedDict):
    id: int
    text: str
    options: List[str] | None
    correct_answer: str | int
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


class QuizConfig(TypedDict):
    show_correct_answers: bool
    max_questions: int

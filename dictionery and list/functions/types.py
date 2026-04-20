from typing import TypedDict

class UserRecord(TypedDict):
    id: int
    name: str
    surname: str
    date_of_birth: str
    grades_mathematics: list[int]
    grades_polish: list[int]
    grades_english: list[int]


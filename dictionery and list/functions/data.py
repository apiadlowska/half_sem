import json
import os
from typing import Any
from .types import UserRecord

FILE_PATH = "data.json"


def normalize_user_record(raw: dict[str, Any]) -> UserRecord:
    return {
        "id": raw.get("id", 0),
        "name": raw.get("name", ""),
        "surname": raw.get("surname", ""),
        "date_of_birth": raw.get("date_of_birth", raw.get("date of birth", "")),
        "grades_mathematics": raw.get("grades_mathematics", raw.get("grades mathematics", [])) or [],
        "grades_polish": raw.get("grades_polish", raw.get("grades polish", [])) or [],
        "grades_english": raw.get("grades_english", raw.get("grades english", [])) or []
    }


def read_data() -> list[UserRecord]:
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            raw_data = json.load(f)
            return [normalize_user_record(item) for item in raw_data]
        except json.JSONDecodeError:
            return []

def save_data(data: list[UserRecord]) -> None:
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def print_all_data(data: list[UserRecord]) -> None:
    print(f"\n{'='*50}\nPEŁNA LISTA UŻYTKOWNIKÓW\n{'='*50}")
    if not data:
        print("Baza danych jest pusta.")
    else:
        for user in data:
            print(f"ID: {user['id']} | {user['name'].title()} {user['surname'].title()}")
    print(f"{'='*50}")
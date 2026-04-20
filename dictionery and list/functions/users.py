import random
from typing import Any

def generate_unique_id(data: list[dict[str, Any]]) -> int:
    existing_ids = [u['id'] for u in data]
    while True:
        new_id = random.randint(100000, 999999)
        if new_id not in existing_ids:
            return new_id

def add_new_user(data: list[dict[str, Any]]) -> dict[str, Any]:
    print("\n--- REJESTRACJA NOWEGO BOHATERA ---")
    name = input("Podaj imię: ").strip().lower()
    surname = input("Podaj nazwisko: ").strip().lower()
    dob = input("Data urodzenia (DD.MM.YYYY): ").strip()
    
    return {
        "id": generate_unique_id(data),
        "name": name,
        "surname": surname,
        "date of birth": dob,
        "grades mathematics": [],
        "grades polish": [],
        "grades english": ()
    }
import random
from typing import Optional
from.types import UserRecord


def _get_avg(grades: list[int]) -> Optional[float]:
    """Pomocnicza: Oblicza średnią lub zwraca None jeśli brak ocen."""
    return sum(grades) / len(grades) if grades else None

# --- WYMAGANE FUNKCJE (0-16) ---

# 1. find_user_by_id
def find_user_by_id(data: list[UserRecord], user_id: int) -> Optional[UserRecord]:
    for u in data:
        if u.get("id") == user_id:
            return u
    return None

# 2. find_users_by_name
def find_users_by_name(data: list[UserRecord], name: str) -> list[UserRecord]:
    if not name or not name.strip():
        return []
    n = name.strip().lower()
    return [u for u in data if u.get("name", "").lower() == n]

# 3. delete_user_by_id
def delete_user_by_id(data: list[UserRecord], user_id: int) -> bool:
    u = find_user_by_id(data, user_id)
    if u:
        data.remove(u)
        return True
    return False

# 4. update_user_name
def update_user_name(data: list[UserRecord], user_id: int, new_name: str) -> bool:
    u = find_user_by_id(data, user_id)
    if u:
        u['name'] = new_name.lower()
        return True
    return False

# 5. update_user_surname
def update_user_surname(data: list[UserRecord], user_id: int, new_surname: str) -> bool:
    u = find_user_by_id(data, user_id)
    if u:
        u['surname'] = new_surname.lower()
        return True
    return False

# 6. update_user_birth_date
def update_user_birth_date(data: list[UserRecord], user_id: int, new_birth_date: str) -> bool:
    u = find_user_by_id(data, user_id)
    if u:
        u['date_of_birth'] = new_birth_date
        return True
    return False

# 7. is_name_taken
def is_name_taken(data: list[UserRecord], name: str, surname: str) -> bool:
    n, s = name.lower(), surname.lower()
    for u in data:
        if u.get('name') == n and u.get('surname') == s:
            return True
    return False

# 8. show_one_user
def show_one_user(user: UserRecord) -> None:
    if not user:
        print("[-] Niepoprawny użytkownik.")
        return
    print(f"\n--- PROFIL: {user.get('name', '').upper()} {user.get('surname', '').upper()} ---")
    print(f"ID: {user.get('id')} | Ur: {user.get('date_of_birth')}")
    print(f"MAT: {user.get('grades_mathematics')}")
    print(f"POL: {user.get('grades_polish')}")
    print(f"ENG: {user.get('grades_english')}")

# 9. count_all_users
def count_all_users(data: list[UserRecord]) -> int:
    return len(data)

# 10. count_users_with_missing_name
def count_users_with_missing_name(data: list[UserRecord]) -> int:
    count = 0
    for u in data:
        if not u['name'].strip():  # Just check for empty/whitespace
            count += 1
    return count

# 11. average_math_for_user
def average_math_for_user(user: UserRecord) -> Optional[float]:
    return _get_avg(user.get("grades_mathematics", []))

# 12. average_polish_for_user
def average_polish_for_user(user: UserRecord) -> Optional[float]:
    return _get_avg(user.get("grades_polish", []))

# 13. average_english_for_user
def average_english_for_user(user: UserRecord) -> Optional[float]:
    return _get_avg(user.get("grades_english", []))

# 14. overall_average_for_user
def overall_average_for_user(user: UserRecord) -> Optional[float]:
    all_g = (user.get("grades_mathematics", []) + 
             user.get("grades_polish", []) + 
             user.get("grades_english", []))
    return _get_avg(all_g)

# 15. best_student_in_subject
def best_student_in_subject(data: list[UserRecord], subject: str) -> Optional[UserRecord]:
    key = f"grades_{subject.lower().strip()}"
    best_u = None
    max_avg = -1.0
    for u in data:
        avg = _get_avg(u.get(key, []))
        if avg is not None and avg > max_avg:
            max_avg = avg
            best_u = u
    return best_u

# 16. subject_average_for_all_users
def subject_average_for_all_users(data: list[UserRecord], subject: str) -> Optional[float]:
    key = f"grades_{subject.lower().strip()}"
    all_grades: list[int] = []
    for u in data:
        all_grades.extend(u.get(key, []))
    return _get_avg(all_grades)

# 0. add_or_remove_grades
def add_or_remove_grades(data: list[UserRecord]) -> None:
    name = input("Podaj imię: ").lower()
    matches = find_users_by_name(data, name)
    if not matches:
        print("Nie znaleziono."); return
    for m in matches:
        print(f"ID: {m['id']} | {m['name'].title()} {m['surname'].title()}")
    try:
        uid = int(input("Wpisz ID: "))
        u = find_user_by_id(data, uid)
        if not u: return
        
        sub = input("Przedmiot (mathematics/polish/english): ").lower().strip()
        
        # Type-safe subject mapping
        grades_map = {
            "mathematics": u["grades_mathematics"],
            "polish": u["grades_polish"],
            "english": u["grades_english"]
        }
        
        if sub not in grades_map:
            print("Zły przedmiot."); return
        
        grades_list = grades_map[sub]
        act = input("Akcja (add/remove): ").lower()
        val = int(input("Ocena (2-6): "))
        
        if not 2 <= val <= 6:
            print("Ocena musi być między 2 a 6!"); return
        
        if act == "add":
            grades_list.append(val)
            print("[+] Dodano.")
        elif act == "remove":
            if val in grades_list:
                grades_list.remove(val)
                print("[+] Usunięto.")
            else:
                print("[-] Ocena nie istnieje.")
    except ValueError:
        print("Błąd danych.")

# --- TWOJE DODATKOWE FUNKCJE ---

def delete_random_user(data: list[UserRecord]) -> bool:
    """Wybiera losową osobę i ją usuwa."""
    if not data:
        return False
    target = random.choice(data)
    print(f"\n[!] USUNIĘTO: {target['name'].title()} {target['surname'].title()} (ID: {target['id']})")
    data.remove(target)
    return True

def add_random_historical_hero(data: list[UserRecord]) -> UserRecord:
    """Generuje losową postać historyczną."""
    pool = [
        {"name": "napoleon", "surname": "bonaparte", "dob": "15.08.1769"},
        {"name": "albert", "surname": "einstein", "dob": "14.03.1879"},
        {"name": "adolf", "surname": "hitler", "dob": "20.04.1889"}
    ]
    h = random.choice(pool)
    return {
        "id": random.randint(100000, 999999),
        "name": h["name"],
        "surname": h["surname"],
        "date_of_birth": h["dob"],
        "grades_mathematics": [random.randint(2,6) for _ in range(2)],
        "grades_polish": [random.randint(2,6) for _ in range(2)],
        "grades_english": [random.randint(2,6) for _ in range(2)]
    }
from typing import List, Dict, Optional, Any

# --- Search & Management ---
def find_user_by_id(data: List[Dict[str, Any]], user_id: int) -> Optional[Dict[str, Any]]:
    for user in data:
        if user.get("id") == user_id:
            return user
    return None

def delete_user_by_id(data: List[Dict[str, Any]], user_id: int) -> bool:
    user = find_user_by_id(data, user_id)
    if user:
        data.remove(user)
        return True
    return False

# --- Statistics ---
def average_math_for_user(user: Dict[str, Any]) -> Optional[float]:
    grades = user.get("grades_mathematics", [])
    return sum(grades) / len(grades) if grades else None

def overall_average_for_user(user: Dict[str, Any]) -> Optional[float]:
    all_grades: List[float] = user.get("grades_mathematics", []) + \
                 user.get("grades_polish", []) + \
                 user.get("grades_english", [])
    return sum(all_grades) / len(all_grades) if all_grades else None

def subject_average_for_all_users(data: List[Dict[str, Any]], subject: str) -> Optional[float]:
    key = f"grades_{subject.lower()}"
    all_grades: List[float] = []
    for user in data:
        all_grades.extend(user.get(key, []))
    return sum(all_grades) / len(all_grades) if all_grades else None
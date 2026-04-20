# from functions import data
# from functions import users
# import os
# import time 

# def program_menu()->None:
#         print(
#     """
#     ================================================
#     \n
#     e - exsit
#     w - add user
#     r - data inf
#     \n
#     ================================================
#     """)


# def main(): 
#     loaded_data:list[dict] = data.read_data()
#     while True:
#         program_menu()
#         inp = input("- ").lower().strip()
#         if inp == "e":
#             print("The program has finished running")
#             data.save_data(loaded_data)
#             break
#         elif inp == "w":
#             new_user = users.add_new_user(loaded_data)
#             loaded_data.append(new_user)
#             data.save_data(loaded_data)
#         elif inp == "r":
#             data.print_all_data(loaded_data)
#         elif inp == "t":
#             pass
#         elif inp == "y":
#             pass
#         elif inp == "u":
#             pass
#         elif inp == "i":
#             pass
#         elif inp == "o":
#             pass
#         else:
#             os.system("cls" if os.name == "nt" else "clear")
#             print("There is no such command")
#             time.sleep(2)


# if __name__ == '__main__':
#     main()
    
    
# # def change_user(data:list[dict]):
# #     i = 0 
# #     print("wybierz ")


# data 
# import json

# def save_data(data):
#     with open("data.json", "w", encoding="utf-8") as file:
#         json.dump(data, file, indent=4)

# def read_data():
#     with open("data.json", "r", encoding="utf-8") as file:
#         return json.load(file)

# def print_all_data(data:list[dict]):
#     for el in data:
#         print("==="*20)
#         for k,v in el.items():
#             print(f"{k} ----- {v}")


# statistic# from typing import List, Dict, Optional

# # --- CORE MATH UTILITY ---

# def _calculate_list_average(grades: List[int]) -> Optional[float]:
#     """Helper function to avoid code repetition."""
#     if not grades:
#         return None
#     return sum(grades) / len(grades)

# # --- INDIVIDUAL USER STATS (Functions 11-14) ---

# def average_math_for_user(user: Dict) -> Optional[float]:
#     return _calculate_list_average(user.get("grades mathematics", []))

# def average_polish_for_user(user: Dict) -> Optional[float]:
#     return _calculate_list_average(user.get("grades polish", []))

# def average_english_for_user(user: Dict) -> Optional[float]:
#     return _calculate_list_average(user.get("grades english", []))

# def overall_average_for_user(user: Dict) -> Optional[float]:
#     all_grades = (
#         user.get("grades mathematics", []) + 
#         user.get("grades polish", []) + 
#         user.get("grades english", [])
#     )
#     return _calculate_list_average(all_grades)

# # --- GLOBAL STATS (Functions 15-16) ---

# def best_student_in_subject(data: List[Dict], subject: str) -> Optional[Dict]:
#     """Finds the student with the highest average in a specific subject."""
#     subject_map = {
#         "mathematics": average_math_for_user,
#         "polish": average_polish_for_user,
#         "english": average_english_for_user
#     }
    
#     calc_func = subject_map.get(subject.lower())
#     if not data or not calc_func:
#         return None

#     best_student = None
#     highest_avg = -1.0

#     for user in data:
#         current_avg = calc_func(user)
#         if current_avg is not None and current_avg > highest_avg:
#             highest_avg = current_avg
#             best_student = user
            
#     return best_student

# def subject_average_for_all_users(data: List[Dict], subject: str) -> Optional[float]:
#     """Calculates the mean for one subject across the whole class."""
#     key_map = {
#         "mathematics": "grades mathematics",
#         "polish": "grades polish",
#         "english": "grades english"
#     }
    
#     key = key_map.get(subject.lower())
#     if not data or not key:
#         return None

#     all_grades = []
#     for user in data:
#         all_grades.extend(user.get(key, []))
        
#     return _calculate_list_average(all_grades)


# userss 
# from random import randint

# def generate_unique_id(data: list[dict]) -> int:
#     lst_id = []
#     for user in data:
#         lst_id.append(user.get("id"))
#     new_id = randint(1, 1000000)
#     while new_id in lst_id:
#         new_id = randint(1, 1000000)
#     return new_id

# def add_new_user(data: list[dict])-> dict:
#     return {
#         "id": generate_unique_id(data),
#         "name": input("Enter name: ").strip().lower() or None,
#         "surname":input("Enter surname: ").strip().lower() or None,
#         "date of birth":input("date of birth: ").strip().lower() or None,
#         "grades mathematics": [],
#         "grades polish": [], 
#         "grades english":[]        
#     }
    


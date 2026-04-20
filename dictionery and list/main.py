from functions import data, statistic
from functions.types import UserRecord
import os, time, random

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def program_menu():
    print(f"""
    {'='*50}
    [1] Statystyki Ogólne (0-16)  [w] Dodaj Użytkownika
    [r] Lista Wszystkich (Z ID)   [d] Usuń (po ID)
    [s] Statystyki Ucznia         [u] Edytuj Dane Osobowe
    [0] Edycja Ocen               [h] Dodaj Bohatera (Losowo)
    [x] Usuń Losowo               [q] Przywróć Dane (Reset)
    [e] Wyjdź i Zapisz
    {'='*50}
    """)

def main():
    loaded_data: list[UserRecord] = data.read_data()  
    while True:
        clear()
        program_menu()
        inp = input("Wybór: ").lower().strip()
        
        if inp == "e":
            data.save_data(loaded_data); break
        
        elif inp == "q":
            if input("Cofnąć zmiany? (t/n): ") == "t": 
                loaded_data = data.read_data()

        elif inp == "w":
            n = input("Imię: "); s = input("Nazwisko: ")
            if statistic.is_name_taken(loaded_data, n, s):
                print("Taka osoba już istnieje!"); time.sleep(1); continue
            user_data: UserRecord = {
                "id": random.randint(100000, 999999), 
                "name": n.lower(), 
                "surname": s.lower(),
                "date_of_birth": input("Data ur: "), 
                "grades_mathematics": [], 
                "grades_polish": [], 
                "grades_english": []
            }
            loaded_data.append(user_data); print(f"Dodano ID: {user_data['id']}"); input("\nEnter...")

        elif inp == "u":
            try:
                uid = int(input("Podaj ID do edycji: "))
                opt = input("Co zmienić? (1-Imię, 2-Nazwisko, 3-Data): ")
                new_val = input("Nowa wartość: ")
                success = False
                if opt == "1": success = statistic.update_user_name(loaded_data, uid, new_val)
                elif opt == "2": success = statistic.update_user_surname(loaded_data, uid, new_val)
                elif opt == "3": success = statistic.update_user_birth_date(loaded_data, uid, new_val)
                print("Sukces!" if success else "Błąd ID.")
            except: print("Błąd.")
            input("\nEnter...")

        elif inp == "s":
            n = input("Imię: ").lower(); matches = statistic.find_users_by_name(loaded_data, n)
            for m in matches: print(f"ID: {m['id']} | {m['name'].title()} {m['surname'].title()}")
            try:
                uid = int(input("ID: ")); found_user: UserRecord | None = statistic.find_user_by_id(loaded_data, uid)
                if found_user: 
                    statistic.show_one_user(found_user)
                    print(f"Średnia MAT: {statistic.average_math_for_user(found_user)}")
                    print(f"Średnia ALL: {statistic.overall_average_for_user(found_user)}")
            except: pass
            input("\nEnter...")

        elif inp == "1":
            print(f"\n{'='*50}\nSTATYSTYKI OGÓLNE (0-16)\n{'='*50}")
            print(f"Liczba użytkowników: {statistic.count_all_users(loaded_data)}")
            print(f"Bez imienia: {statistic.count_users_with_missing_name(loaded_data)}")
            for subj in ["mathematics", "polish", "english"]:
                avg = statistic.subject_average_for_all_users(loaded_data, subj)
                best = statistic.best_student_in_subject(loaded_data, subj)
                print(f"\n{subj.upper()}:")
                print(f"  Średnia: {avg:.2f}" if avg else "  Średnia: Brak danych")
                if best:
                    print(f"  Najlepszy: {best['name'].title()} {best['surname'].title()} ({best['id']})")
            print(f"{'='*50}")
            input("\nEnter...")

        elif inp == "d":
            try:
                uid = int(input("Podaj ID do usunięcia: "))
                if statistic.delete_user_by_id(loaded_data, uid):
                    print(f"[+] Usunięto użytkownika (ID: {uid})")
                else:
                    print("[-] Nie znaleziono użytkownika.")
            except ValueError:
                print("[-] Błędne ID.")
            input("\nEnter...")

        elif inp == "0": statistic.add_or_remove_grades(loaded_data); input("\nEnter...")
        elif inp == "r": data.print_all_data(loaded_data); input("\nEnter...")
        elif inp == "h": 
            hero: UserRecord = statistic.add_random_historical_hero(loaded_data)
            loaded_data.append(hero); print(f"Dodano: {hero['name'].title()}"); input("\nEnter...")
        elif inp == "x": statistic.delete_random_user(loaded_data); time.sleep(2)

if __name__ == '__main__': main()

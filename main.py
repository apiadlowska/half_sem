from funkcje import clear_screen
import time
from gra import gra


if __name__ == "__main__":
    clear_screen()
    print("Witaj w grze RPG!")
    print("Czy chcesz rozpocząć grę? (T/N)")
    while True:
        odpowiedz = input().strip().lower()
        clear_screen()
        if odpowiedz == 't':
            gra()
            break
        elif odpowiedz == 'n':
            print("Do zobaczenia następnym razem!")
            time.sleep(1)
            break
        else:
            print("Nieprawidłowa wybór. Wybierzen 'T' lub 'N'.")
        
    exit(0)
    
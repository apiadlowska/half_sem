
import time
from typing import Any
import funkcje
CZAR_POSTAWOWY = "Postawowy"
CZAR_BLYSKAWICA = "Błyskawica"
CZAR_KULA_OGNIA = "Kula ognia"
CZAR_ZAMROZENIE = "Zamrożenie"


CZARY_MANA = "mana"
CZARY_KOSZT = "złoto"
CZARY_ATAK = "atak"
CZARY_EFEKT = "efekt"
CZARY_ZYCIE = "HP"

BOHATER_CZARY = "czary"
BOHATER_ELIKSIRY = "eliksiry"
BOHATER_WOJOWNIK = "Wojownik"
BOHATER_RODZAJ = "rodzaj"
BOHATER_ZLOTO = "złoto"

ELIKSIR_ZYCIA = "Eliksir życia"
ELIKSIR_MANY = "Eliksir many"
ELIKSIR_FULL_ZYCIE = "Eliksir full życia"
ELIKSIR_FULL_MANA = "Eliksir full many"
ELIKSIR_KOSZT = "zloto"
ELIKSIR_ZYCIE = "zycie"
ELIKSIR_MANA = "mana"


parametry_czaru:dict[str,Any] = {
    CZAR_POSTAWOWY: {CZARY_MANA: 10, CZARY_ATAK: 20, CZARY_KOSZT: 100, CZARY_EFEKT: "brak"},
    CZAR_BLYSKAWICA: {CZARY_MANA: 20, CZARY_ATAK: 40, CZARY_EFEKT: "zamrozenie (50% szans)", CZARY_KOSZT: 200},
    CZAR_KULA_OGNIA: {CZARY_MANA: 25, CZARY_ATAK: 60, CZARY_EFEKT: "125% obrazen", CZARY_KOSZT: 250},
    CZAR_ZAMROZENIE: {CZARY_MANA: 15, CZARY_ATAK: 10, CZARY_EFEKT: "2 rundy unieruchomienia", CZARY_KOSZT: 180}
}

parametry_eliksiru:dict[str,Any] = {
    ELIKSIR_ZYCIA: {ELIKSIR_KOSZT: 30, ELIKSIR_ZYCIE: 25, ELIKSIR_MANA: 0},
    ELIKSIR_MANY: {ELIKSIR_KOSZT: 40, ELIKSIR_ZYCIE: 0, ELIKSIR_MANA: 50},
    ELIKSIR_FULL_ZYCIE: {ELIKSIR_KOSZT: 50, ELIKSIR_ZYCIE: 100, ELIKSIR_MANA: 0},
    ELIKSIR_FULL_MANA: {ELIKSIR_KOSZT: 70, ELIKSIR_ZYCIE: 0, ELIKSIR_MANA: 100}
}
def wypisz_czary(czary:list[str]) -> str:
    return ", ".join(czary)        
    
def nauka_czarow(bohater:dict[str,Any]) -> dict[str,Any]:
    while True:
        funkcje.clear_screen()
        print(f"Masz: {bohater[BOHATER_ZLOTO]} złota i umiesz czary: {wypisz_czary(bohater[BOHATER_CZARY])}")
        print("Naucz się nowego czaru. (Bohater typu wojownik cena x 2)")
        print(f"1. {CZAR_POSTAWOWY}: {parametry_czaru[CZAR_POSTAWOWY][CZARY_KOSZT]} złota.")
        print(f"2. {CZAR_BLYSKAWICA}: {parametry_czaru[CZAR_BLYSKAWICA][CZARY_KOSZT]} złota.")
        print(f"3. {CZAR_KULA_OGNIA}: {parametry_czaru[CZAR_KULA_OGNIA][CZARY_KOSZT]} złota.")
        print(f"4. {CZAR_ZAMROZENIE}: {parametry_czaru[CZAR_ZAMROZENIE][CZARY_KOSZT]} złota.")
        print("5. Wyjście.")
        wybor = input("Który czar chcesz się nauczyć?: ")
        if wybor == "1" and CZAR_POSTAWOWY not in bohater[BOHATER_CZARY]:
            nauka_czaru(bohater, CZAR_POSTAWOWY)
        elif wybor == "2" and CZAR_BLYSKAWICA not in bohater[BOHATER_CZARY]:
            nauka_czaru(bohater, CZAR_BLYSKAWICA)
        elif wybor == "3"  and CZAR_KULA_OGNIA not in bohater[BOHATER_CZARY]:
            nauka_czaru(bohater, CZAR_KULA_OGNIA)
        elif wybor == "4" and CZAR_ZAMROZENIE not in bohater[BOHATER_CZARY]:
            nauka_czaru(bohater, CZAR_ZAMROZENIE)
        elif wybor == "5":
            print("Wychodzisz z nauki czarów.")
            break
        time.sleep(1)
    return bohater    


def nauka_czaru(bohater:dict[str,Any], czar:str):
    mnoznik = 1
    if bohater[BOHATER_RODZAJ] == BOHATER_WOJOWNIK: mnoznik = 2
    if bohater[BOHATER_ZLOTO] >= parametry_czaru[czar][CZARY_KOSZT] * mnoznik:
        bohater[BOHATER_CZARY].append(czar)
        bohater[BOHATER_ZLOTO] -= parametry_czaru[czar][CZARY_KOSZT] * mnoznik
        print("Nauczyłeś się czaru: " + czar + "!")
    else:
        print("Nie masz wystarczająco złota na naukę tego czaru.")
    time.sleep(2)

def zakup_eliksiru(bohater:dict[str,Any], eliksir:str):
    mnoznik = 1
    if bohater[BOHATER_RODZAJ] == BOHATER_WOJOWNIK: mnoznik = 2
    if bohater[BOHATER_ZLOTO] >= parametry_eliksiru[eliksir][ELIKSIR_KOSZT] * mnoznik:
        if eliksir in bohater[BOHATER_ELIKSIRY]:
            bohater[BOHATER_ELIKSIRY][eliksir] += 1
        else:
            bohater[BOHATER_ELIKSIRY][eliksir] = 1
        bohater[BOHATER_ZLOTO] -= parametry_eliksiru[eliksir][ELIKSIR_KOSZT] * mnoznik
        print("Kupiłeś eliksir: " + eliksir + "!")
    else:
        print("Nie masz wystarczająco złota na zakup tego eliksiru.")    
        

        
def wypisz_eliksiry(eliksiry:dict[str,int]) -> str:
    return ", ".join(f"{eliksir}: {ilosc}" for eliksir, ilosc in eliksiry.items())
        
def kup_eliksiry(bohater:dict[str,Any]) -> dict[str,Any]:
    while True:
        funkcje.clear_screen()
        print(f"Masz: {bohater[BOHATER_ZLOTO]} złota i masz eliksiry: [{wypisz_eliksiry(bohater[BOHATER_ELIKSIRY])}]")
        print("Bohater typu wojownik cena x 2")
        print(f"1. {ELIKSIR_ZYCIA}: {parametry_eliksiru[ELIKSIR_ZYCIA][ELIKSIR_KOSZT]} złota.")
        print(f"2. {ELIKSIR_MANY }: {parametry_eliksiru[ELIKSIR_MANY][ELIKSIR_KOSZT]} złota.")
        print(f"3. {ELIKSIR_FULL_ZYCIE}: {parametry_eliksiru[ELIKSIR_FULL_ZYCIE][ELIKSIR_KOSZT]} złota.")
        print(f"4. {ELIKSIR_FULL_MANA}: {parametry_eliksiru[ELIKSIR_FULL_MANA][ELIKSIR_KOSZT]} złota.")
        print("5. Wyjście.")
        wybor = input("Który eliksir chcesz się kupic?: ")
        if wybor == "1":
            zakup_eliksiru(bohater, ELIKSIR_ZYCIA)
        elif wybor == "2":
            zakup_eliksiru(bohater, ELIKSIR_MANY)
        elif wybor == "3":
            zakup_eliksiru(bohater, ELIKSIR_FULL_ZYCIE)
        elif wybor == "4":
            zakup_eliksiru(bohater, ELIKSIR_FULL_MANA)
        elif wybor == "5":
            print("Szkoda, że nas opuszczasz.")
            time.sleep(1)
            break
    return bohater  
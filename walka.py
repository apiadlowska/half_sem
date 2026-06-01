from typing import Any
import random
import time
import funkcje
from miejsca import NABRZEZE_WALKA_ZE_ZLOCZYNCAMI, RYNEK_SZUKAJ_ZLODZIEJA, MIASTO, BRON_LUK, BRON_MIECZ, BRON_ZBROJA, parametry_broni, BRONIE_ATAK
from postacie import ATAK, ZYCIE, ZLOTO, CZARY, MANA, ELIKSIRY, BRON, ZBROJA,ZYCIE_AKTUALNE,MANA_AKTUALNA, wypisz_statystyki, wypisz_czary, wypisz_eliksiry
import czary

REZULTAT = "rezultat"
PORAZKA = "porażka"
WYGRANA = "wygrana"
UCIECZKA = "ucieczka"
BOHATER = "bohater"
WALKA= "walka"
ZAMROZENIE= "zamrożenie"
ZAMROZENIE_x2= "zamrożenie x2"
POWROT = "powrot"

def generuj_wroga(miejsce_walki:str) -> dict[str, int]:
    wrog = { ATAK: 0, ZYCIE: 0, ZLOTO: 0}
    if miejsce_walki == MIASTO:
        wrog[ATAK] = random.randint(25,40)
        wrog[ZYCIE] = random.randint(80,120)
        wrog[ZLOTO] = random.randint(70,90)
    elif miejsce_walki == NABRZEZE_WALKA_ZE_ZLOCZYNCAMI:
        wrog[ATAK] = random.randint(35,60)
        wrog[ZYCIE] = random.randint(60,100)
        wrog[ZLOTO] = random.randint(40,60)
    elif miejsce_walki == RYNEK_SZUKAJ_ZLODZIEJA:
        wrog[ATAK] = random.randint(10,25)
        wrog[ZYCIE] = random.randint(100,150)
        wrog[ZLOTO] = random.randint(60,110)
    return wrog

def wypisz_wroga(wrog: dict[str,int]) -> str:
    return f"Atak({wrog[ATAK]}), HP({wrog[ZYCIE]})"

def ma_czary(bohater:dict[str,Any]) -> bool:
    return len(bohater[CZARY]) > 0

def ma_eliksiry(bohater:dict[str,Any]) -> bool:
    return len(bohater[ELIKSIRY]) > 0


def atak_bronia(bohater:dict[str,Any], wrog:dict[str,int]):
    sila_ataku = bohater[ATAK]
    if bohater[BRON] == BRON_LUK:
        sila_ataku += parametry_broni[BRON_LUK][BRONIE_ATAK]
    elif bohater[BRON] == BRON_MIECZ:
        sila_ataku += parametry_broni[BRON_MIECZ][BRONIE_ATAK]
    wrog[ZYCIE] -= sila_ataku
    print(f"Atakujesz wroga z siłą: {sila_ataku}!")
    time.sleep(1)
    if wrog[ZYCIE] < 0:
        return WYGRANA
    return WALKA

def atak_wroga(bohater:dict[str,Any], wrog:dict[str,int]):
    sila_wroga = wrog[ATAK]
    if bohater[ZBROJA] == BRON_ZBROJA:
        sila_wroga += parametry_broni[BRON_ZBROJA][BRONIE_ATAK]
    if sila_wroga > 0:
        bohater[ZYCIE_AKTUALNE] -= sila_wroga
    print(f"Wróg atakuje cię z siłą: {sila_wroga}!")
    time.sleep(1)
    if bohater[ZYCIE_AKTUALNE] < 0:
        return PORAZKA
    return WALKA

def wypisanie_czarow(czary_bohatera:list[str]):
    if czary.CZAR_POSTAWOWY in czary_bohatera:
        print(f"1. {czary.CZAR_POSTAWOWY} (atak: {czary.parametry_czaru[czary.CZAR_POSTAWOWY][czary.CZARY_ATAK]}, efekt: {czary.parametry_czaru[czary.CZAR_POSTAWOWY][czary.CZARY_EFEKT]}).")
    if czary.CZAR_BLYSKAWICA in czary_bohatera:
        print(f"2. {czary.CZAR_BLYSKAWICA}(atak: {czary.parametry_czaru[czary.CZAR_BLYSKAWICA][czary.CZARY_ATAK]}, efekt: {czary.parametry_czaru[czary.CZAR_BLYSKAWICA][czary.CZARY_EFEKT]}).")
    if czary.CZAR_KULA_OGNIA in czary_bohatera:
        print(f"3. {czary.CZAR_KULA_OGNIA}(atak: {czary.parametry_czaru[czary.CZAR_KULA_OGNIA][czary.CZARY_ATAK]}, efekt: {czary.parametry_czaru[czary.CZAR_KULA_OGNIA][czary.CZARY_EFEKT]}).")
    if czary.CZAR_ZAMROZENIE in czary_bohatera:
        print(f"4. {czary.CZAR_ZAMROZENIE}(atak: {czary.parametry_czaru[czary.CZAR_ZAMROZENIE][czary.CZARY_ATAK]}, efekt: {czary.parametry_czaru[czary.CZAR_ZAMROZENIE][czary.CZARY_EFEKT]}).")
    print(f"5. Powrót.")

def atak_czarem(bohater:dict[str,Any], wrog:dict[str,int]) -> str:
    print(f"Czary bohatera: [{wypisz_czary(bohater[CZARY])}], mana: [{bohater[MANA_AKTUALNA]}]")
    wypisanie_czarow(bohater[CZARY])
    sila_ataku = bohater[ATAK]
    rezultat = WALKA
    while True:
        czar = input("Wybierz czar: ?")
        wybrany_czar = ""
        if czar == "1" and czary.CZAR_POSTAWOWY in bohater[CZARY] and bohater[MANA_AKTUALNA] >= czary.parametry_czaru[czary.CZAR_POSTAWOWY][czary.CZARY_MANA]:        
            sila_ataku += czary.parametry_czaru[czary.CZAR_POSTAWOWY][czary.CZARY_ATAK]
            bohater[MANA_AKTUALNA] -= czary.parametry_czaru[czary.CZAR_POSTAWOWY][czary.CZARY_MANA]
            wybrany_czar = czary.CZAR_POSTAWOWY
            break
        elif czar == "2" and czary.CZAR_BLYSKAWICA in bohater[CZARY] and bohater[MANA] >= czary.parametry_czaru[czary.CZAR_BLYSKAWICA][czary.CZARY_MANA]:        
            sila_ataku += czary.parametry_czaru[czary.CZAR_BLYSKAWICA][czary.CZARY_ATAK]
            bohater[MANA_AKTUALNA] -= czary.parametry_czaru[czary.CZAR_BLYSKAWICA][czary.CZARY_MANA]
            if random.randint(0,100) <= 50:
                rezultat = ZAMROZENIE
            wybrany_czar = czary.CZAR_BLYSKAWICA
            break
        elif czar == "3" and czary.CZAR_KULA_OGNIA in bohater[CZARY] and bohater[MANA_AKTUALNA] >= czary.parametry_czaru[czary.CZAR_KULA_OGNIA][czary.CZARY_MANA]:        
            sila_ataku += czary.parametry_czaru[czary.CZAR_KULA_OGNIA][czary.CZARY_ATAK]
            sila_ataku = int(1.25 * sila_ataku)
            bohater[MANA_AKTUALNA] -= czary.parametry_czaru[czary.CZAR_KULA_OGNIA][czary.CZARY_MANA]
            wybrany_czar = czary.CZAR_KULA_OGNIA
            break
        elif czar == "4" and czary.CZAR_ZAMROZENIE in bohater[CZARY] and bohater[MANA_AKTUALNA] >= czary.parametry_czaru[czary.CZAR_ZAMROZENIE][czary.CZARY_MANA]:        
            sila_ataku += czary.parametry_czaru[czary.CZAR_ZAMROZENIE][czary.CZARY_ATAK]
            bohater[MANA_AKTUALNA] -= czary.parametry_czaru[czary.CZAR_ZAMROZENIE][czary.CZARY_MANA]
            rezultat = ZAMROZENIE_x2
            wybrany_czar = czary.CZAR_ZAMROZENIE
            break
        elif czar == "5":
            return POWROT      
    if(rezultat != WALKA): 
        efekt = rezultat 
    else: 
        efekt = "brak"
    print(f"Atakujesz wroga z czarem: {wybrany_czar}, siła ataku: {sila_ataku}, efekt dodatkowy: {efekt}")
    time.sleep(1)
    wrog[ZYCIE] -= sila_ataku
    if wrog[ZYCIE] < 0:
        rezultat = WYGRANA
    return rezultat

def wypisanie_eliksirow(eliksiry_bohatera:dict[str,int]):
    if czary.ELIKSIR_ZYCIA in eliksiry_bohatera and eliksiry_bohatera[czary.ELIKSIR_ZYCIA] > 0:
        print(f"1. {czary.ELIKSIR_ZYCIA}(HP: {czary.parametry_eliksiru[czary.ELIKSIR_ZYCIA][czary.ELIKSIR_ZYCIE]}, mana: {czary.parametry_eliksiru[czary.ELIKSIR_ZYCIA][czary.ELIKSIR_MANA]}).")
    if czary.ELIKSIR_MANY in eliksiry_bohatera and eliksiry_bohatera[czary.ELIKSIR_MANY] > 0:
        print(f"2. {czary.ELIKSIR_MANY}(HP: {czary.parametry_eliksiru[czary.ELIKSIR_MANY][czary.ELIKSIR_ZYCIE]}, mana: {czary.parametry_eliksiru[czary.ELIKSIR_MANY][czary.ELIKSIR_MANA]}).")
    if czary.ELIKSIR_FULL_ZYCIE in eliksiry_bohatera and eliksiry_bohatera[czary.ELIKSIR_FULL_ZYCIE] > 0: 
        print(f"3. {czary.ELIKSIR_FULL_ZYCIE}(HP: {czary.parametry_eliksiru[czary.ELIKSIR_FULL_ZYCIE][czary.ELIKSIR_ZYCIE]}, mana: {czary.parametry_eliksiru[czary.ELIKSIR_FULL_ZYCIE][czary.ELIKSIR_MANA]}).")
    if czary.ELIKSIR_FULL_MANA in eliksiry_bohatera and eliksiry_bohatera[czary.ELIKSIR_FULL_MANA] > 0:
        print(f"4. {czary.ELIKSIR_FULL_MANA}(HP: {czary.parametry_eliksiru[czary.ELIKSIR_FULL_MANA][czary.ELIKSIR_ZYCIE]}, mana: {czary.parametry_eliksiru[czary.ELIKSIR_FULL_MANA][czary.ELIKSIR_MANA]}).")
    print(f"5. Powrót.")


def uzycie_eliksiru(bohater:dict[str,Any] ):
    print(f"Eliksiry bohatera: [{wypisz_eliksiry(bohater[ELIKSIRY])}]")
    wypisanie_eliksirow(bohater[ELIKSIRY])
    eliksir_wybrany = ""
    while True:
        eliksir = input("Wybierz eliksir: ?")
        if eliksir == "1" and bohater[ELIKSIRY][czary.ELIKSIR_ZYCIA] > 0:
            eliksir_wybrany = czary.ELIKSIR_ZYCIA
            break
        elif eliksir == "2" and bohater[ELIKSIRY][czary.ELIKSIR_MANY] > 0:
            eliksir_wybrany = czary.ELIKSIR_MANY    
            break
        elif eliksir == "3" and bohater[ELIKSIRY][czary.ELIKSIR_FULL_ZYCIE] > 0:
            eliksir_wybrany = czary.ELIKSIR_FULL_ZYCIE    
            break
        elif eliksir == "4" and bohater[ELIKSIRY][czary.ELIKSIR_FULL_MANA] > 0:
            eliksir_wybrany = czary.ELIKSIR_FULL_MANA    
            break
        elif eliksir == "5":
            return
        else:
            continue
    print(f"Użyłeś eliksiru: {eliksir_wybrany}")
    time.sleep(1)
    bohater[ELIKSIRY][eliksir_wybrany] -= 1
    bohater[ZYCIE_AKTUALNE] += czary.parametry_eliksiru[eliksir_wybrany][czary.ELIKSIR_ZYCIE]
    if bohater[ZYCIE_AKTUALNE] > bohater[ZYCIE]:
        bohater[ZYCIE_AKTUALNE] = bohater[ZYCIE]
    bohater[MANA_AKTUALNA] += czary.parametry_eliksiru[eliksir_wybrany][czary.ELIKSIR_MANA]
    if bohater[MANA_AKTUALNA] > bohater[MANA]:
        bohater[MANA_AKTUALNA] = bohater[MANA]
    print(f"Bohater [ {wypisz_statystyki(bohater)} ]")

def walka(bohater:dict[str,Any], miejsce_walki: str) -> dict[str, Any]:
    
    nowy_bohater = bohater.copy()
    wrog = generuj_wroga(miejsce_walki)
    tura = 1
    print("Zaczynamy walkę!")
    time.sleep(1)
    zamrozenie = 0
    while True:
        
        funkcje.clear_screen()
        print(f"Bohater [ {wypisz_statystyki(nowy_bohater)} ]")
        print(f"Wróg [ {wypisz_wroga(wrog)} ]")
        print(f"Tura [{tura}] atak bohatera!")
        print(f"1. Atak bronią")
        if ma_czary(nowy_bohater):
            print(f"2. Atak czarem")
        if ma_eliksiry(nowy_bohater):
            print(f"3. Użycie eliksiru")
        print(f"4. Ucieczka (strata połowy złota)")
        rezultat = WALKA    
        akcja = input("Co robisz?")
        if akcja == "1":
            rezultat = atak_bronia(nowy_bohater, wrog)
            tura += 1
        elif akcja == "2" and ma_czary(nowy_bohater):
            rezultat = atak_czarem(nowy_bohater, wrog)
            if rezultat == POWROT:
                continue
            elif rezultat == ZAMROZENIE:
                zamrozenie += 1
            elif rezultat == ZAMROZENIE_x2:
                zamrozenie += 2
            tura += 1
        elif akcja == "3" and ma_eliksiry(nowy_bohater):
            uzycie_eliksiru(nowy_bohater)
            continue
        elif akcja == "4":
            zloto = int(nowy_bohater[ZLOTO]/2)
            print(f"Niestety podczas ucieczki straciłeś: {zloto} złota!")
            nowy_bohater[ZLOTO] -= zloto
            return {
                REZULTAT: UCIECZKA,
                BOHATER: nowy_bohater
            }    
        if rezultat == WYGRANA:
            print(f"Znalazłeś u pokonanego wroga: {wrog[ZLOTO]} złota!")
            nowy_bohater[ZLOTO] += wrog[ZLOTO]
            break
        if zamrozenie > 0:
            zamrozenie -= 1
            continue
        print(f"Atak wroga!")
        rezultat = atak_wroga(nowy_bohater, wrog)
        if rezultat == PORAZKA:
            return {
                REZULTAT: PORAZKA,
                BOHATER: nowy_bohater
            }
        time.sleep(1)
           
    return {
        REZULTAT: WYGRANA,
        BOHATER: nowy_bohater
    }
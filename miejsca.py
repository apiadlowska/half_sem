from typing import Any
import time
import random
import funkcje
import postacie

# Miejsca w grze
WIERZA_CZAROWNIKA = "Wieża Czarownika"
TAWERNA = "Tawerna"
BARAKI = "Baraki"
NABRZEZE = "Nabrzeże"
RYNEK = "Rynek"
MIASTO = "Miasto"

WYJSCIE_Z_GRY = "Wyjście z gry"

# Wierza Czarownika - opcje
WIERZA_NAUKA_CZAROW = "Nauka Czarów"
WIERZE_KUP_ELIKSIRY = "Kup eliksiry"
# WIERZA_ZACZAROWANIE_BRONI = "Zaczarowanie broni"

#Tawerna - opcje
TAWERNA_ZJEDZ = "Zjedz posiłek (życie +40, mana: +10, koszt: 20 złota)"
TAWERNA_WYPOCZNIJ = "Wypocznij (życie FULL, mana: FULL, koszt: 50 złota)"
TAWERNA_POPITEK = "Zabawa przy popitku (życie +5, mana: +40, koszt: 15 złota)"

#Barak - opcje
BARAKI_TRENING_WYTRZYMALOSCI = "Trening wytrzymałości (życie +10, mana +10, koszt: 40 złota)"
BARAKI_TRENING_ATAK = "Trening ataku (atak +10, mana +5, koszt: 50 złota)"
BARAKI_ZAKUP_BRONI = "Zakup broni"

BRON_MIECZ = "Miecz (Atak +30, koszt: 100 złota)"
BRON_LUK = "Łuk (Atak +25, koszt: 90 złota)"
BRON_ZBROJA = "Zbroja (Atak -20, koszt: 80 złota)"
BRONIE_KOSZT = "koszt"
BRONIE_ATAK = "atak"
parametry_broni = {
    BRON_MIECZ: {BRONIE_KOSZT: 100, BRONIE_ATAK: 30},
    BRON_LUK: {BRONIE_KOSZT: 90, BRONIE_ATAK: 25},
    BRON_ZBROJA: {BRONIE_KOSZT: 80, BRONIE_ATAK: -20},
}

#Rynek - opcje
RYNEK_SZUKAJ_ZLODZIEJA = "Wypatruj złodzieja"
#RYNEK_KUP_BRON = "Kup nielegalną broń"

#Nabrzeze - opcje
NABRZEZE_WALKA_ZE_ZLOCZYNCAMI = "Walka ze złoczyńcami"

def wybor_pozycji(menu: dict[str,str]) -> str:
    while True:
        for klucz, wartosc in menu.items():
            print(f"{klucz}. {wartosc}")       
        nowa_pozycja = input("Gdzie idziesz przyjacielu?:").strip()
        funkcje.clear_screen()
        if nowa_pozycja in menu.keys():
            return menu[nowa_pozycja]
        continue
        
    
    

def ruch_gracza(aktualna_pozycja:str,bohater:dict[str,Any]) -> str:
    funkcje.clear_screen()
    print(f"Bohater:[ {postacie.wypisz_statystyki(bohater)} ]")
    print("Wybierze miejsce, do którego chcesz się udać.")
    time.sleep(1)
    if aktualna_pozycja == MIASTO:
        return wybor_pozycji({
            "1": WIERZA_CZAROWNIKA,
            "2": TAWERNA,
            "3": BARAKI,
            "4": NABRZEZE,
            "5": RYNEK,
            "6": WYJSCIE_Z_GRY
        })
    elif aktualna_pozycja == WIERZA_CZAROWNIKA:
        return wybor_pozycji({
            "1": WIERZA_NAUKA_CZAROW,
            "2": WIERZE_KUP_ELIKSIRY,
            # "3": WIERZA_ZACZAROWANIE_BRONI,
            "3": MIASTO           
        })
    elif aktualna_pozycja in TAWERNA:
        return wybor_pozycji({
            "1": TAWERNA_ZJEDZ,
            "2": TAWERNA_WYPOCZNIJ,
            "3": TAWERNA_POPITEK,
            "4": MIASTO
        })
    elif aktualna_pozycja == BARAKI:
        return wybor_pozycji({
            "1": BARAKI_TRENING_WYTRZYMALOSCI,
            "2": BARAKI_TRENING_ATAK,
            "3": BARAKI_ZAKUP_BRONI,
            "4": MIASTO
        })
    elif aktualna_pozycja in RYNEK:
        return wybor_pozycji({
            "1": RYNEK_SZUKAJ_ZLODZIEJA,
            "2": MIASTO
        })
    elif aktualna_pozycja == NABRZEZE:
        return wybor_pozycji({
            "1": NABRZEZE_WALKA_ZE_ZLOCZYNCAMI,
            "2": MIASTO
        })
    return MIASTO
        
        
        
def czy_walka(pozycja:str) -> bool:
    if pozycja == NABRZEZE_WALKA_ZE_ZLOCZYNCAMI:
        return True
    elif pozycja == RYNEK_SZUKAJ_ZLODZIEJA:
        return random.randint(0,100) <= 30  # 30% szans na walkę
    elif pozycja == MIASTO:
        return random.randint(0,100) <= 5   # 5% szans na walkę
    return False




def baraki_trening_atak(bohater:dict[str,Any]):
    if bohater[postacie.ZLOTO] < 50:
        print("Nie masz wystarczająco złota na trening.")
        time.sleep(1)
        return
    print("Trenujesz atak.")
    time.sleep(1)
    bohater[postacie.ATAK] += 10
    bohater[postacie.MANA] += 5
    bohater[postacie.MANA_AKTUALNA] += 5
    bohater[postacie.ZLOTO] -= 50
    time.sleep(1)
    
def baraki_trening_wytrzymalosc(bohater:dict[str,Any]):
    if bohater[postacie.ZLOTO] < 40:
        print("Nie masz wystarczająco złota na trening.")
        time.sleep(1)
        return
    print("Trenujesz wytrzymałość.")
    time.sleep(1)
    bohater[postacie.ZYCIE] += 10
    bohater[postacie.ZYCIE_AKTUALNE] += 10
    bohater[postacie.MANA] += 10
    bohater[postacie.MANA_AKTUALNA] += 10
    bohater[postacie.ZLOTO] -= 40
    time.sleep(1)
    

def baraki_zakup_broni(bohater:dict[str,Any]):
    while True:
        funkcje.clear_screen()
        print(f"Masz: {bohater[postacie.ZLOTO]} złota i posiadasz: [broń: {bohater[postacie.BRON]}, zbroja: {bohater[postacie.ZBROJA]}]")
        print(f"1. {BRON_MIECZ}: {parametry_broni[BRON_MIECZ][BRONIE_KOSZT]} złota.")
        print(f"2. {BRON_LUK}: {parametry_broni[BRON_LUK][BRONIE_KOSZT]} złota.")
        print(f"3. {BRON_ZBROJA}: {parametry_broni[BRON_ZBROJA][BRONIE_KOSZT]} złota.")
        
        print("4. Powrót do baraków.")
        wybor = input("Którą broń chcesz się kupic?: ")
        if wybor == "1" and BRON_MIECZ != bohater[postacie.BRON]:
            zakup_broni(bohater, postacie.BRON, BRON_MIECZ)
        elif wybor == "2" and BRON_LUK != bohater[postacie.BRON]:
            zakup_broni(bohater, postacie.BRON, BRON_LUK)
        elif wybor == "3" and BRON_ZBROJA != bohater[postacie.ZBROJA]:
            zakup_broni(bohater,postacie.ZBROJA, BRON_ZBROJA)
        elif wybor == "4":
            print("Szkoda, że nas opuszczasz.")
            time.sleep(1)
            break
    return bohater  

def zakup_broni(bohater:dict[str,Any],bohater_parametr:str , bron: str):
    if bohater[postacie.ZLOTO] >= parametry_broni[bron][BRONIE_KOSZT]:
        bohater[bohater_parametr] = bron
        bohater[postacie.ZLOTO] -= parametry_broni[bron][BRONIE_KOSZT]
        print("Kupiłeś: " + bron + "!")
    else:
        print(f"Nie masz wystarczająco złota na zakup: {bron}.")
    time.sleep(2)
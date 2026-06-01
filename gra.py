from typing import Any
import time
import miejsca
import postacie
import walka
import czary
import funkcje


bohater:dict[str,Any] = {}
pozycja_gracza:str = ""

def wybierz_bohatera():
    print("Bohater:")
    print("1. Wojownik")
    print("2. Mag")
    print("Q - wyjście z gry")
    while True:
        rodzaj_bohatera = input("Twój wybór: ").strip()
        if rodzaj_bohatera == '1':
            return postacie.BOHATER_WOJOWNIK
        elif rodzaj_bohatera == '2':
            return postacie.BOHATER_MAG
        elif rodzaj_bohatera.lower() == 'q':
            print("Wyjście z gry.")
            time.sleep(1)
            exit(0)

def gra():
    global bohater
    print("Rozpoczynamy przygodę!")
    rodzaj_bohatera = wybierz_bohatera()
    bohater = postacie.stworz_bohatera(rodzaj_bohatera)
    print("Stworzyłeś bohatera: " + rodzaj_bohatera + " " + postacie.wypisz_statystyki(bohater))
    input("Kontynuuj???...")
    funkcje.clear_screen()
    gra_poruszanie(miejsca.MIASTO)
    
def miasto() -> bool:
    global bohater, pozycja_gracza
    print("Witaj w mieście. Oby spokój panował na ulicach.")
    time.sleep(1)
    if miejsca.czy_walka(miejsca.MIASTO):
        print("Szykuje się walka!")
        time.sleep(1)
        rezultat = walka.walka(bohater,miejsca.MIASTO)
        if rezultat[walka.REZULTAT] == walka.PORAZKA:
            print("Niestety przegrałeś walkę. Koniec gry.")
            time.sleep(2)
            funkcje.clear_screen()
            return False
        elif rezultat[walka.REZULTAT] == walka.WYGRANA:
            print("Wygrałeś walkę, zyskałeś złoto i chwałę.")
            time.sleep(2)
        else:
            print("Lepiej uratować skórę, niż parę srebrników.")
            time.sleep(2)
        bohater = rezultat[walka.BOHATER]
        funkcje.clear_screen()
    else: 
        print("Spokojny dzień w mieście.")
        time.sleep(1)
    return True


def nabrzeze() -> bool:
    global bohater
    print("Witaj na nabrzeżu.")
    if miejsca.czy_walka(miejsca.NABRZEZE_WALKA_ZE_ZLOCZYNCAMI):
        print("Szykuje się walka!")
        time.sleep(1)
        rezultat = walka.walka(bohater,miejsca.NABRZEZE_WALKA_ZE_ZLOCZYNCAMI)
        if rezultat[walka.REZULTAT] == walka.PORAZKA:
            print("Niestety przegrałeś walkę. Koniec gry.")
            time.sleep(2)
            funkcje.clear_screen()
            return False
        elif rezultat[walka.REZULTAT] == walka.WYGRANA:
            print("Wygrałeś walkę, zyskałeś złoto i chwałę.")
            time.sleep(2)
        else:
            print("Lepiej uratować skórę, niż parę srebrników.")
            time.sleep(2)
        bohater = rezultat[walka.BOHATER]
        funkcje.clear_screen()
    return True
    
def rynek() -> bool:
    global bohater
    print("Witaj na rynku, ciekawe czy znajdziesz złodziei.")
    if miejsca.czy_walka(miejsca.RYNEK_SZUKAJ_ZLODZIEJA):
        print("Szykuje się walka!")
        time.sleep(1)
        rezultat = walka.walka(bohater,miejsca.RYNEK_SZUKAJ_ZLODZIEJA)
        if rezultat[walka.REZULTAT] == walka.PORAZKA:
            print("Niestety przegrałeś walkę. Koniec gry.")
            time.sleep(2)
            funkcje.clear_screen()
            return False
        elif rezultat[walka.REZULTAT] == walka.WYGRANA:
            print("Wygrałeś walkę, zyskałeś złoto i chwałę.")
            time.sleep(2)
        else:
            print("Lepiej uratować skórę, niż parę srebrników.")
            time.sleep(2)
        bohater = rezultat[walka.BOHATER]
        funkcje.clear_screen()
    else: 
        print("Spokojny dzień na rynku, brak złodziei.")
        time.sleep(1)
    return True
 
def tawerna_odpoczynek():
    if bohater[postacie.ZLOTO] < 50:
        print("Nie masz wystarczająco złota na odpoczynek.")
        time.sleep(1)
        return
    print("Odpoczywasz w tawernie.")
    time.sleep(1)
    bohater[postacie.ZYCIE_AKTUALNE] = bohater[postacie.ZYCIE]
    bohater[postacie.MANA_AKTUALNA] = bohater[postacie.MANA]
    bohater[postacie.ZLOTO] -= 50


def tawerna_jedzenie():
    if bohater[postacie.ZLOTO] < 20:
        print("Nie masz wystarczająco złota na jedzenie.")
        time.sleep(1)
        return
    print("Najadłeś się i odzyskałeś trochę sił.")
    time.sleep(1)
    bohater[postacie.ZYCIE_AKTUALNE] += 40
    if bohater[postacie.ZYCIE_AKTUALNE] > bohater[postacie.ZYCIE]:
        bohater[postacie.ZYCIE_AKTUALNE] = bohater[postacie.ZYCIE]
    bohater[postacie.ZLOTO] -= 20           

def tawerna_popitek():
    if bohater[postacie.ZLOTO] < 15:
        print("Nie masz wystarczająco złota na jedzenie.")
        time.sleep(1)
        return
    print("Pobawiłeś się i odzyskałeś siłę umysłu.")
    time.sleep(1)
    bohater[postacie.ZYCIE_AKTUALNE] += 5
    if bohater[postacie.ZYCIE_AKTUALNE] > bohater[postacie.ZYCIE]:
        bohater[postacie.ZYCIE_AKTUALNE] = bohater[postacie.ZYCIE]
    bohater[postacie.MANA_AKTUALNA] += 40
    if bohater[postacie.MANA_AKTUALNA] > bohater[postacie.MANA]:
        bohater[postacie.MANA_AKTUALNA] = bohater[postacie.MANA]    
    bohater[postacie.ZLOTO] -= 15        

   

def gra_poruszanie(pozycja_gracza:str):
    global bohater
    while True:
        pozycja_gracza = miejsca.ruch_gracza(pozycja_gracza,bohater)
        if pozycja_gracza == miejsca.WYJSCIE_Z_GRY:
            return
        if pozycja_gracza == miejsca.MIASTO:
            if not miasto():
                return
        elif pozycja_gracza == miejsca.TAWERNA:
            print("Witaj w tawernie.")
            time.sleep(1)
            continue
        elif pozycja_gracza == miejsca.BARAKI:
            print("Witaj w barakach.")
            time.sleep(1)
            continue
        elif pozycja_gracza == miejsca.NABRZEZE or pozycja_gracza == miejsca.NABRZEZE_WALKA_ZE_ZLOCZYNCAMI:
            pozycja_gracza = miejsca.NABRZEZE
            if not nabrzeze():
                return
        elif pozycja_gracza == miejsca.RYNEK or pozycja_gracza == miejsca.RYNEK_SZUKAJ_ZLODZIEJA:
            pozycja_gracza = miejsca.RYNEK
            if not rynek():
                return
        elif pozycja_gracza == miejsca.WIERZA_CZAROWNIKA:
            print("Witaj w wieży czarownika.")
            time.sleep(1)
            continue
        elif pozycja_gracza == miejsca.TAWERNA_WYPOCZNIJ:
            tawerna_odpoczynek()
            pozycja_gracza = miejsca.TAWERNA
        elif pozycja_gracza == miejsca.TAWERNA_ZJEDZ:
            tawerna_jedzenie()
            pozycja_gracza = miejsca.TAWERNA
        elif pozycja_gracza == miejsca.TAWERNA_POPITEK:
            tawerna_popitek()
            pozycja_gracza = miejsca.TAWERNA
        elif pozycja_gracza == miejsca.WIERZA_NAUKA_CZAROW:
            czary.nauka_czarow(bohater)
            pozycja_gracza = miejsca.WIERZA_CZAROWNIKA
        elif pozycja_gracza == miejsca.WIERZE_KUP_ELIKSIRY:
            czary.kup_eliksiry(bohater)
            pozycja_gracza = miejsca.WIERZA_CZAROWNIKA
        elif pozycja_gracza == miejsca.BARAKI_TRENING_ATAK:
            miejsca.baraki_trening_atak(bohater)
            pozycja_gracza = miejsca.BARAKI
        elif pozycja_gracza == miejsca.BARAKI_TRENING_WYTRZYMALOSCI:
            miejsca.baraki_trening_wytrzymalosc(bohater)
            pozycja_gracza = miejsca.BARAKI
        elif pozycja_gracza == miejsca.BARAKI_ZAKUP_BRONI:
            miejsca.baraki_zakup_broni(bohater)
            pozycja_gracza = miejsca.BARAKI
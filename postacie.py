from typing import Any
from czary import CZAR_POSTAWOWY, wypisz_eliksiry, wypisz_czary
BOHATER_WOJOWNIK = "Wojownik"
BOHATER_MAG = "Mag"

RODZAJ = "rodzaj"
ATAK = "atak"
ZYCIE = "HP"
ZYCIE_AKTUALNE = "hp_aktualne"
MANA = "mana"
MANA_AKTUALNA = "mana_aktualna"
ZLOTO = "złoto"
CZARY = "czary"
ELIKSIRY = "eliksiry"
BRON = "broń"
ZBROJA = "zbroja"


def stworz_bohatera(rodzaj:str) -> dict[str,Any]:
    if rodzaj == BOHATER_WOJOWNIK:
        return {
            RODZAJ: BOHATER_WOJOWNIK,
            ATAK:50,
            ZYCIE: 150,
            ZYCIE_AKTUALNE: 150,
            MANA: 20,
            MANA_AKTUALNA: 20,
            ZLOTO: 2500,
            CZARY: [],
            BRON: "brak",
            ZBROJA: "brak",
            ELIKSIRY:{}
        }
    elif rodzaj == BOHATER_MAG:
        return {
            RODZAJ: BOHATER_MAG,
            ATAK: 25,
            ZYCIE: 100,
            ZYCIE_AKTUALNE: 100,
            MANA: 150,
            MANA_AKTUALNA: 150,
            ZLOTO: 2500,
            CZARY: [CZAR_POSTAWOWY],
            BRON: "brak",
            ZBROJA: "brak",
            ELIKSIRY:{}
        }
    else: 
        return {}


    
def wypisz_statystyki(bohater:dict[str,Any]) -> str:
    return "Atak(" + str(bohater[ATAK]) + ")" \
        + ", HP("+ str(bohater[ZYCIE_AKTUALNE]) + "/" + str(bohater[ZYCIE]) + ")" \
        + ", Mana(" + str(bohater[MANA_AKTUALNA]) + "/" + str(bohater[MANA]) + ")" \
        +  ", Złoto(" + str(bohater[ZLOTO]) + ")" \
        +  ", Broń(" + bohater[BRON] + ")" \
        +  ", Zbroja(" + bohater[ZBROJA] + ")" \
        +  ", Czary(" + wypisz_czary(bohater[CZARY]) + ")" \
        +  ", Eliksiry(" + wypisz_eliksiry(bohater[ELIKSIRY]) + ")"   
        
        
        

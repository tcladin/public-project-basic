import os
from uzivatelske_rozhrani import UzivatelskeRozhrani
from pojistenec import Pojistenec
from pojistenci import PojistenciManager
from hledani import Hledani

# inicializace
uzivatelske_rozhrani=UzivatelskeRozhrani() 
pojistenci_manager = PojistenciManager() # založí seznam pojištěnců

def clear_screen():
    # Pro Windows
    if os.name == 'nt':
        os.system('cls')
    # Pro Unix/Linux/MacOS
    else:
        os.system('clear')

# hlavní smyčka, která opakuje nabídku z menu dokud uživatel nezvolí ukončení programu
zadej = True
while zadej == True:
    clear_screen()
    uzivatelske_rozhrani.vypis_menu()
    vstup = input()   
    print()
    if vstup == "1":  # Přidat pojištěnce
        jmeno = uzivatelske_rozhrani.zadej_vstup("Zadejte jméno pojištěného:\n","nazev",2,12)   # jmeno="Petr"
        prijmeni = uzivatelske_rozhrani.zadej_vstup("Zadejte příjmení:\n","nazev",2,50)       # prijmeni="Pavel"
        tel = uzivatelske_rozhrani.zadej_vstup("Zadejte telefonní číslo: \n", "telefonni_cislo") # tel="732148411"
        vek = uzivatelske_rozhrani.zadej_vstup("Zadej věk: \n", "cele_cislo", 0, 150)            # vek="46"
        pojistenec = Pojistenec(jmeno, prijmeni, tel, vek)         # instance nového pojištěnce
        pojistenci_manager.vloz_pojistence(pojistenec) # vloží pojištěnce do seznamu pojištěnců
        print()
        uzivatelske_rozhrani.vypis_ulozeno()  
    elif vstup == "2":  # Vypsat pojištěné. Pokud existují záznamy, vypíše je.
        if pojistenci_manager.je_prazdny_seznam():        
            uzivatelske_rozhrani.vypis_prazdny_seznam()        
        else:
            seznam_vsech_pojistencu=pojistenci_manager.vydej_seznam()  # získá seznam všech pojištěnců         
            uzivatelske_rozhrani.vypis_pojistence(seznam_vsech_pojistencu) # vypíše seznam všech pojištěnců           
    elif vstup == "3":  # Hledat pojištěné. Pokud existují záznamy vyžádá si vstup a prohledá zda je taková osoba v seznamu všech pojištěnců, pokud ano vypíše ji.
        if pojistenci_manager.je_prazdny_seznam(): 
            uzivatelske_rozhrani.vypis_prazdny_seznam()
        else:
            jmeno = uzivatelske_rozhrani.zadej_vstup("Zadejte jméno pojištěného:\n","nazev",2,12)   # jmeno="Petr"
            prijmeni = uzivatelske_rozhrani.zadej_vstup("Zadejte příjmení:\n","nazev",2,50)         # prijmeni="Pavel"        
            seznam_vsech_pojistencu=pojistenci_manager.vydej_seznam() # získá seznam všech pojištěnců       
            nalezeni_pojistenci = Hledani(seznam_vsech_pojistencu,jmeno,prijmeni).hledat() # vyhledá pojištěnce v seznamu všech pojištěnců
            print()            
            uzivatelske_rozhrani.vypis_hledani(seznam_vsech_pojistencu,nalezeni_pojistenci) # vypíše nalezené pojištěnce v seznamu všech pojištěnců
    elif vstup == "4":  # Konec programu.      
        uzivatelske_rozhrani.vypis_konec()
        zadej = False
    else:
        uzivatelske_rozhrani.vypis_neplatna_volba()  # vypíše hlášku o neplatné volbě
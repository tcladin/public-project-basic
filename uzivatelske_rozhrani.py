class UzivatelskeRozhrani:
    """
    Vstupy a výstupy uživatele
    """    

    def __init__(self):
        self._pojistenci=[]

    def zadej_vstup(self,text_zadani,typ,min_hodnota=None,max_hodnota=None):
        """vybere metodu pro získání vstupu od uživatele podle typu
        Args:
            text_zadani: str - popisný text při zadání vstupu uživatelem
            typ: str - typ hodnoty
            min_hodnota: int - minimální hodnota
            max_hodnota: int - maximální hodnota
        Returns:
            object - metoda pro získání vstupu od uživatele podle typu
        """
        if typ=="nazev":
            # Předání výchozích hodnot pro min_hodnota a max_hodnota, pokud nejsou poskytnuty
            min_hodnota = min_hodnota if min_hodnota is not None else 2
            max_hodnota = max_hodnota if max_hodnota is not None else 15
            return self._zadej_nazev(text_zadani, min_hodnota, max_hodnota)
        elif typ=="telefonni_cislo":
            return self._zadej_telefonni_cislo(text_zadani)
        elif typ=="cele_cislo":
            return self._zadej_cele_cislo(text_zadani,min_hodnota,max_hodnota)

    def _zadej_nazev(self,text_zadani="Zadej název: \n", min_znaku=2, max_znaku=15):
        """vstupní pole pro název
        Args:
            text_zadani: str - popisný text při zadání vstupu uživatelem
            min_znaku: int - minimální počet znaků
            max_znaku: int - maximální počet znaků
        Returns:
            str - název
        """
        chybne_zadane = True
        while chybne_zadane:
            try:
                # odstraní všechny mezery https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
                vstup = "".join(input(text_zadani).split())
                if min_znaku <= len(vstup.strip()) <= max_znaku:  # délka je v rozmení min_znaku - max_znaku
                    # začíná velkým písmenem
                    if vstup.strip()[0] == vstup.strip()[0].upper():
                        #v názvu nejsou jiné znaky než písmena
                        je_cislo_v_nazev = False
                        for znak in vstup.strip():
                            if not znak.isalpha():
                                je_cislo_v_nazev = True
                                print("Je povoleno zadat pouze písmena.")
                                break
                        if not je_cislo_v_nazev:
                            return vstup
                    else:
                        print("Je požadováno první velké písmeno.")
                else:
                    print(f"Je požadována délka v rozmení od {min_znaku} do {max_znaku} znaků.")
            except Exception as e:  # obecná vyjímka
                print("Došlo k výjimce: ", str(e))    
    
    def _zadej_telefonni_cislo(self, text_zadani):
        """Vstupní pole pro telefonní číslo
        Args:
            text_zadani: str - popisný text při zadání vstupu uživatelem
        Returns:
            str - telefonní číslo
        """
        while True:
            cislo = input(text_zadani).strip()
            # Odstranění mezer a pomlček
            cislo = cislo.replace(" ", "").replace("-", "")
            # Kontrola platnosti čísla
            if cislo.startswith("+"):
                if len(cislo[1:]) == 12 and cislo[1:].isdigit():
                    return cislo
                else:
                    print("Telefonní číslo s mezinárodní předvolbou musí mít 12 číslic.")
            elif cislo.startswith("00"):
                if len(cislo[2:]) == 12 and cislo[2:].isdigit():
                    return cislo
                else:
                    print("Telefonní číslo s mezinárodní předvolbou musí mít 12 číslic.")                    
            elif len(cislo) == 9 and cislo.isdigit():
                return cislo
            else:
                print("Telefonní číslo musí mít 9 číslic nebo mezinárodní předvolbu a následně 9 číslic.")
    
    def _zadej_cele_cislo(self,text_zadani="Zadejte číslo: \n", min_cislic=0, max_cislic=10):
        """Vstupní pole pro celé číslo
        Args:
            text_zadani: str - popisný text při zadání vstupu uživatelem
            min_cislic: int - minimální hodnota
            max_cislic: int - maximální hodnota
        Returns:
            int - celé číslo"""    
        chybne_zadane = True
        while chybne_zadane:
            try:
                # odstraní všechny mezery https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
                vstup = int("".join(input(text_zadani).split()))
                if min_cislic <= vstup <= max_cislic:
                    return vstup
                else:
                    print(f"Je požadováno číslo v rozmení od {min_cislic} do {max_cislic}.")
                    chybne_zadane = True    
            except ValueError:
                print("Je požadováno celé číslo!")
            except Exception as e:  # obecná vyjímka
                print("Došlo k výjimce: ", str(e))


    @staticmethod
    def vypis_menu():
        """ vypíše menu pro uživatele"""
        print("Kartotéka pojišťenců")
        print("=============================")
        print("Vyberte si akci:")
        print("1 - přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    @staticmethod   
    def vypis_prazdny_seznam():
        """vypíše hlášku, že kartotéka je prázdná"""
        print("Kartotéka pojištěnců je prázdná")
        print()
        input("Pokračujte stiskem ENTER...")     

    @staticmethod  
    def vypis_ulozeno():
        """vypíše hlášku, že data byla uložena"""
        input("Data byla uložena. Pokračujte stiskem ENTER...")

    @staticmethod  
    def vypis_konec():
        """vypíše hlášku že končí program"""
        print("Díky za použití aplikace.")
        input("\nPokračujte stiskem ENTER...                         ladislav@schnaiberg.cz 2024(c)\n")      

    @staticmethod
    def vypis_neplatna_volba():
        """vypíše hlášku, že volba je neplatná"""
        print("Neplatná volba.") 
        input("Pokračujte stiskem ENTER...") 


    def vypis_pojistence(self, kartoteka=[]):
        """vypíše všechny pojištěnce ze seznamu
        Args:
            kartoteka: list - seznam pojištěnců
        Returns:
            str - vypíše seznam pojištěnců ve formátu jméno příjmení věk telefon
        """     
        self._kartoteka=kartoteka        
        # Zjistěte maximální délku příjmení
        max_prijmeni_len = max(len(pojistenec.prijmeni) for pojistenec in self._kartoteka)
        prijmeni_width = max(16, max_prijmeni_len + 2)  # Nastavte minimální šířku na 16 nebo více podle potřeby
        #záhlaví seznamu    
        print(f"{'Jméno'.ljust(16,' ')} {'Příjmení'.ljust(prijmeni_width,' ')} {'Věk'.ljust(8,' ')} {'Telefon'.ljust(13,' ')}")
        #tělo seznamu
        for pojistenec in self._kartoteka:
            print(pojistenec.__str__(prijmeni_width))
        print()
        input("Pokračujte stiskem ENTER...")                   

    def vypis_hledani(self, kartoteka=[], nalezeni_pojistenci=[]):     
        """vypíše pojištěnce pro které bylo provedeno hledání 
        Args:
            kartoteka: list - seznam všech pojištěnců
            nalezeni_pojistenci: list - seznam nalezených pojištěnců
        Returns:
        str - vypíše seznam nalezených pojištěnců ve formátu jméno příjmení věk telefon"""   
        self._kartoteka=kartoteka    
        self._nalezeni_pojistenci=nalezeni_pojistenci           
        nalezeno = 0
        # Zjistěte maximální délku příjmení
        max_prijmeni_len = max(len(pojistenec.prijmeni) for pojistenec in self._kartoteka)
        prijmeni_width = max(16, max_prijmeni_len + 2)  # Nastavte minimální šířku na 16 nebo více podle potřeby
        #záhlaví seznamu
        print(f"{'Jméno'.ljust(16,' ')} {'Příjmení'.ljust(prijmeni_width,' ')} {'Věk'.ljust(8,' ')} {'Telefon'.ljust(13,' ')}")
        #tělo seznamu
        for pojistenec in self._nalezeni_pojistenci:
            print(pojistenec.__str__(prijmeni_width))
            nalezeno += 1
        if nalezeno == 0:
            print(
                "\033[1A" + "\033[K"
            )  # vymaze zahlavi https://stackoverflow.com/questions/59736217/python-deleting-input-line
            print("Pojištěnec nenalezen.")
        print()
        input("Pokračujte stiskem ENTER...")       


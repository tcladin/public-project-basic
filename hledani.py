class Hledani:
    """reprezentuje vyhledaní pojištěnců"""

    def __init__(self,pojistenci,jmeno,prijmeni):
        """inicializace hledání
        Args:
            pojistenci: list pojištěnců
            jmeno: jméno pojištěnce
            prijmeni: příjmení pojištěnce
        """        
        self._pojistenci = pojistenci
        self._jmeno=jmeno
        self._prijmeni=prijmeni
        self._nalezeni_pojistenci=[]

    def hledat(self):
        """hledá podle zadaného jména a příjmení, vrátí nalezené pojištěnce v kartotéce
        return: nalezeni_pojistenci"""
        for pojistenec in self._pojistenci:
            if pojistenec.jmeno == self._jmeno and pojistenec.prijmeni == self._prijmeni:
                self._nalezeni_pojistenci.append(pojistenec)
        return self._nalezeni_pojistenci


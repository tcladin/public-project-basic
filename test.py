import unittest
from unittest.mock import patch
from pojistenec import Pojistenec
from pojistenci import PojistenciManager
from uzivatelske_rozhrani import UzivatelskeRozhrani

class NewlineTextTestResult(unittest.TextTestResult):
    """Třída pro výsledky testů, která vypisuje tečky s novým řádkem po každé tečce."""
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write('\n')  # Přidá nový řádek po každé tečce
        self.stream.flush()

class NewlineTextTestRunner(unittest.TextTestRunner):
    """Třída pro spuštění testů, která používá NewlineTextTestResult. 
    Umožňuje vypisovat tečky s novým řádkem po každé tečce."""	
    def _makeResult(self):
        return NewlineTextTestResult(self.stream, self.descriptions, self.verbosity)

class TestPojisteni(unittest.TestCase):

    def setUp(self):
        """Tato metoda se spustí před každým testem. 
        Slouží k inicializaci objektů"""
        self.uzivatelske_rozhrani = UzivatelskeRozhrani()
        self.pojistenec = Pojistenec("Jan", "Novak", "123456789", 30)
        self.pojistenci = PojistenciManager()

    def test_pojistenec(self):
        """Testuje vytvoření pojištěnce. 
        Testuje, zda je instance Pojistenec správně vytvořena."""
        self.assertEqual(self.pojistenec.jmeno, "Jan")
        self.assertEqual(self.pojistenec.prijmeni, "Novak")
        self.assertEqual(self.pojistenec.tel, "123456789")
        self.assertEqual(self.pojistenec.vek, 30)

    @patch('builtins.input', lambda _: "+420123456789")
    def test_zadej_telefonni_cislo_s_prime_prefix(self):
        """Testuje zadání telefonního čísla s mezinárodní předvolbou +420."""
        cislo = self.uzivatelske_rozhrani._zadej_telefonni_cislo("Zadejte telefonní číslo:\n")
        self.assertEqual(cislo, "+420123456789")

    @patch('builtins.input', lambda _: "00420123456789")
    def test_zadej_telefonni_cislo_s_nulovym_prefixem(self):
        """Testuje zadání telefonního čísla s mezinárodní předvolbou 00420."""
        cislo = self.uzivatelske_rozhrani._zadej_telefonni_cislo("Zadejte telefonní číslo:\n")
        self.assertEqual(cislo, "00420123456789")        

    def test_vlozeni_pojistence(self):
        """Testuje vložení pojištěnce do seznamu. 
        Testuje, zda je pojištěnec správně vložen do kartotéky."""
        self.pojistenci.vloz_pojistence(self.pojistenec)
        self.assertIn(self.pojistenec, self.pojistenci.vydej_seznam())

    def test_prazdny_seznam(self):
        """Testuje, zda je kartotéka prázdná.
        Testuje, zda metoda prazdna_kartoteka funguje správně."""  
        self.pojistenci.delete_vsechny_pojistence()      
        self.assertTrue(self.pojistenci.je_prazdny_seznam())
        self.pojistenci.vloz_pojistence(self.pojistenec)
        self.assertFalse(self.pojistenci.je_prazdny_seznam())


    def test_vydej_seznam(self):
        """Testuje, zda metoda vydej_seznam vrací správný seznam pojištěnců."""
        self.pojistenci.delete_vsechny_pojistence() # Smaže všechny pojištěnce
        self.pojistenci.vloz_pojistence(self.pojistenec)  # Vloží pojištěnce do kartotéky
        seznam = self.pojistenci.vydej_seznam()  # Získá seznam pojištěnců
        self.assertEqual(len(seznam), 1)  # Ověří, že seznam obsahuje jednoho pojištěnce
        self.assertEqual(seznam[0], self.pojistenec)  # Ověří, že první pojištěnec v seznamu je ten, který byl vložen

    def test_vloz_pojistence(self):
        self.pojistenci.delete_vsechny_pojistence() # Smaže všechny pojištěnce
        pojistenec = Pojistenec("Jan", "Novak", "123456789", 30)  # Vytvoří nového pojištěnce
        self.pojistenci.vloz_pojistence(pojistenec)  # Vloží pojištěnce do kartotéky
        self.assertEqual(len(self.pojistenci.vydej_seznam()), 1)  # Ověří, že seznam obsahuje jednoho pojištěnce
        self.assertEqual(self.pojistenci.vydej_seznam()[0].jmeno, "Jan")  # Ověří, že jméno prvního pojištěnce v seznamu je "Jan"

    def test_vypis_pojistenci(self):
        pojistenec1 = Pojistenec("Jan", "Novak", "123456789", 30)  # Vytvoří prvního pojištěnce
        pojistenec2 = Pojistenec("Petr", "Svoboda", "987654321", 25)  # Vytvoří druhého pojištěnce
        self.pojistenci.vloz_pojistence(pojistenec1)  # Vloží prvního pojištěnce do kartotéky
        self.pojistenci.vloz_pojistence(pojistenec2)  # Vloží druhého pojištěnce do kartotéky
        pojistenci = self.pojistenci.vydej_seznam()  # Získá seznam pojištěnců
        self.uzivatelske_rozhrani.vypis_pojistence(pojistenci)  # Vypíše seznam pojištěnců

if __name__ == '__main__':
    unittest.main(testRunner=NewlineTextTestRunner()) # Spustí testy s vlastním testRunnerem, který vypisuje tečky s novým řádkem po každé tečce

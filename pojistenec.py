class Pojistenec:
    """reprezentuje jednoho pojištěnce"""

    def __init__(self, jmeno, prijmeni, tel, vek):
        """inicializuje pojištěnce"""
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel = tel
        self.vek = vek

    def __str__(self, prijmeni_width=15):
        """reprezentuje výpis pojištěnce
        Args:
            string prijmeni_width
        Returns 
            string jméno, příjmení, věk a telefon pojištěnce
        """
        # rjust https://www.geeksforgeeks.org/add-padding-to-a-string-in-python/
        return f"{self.jmeno.ljust(16,' ')} {self.prijmeni.ljust(prijmeni_width,' ')} {str(self.vek).ljust(8,' ')} {str(self.tel).ljust(16,' ')}"

class PojistenciManager:
    """reprezentuje manažera pojištěnců, inicializuje, vkládá, vrací pojištěnce"""

    def __init__(self,pojistenci=[]):
        """inicializuje seznam pojištěnců"""
        self._pojistenci=pojistenci 
        

    def vloz_pojistence(self, pojistenec):
        """
        vloží pojištěnce do seznamu pojišťenců
        Args: 
            object pojistenec
        """
        self._pojistenci.append(pojistenec)

    def vydej_seznam(self):
        """vrací seznam pojištěnců
        Returns 
            list seznam pojištěnců
        """
        return self._pojistenci

    def delete_vsechny_pojistence(self):
        """odstraní všechny pojištěnce ze seznamu pojištěnců
        """
        self._pojistenci.clear()
    
    def je_prazdny_seznam(self):
        """testuje seznam pojištěnců, zda je prázdný
        Returns
            bool True pokud je seznam prázdný, jinak False
        """
        return len(self._pojistenci)==0

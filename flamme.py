import random
from constantes import *

class Flamme:
    def __init__(self):
        pass

class TimerFlammes:
    def __init__(self):
        self.delai = random.randint(15, 25)
        

    def actualiser(self):
        nouvelleFlamme = Constantes.AUCUN
        self.delai -= 1

        if self.delai == 0:
            self.delai = random.randint(15, 25)
            nouvelleFlamme = random.randint(0, 2)

        return nouvelleFlamme
    
    def ajouterFlamme(self, tabFlammes, colonne):
        i = 0
        while i < 7 and tabFlammes[i][colonne] != None:
            i += 1
        tabFlammes[i][colonne] = Flamme()
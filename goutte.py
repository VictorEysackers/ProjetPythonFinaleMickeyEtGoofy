from goofy import*

class Goutte:
    def __init__ (self):
        self.ligne = 0
        self.etat = Constantes.NORMAL
    
    def actualiser(self, lGoutte):
        for i in range(len(lGoutte) -1, -1, -1):
            lGoutte[i].ligne += 1

            if lGoutte[i].ligne > 8:
                lGoutte.pop(i)


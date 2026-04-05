from goofy import*

class Goutte:
    def __init__ (self, ligne, colonne):
        self.ligne = ligne
        self.colonne = colonne
        self.etat = Constantes.NORMAL
        self.delaiTomb = 2
    
    def actualiser(self, lGoutte):
        finTuyau = False
        for i in range(len(lGoutte) -1, -1, -1):
            lGoutte[i].ligne += 1

            if lGoutte[i].ligne > 8:
                lGoutte.pop(i)
                finTuyau = True
        
        return finTuyau
    
    def actualiserGoutteTomb(self, lGoutteTomb):
        self.delaiTomb -= 1
        if self.delaiTomb == 0:
            self.delaiTomb = 2
            for i in range(len(lGoutteTomb) -1, -1, -1):
                lGoutteTomb[i].ligne -= 1

                if lGoutteTomb[i].ligne < 1:
                    lGoutteTomb.pop(i)

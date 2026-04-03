from presentation import *
from mickey import *
from goofy import *
from goutte import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()
        self.mickey = Mickey()
        self.goofy = Goofy()
        self.goutte = Goutte()
        self.lGoutte = []
        

    # ----------------------------------------------------------------------------

    def demarrer(self):
        i = 0
        while True:
            evenement = self.presentation.lireEvenement()
            changementM = self.mickey.actualiser(evenement)
            changementG = self.goofy.actualiser(self.mickey)

            if self.mickey.ligne == 1 and changementM == True:
                self.goutte.actualiser(self.lGoutte)
                i += 1
                if i == 2:
                    i = 0
                    self.lGoutte.append(Goutte())
            elif changementG == True:
                self.goutte.actualiser(self.lGoutte)
                i += 1
                if i == 2:
                    i = 0
                    self.lGoutte.append(Goutte())

            #if self.lGoutte:
            #    self.goutte.actualiser(self.lGoutte)

            self.actualiserEcran()

            time.sleep(0.1)

    # ----------------------------------------------------------------------------

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherMickey(self.mickey.ligne, self.mickey.action)
        self.presentation.afficherGoofy(self.goofy.action)

        for i in range(len(self.lGoutte)):
            self.presentation.afficherGoutteTuyau(self.lGoutte[i].ligne, self.lGoutte[i].etat)

        self.presentation.afficherCrochet()

        self.presentation.actualiserFenetreGraphique()


from presentation import *
from mickey import *
from goofy import *
from goutte import *
from donald import *
from flamme import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()
        self.mickey = Mickey()
        self.goofy = Goofy()
        self.donald = Donald()
        self.goutte = Goutte(0, 0)
        self.lGoutte = []
        self.lGoutteTomb = []
        self.TimerFlammes = TimerFlammes()
        self.flammes = [[Flamme(), Flamme(), Flamme()],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None]]
        

    # ----------------------------------------------------------------------------

    def demarrer(self):
        i = 0
        while True:
            finTuyau = False   

            evenement = self.presentation.lireEvenement()
            self.donald.actualiser(evenement)
            changementM = self.mickey.actualiser(evenement)
            changementG = self.goofy.actualiser(self.mickey)

            if self.mickey.ligne == 1 and changementM == True:
                finTuyau = self.goutte.actualiser(self.lGoutte)
                i += 1
                if i == 2:
                    i = 0
                    self.lGoutte.append(Goutte(1, 0))
            elif changementG == True:
                finTuyau = self.goutte.actualiser(self.lGoutte)
                i += 1
                if i == 2:
                    i = 0
                    self.lGoutte.append(Goutte(1, 0))

            nouvelleFlamme = self.TimerFlammes.actualiser()
            if nouvelleFlamme != Constantes.AUCUN:
                self.TimerFlammes.ajouterFlamme(self.flammes, nouvelleFlamme)

            if finTuyau == True:
                self.lGoutteTomb.append(Goutte(7, self.donald.colonne))
            
            if self.lGoutteTomb:
                self.goutte.actualiserGoutteTomb(self.lGoutteTomb, self.flammes)

            

            self.actualiserEcran()

            time.sleep(0.1)

    # ----------------------------------------------------------------------------

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherMickey(self.mickey.ligne, self.mickey.action)
        self.presentation.afficherGoofy(self.goofy.action)
        self.presentation.afficherDonald(self.donald.colonne)

        for i in range(len(self.lGoutte)):
            self.presentation.afficherGoutteTuyau(self.lGoutte[i].ligne, self.lGoutte[i].etat)

        for i in range(len(self.lGoutteTomb)):
            self.presentation.afficherGoutteVersFlammes(self.lGoutteTomb[i].ligne, self.lGoutteTomb[i].colonne,\
                                                         self.lGoutteTomb[i].etat)

        for i in range(7):
            for j in range(3):
                if self.flammes[i][j] != None:
                    self.presentation.afficherFlamme(i + 1, j + 1)

        self.presentation.afficherCrochet()

        self.presentation.actualiserFenetreGraphique()


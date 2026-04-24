from presentation import *
from mickey import *
from goofy import *
from goutte import *
from donald import *
from flamme import *
import random

class Jeu:
    def __init__(self):
        self.presentation = Presentation()
        self.mickey = Mickey()
        self.goofy = Goofy()
        self.donald = Donald()
        self.goutte = Goutte(0, 0, 0)
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
        self.score = 0
        self.nbrEchecs = 0

    
        

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
                    self.lGoutte.append(Goutte(1, self.donald.colonne, random.randint(1, 4)))
            elif changementG == True:
                finTuyau = self.goutte.actualiser(self.lGoutte)
                i += 1
                if i == 2:
                    i = 0
                    self.lGoutte.append(Goutte(1, self.donald.colonne, random.randint(1, 4)))

            nouvelleFlamme = self.TimerFlammes.actualiser()
            if nouvelleFlamme != Constantes.AUCUN:
                defaite = self.TimerFlammes.ajouterFlamme(self.flammes, nouvelleFlamme)

                if defaite == True:
                    self.nbrEchecs += 1

                    if self.nbrEchecs < 3:
                        self.donald.etat = "echec1"
                        self.actualiserEcran()
                        time.sleep(1)

                        self.donald.etat = "echec2"
                        self.actualiserEcran()
                        time.sleep(2)

                        self.resetApresEchec()
                        self.donald.etat = "normal"

                    else:
                        self.donald.etat = "echec1"
                        self.actualiserEcran()
                        time.sleep(1)

                        self.donald.etat = "echec2"
                        self.actualiserEcran()
                        time.sleep(2)
                        break



            if finTuyau != False:
                self.lGoutteTomb.append(Goutte(7, self.donald.colonne, finTuyau))
            
            if self.lGoutteTomb:
                addScore = self.goutte.actualiserGoutteTomb(self.lGoutteTomb, self.flammes)
                if addScore > 0:
                    self.score += addScore
                    present = 0
                    for l in range(7):
                        for c in range(3):
                            if self.flammes[l][c] != None:
                                present = 1

                    if present == 0:
                        self.score += 10

                        self.mickey.etat = "m&mi1"
                        self.actualiserEcran()
                        time.sleep(1)

                        self.mickey.etat = "m&mi2"
                        self.actualiserEcran()
                        time.sleep(1)

                        self.mickey.etat = "m&mi3"
                        self.actualiserEcran()
                        time.sleep(1)

                        self.resetApresEchec()
                        self.mickey.etat = "normal"


            self.actualiserEcran()

            time.sleep(0.1)

        #fin du jeu freeze --------------------------------------
        self.presentation.attendreFermetureFenetre()
        
        pygame.exit()
        exit()

    # ----------------------------------------------------------------------------

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        if self.mickey.etat == "normal":
            self.presentation.afficherMickey(self.mickey.ligne, self.mickey.action)
        elif self.mickey.etat == "m&mi1":
            self.presentation.afficherMickeyMinnie(1)
        elif self.mickey.etat == "m&mi2":
            self.presentation.afficherMickeyMinnie(2)
        else:
            self.presentation.afficherMickeyMinnie(3)
            

        self.presentation.afficherGoofy(self.goofy.action)


        if self.donald.etat == "normal":
            self.presentation.afficherDonald(self.donald.colonne)
            self.presentation.afficherCrochet()
        elif self.donald.etat == "echec1":
            self.presentation.afficherDonaldEchec(1)
            self.presentation.afficherCrochet()
        else:
            self.presentation.afficherDonaldEchec(2)


        for i in range(len(self.lGoutte)):
            self.presentation.afficherGoutteTuyau(self.lGoutte[i].ligne, self.lGoutte[i].etat)

        for i in range(len(self.lGoutteTomb)):
            self.presentation.afficherGoutteVersFlammes(self.lGoutteTomb[i].ligne, self.lGoutteTomb[i].colonne,\
                                                         self.lGoutteTomb[i].etat)

        for i in range(7):
            for j in range(3):
                if self.flammes[i][j] != None:
                    self.presentation.afficherFlamme(i + 1, j + 1)

        
        self.presentation.afficherScore(self.score)
        self.presentation.afficherEchecs(self.nbrEchecs)

        self.presentation.actualiserFenetreGraphique()


    def resetFlammes(self):
        self.flammes = [[Flamme(), Flamme(), Flamme()],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None],
                        [None, None, None]]
        
    def resetGouttes(self):
        self.lGoutte = []
        self.lGoutteTomb = []

    def resetApresEchec(self):
        self.resetFlammes()
        self.resetGouttes()
        self.mickey.ligne = 1
        self.donald.colonne = 2
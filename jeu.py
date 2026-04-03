from presentation import *
from mickey import *
from goofy import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()
        self.mickey = Mickey()
        self.goofy = Goofy()

    # ----------------------------------------------------------------------------

    def demarrer(self):
        while True:
            evenement = self.presentation.lireEvenement()
            self.mickey.actualiser(evenement)
            self.goofy.actualiser(self.mickey)

            self.actualiserEcran()

            time.sleep(0.1)

    # ----------------------------------------------------------------------------

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherMickey(self.mickey.ligne, self.mickey.action)
        self.presentation.afficherGoofy(self.goofy.action)
        self.presentation.afficherCrochet()

        self.presentation.actualiserFenetreGraphique()


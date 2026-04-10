from constantes import *
import pygame

class Mickey:
    def __init__(self):
        self.delai = 2
        self.ligne = 1
        self.action = Constantes.HAUT
        self.etat = "normal"

    def actualiser(self, evenement):
        self.delai -= 1
        changement = False

        if self.delai == 0:
            self.delai = 2
            if self.action == Constantes.HAUT:
                self. action = Constantes.BAS
                changement = True
            else:
                self.action = Constantes.HAUT

        if evenement == pygame.K_UP:
            if self.ligne + 1 < 4:
                self.ligne += 1

        elif evenement == pygame.K_DOWN:
            if self.ligne == 3:
                self.ligne = 2
            elif self.ligne == 2:
                self.ligne = 1
                self.delay = 0

        return changement
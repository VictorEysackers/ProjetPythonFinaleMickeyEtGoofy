import pygame

class Donald:
    def __init__(self):
        self.colonne = 2

    def actualiser(self, evenement):
        if evenement == pygame.K_LEFT:
            if self.colonne -1 > 0:
                self.colonne -= 1
        elif evenement == pygame.K_RIGHT:
            if self.colonne + 1 < 4:
                self.colonne += 1
    
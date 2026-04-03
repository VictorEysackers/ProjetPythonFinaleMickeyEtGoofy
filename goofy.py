from constantes import *
from mickey import *
import pygame

class Goofy:
    def __init__(self):
        self.delai = 4
        self.ligne = 1
        self.action = Constantes.HAUT
    
    def actualiser(self, mickey):
        if mickey.ligne == 1:
            self.action = mickey.action
        else:
            self.delai -= 1
            if self.delai == 0:
                self.delai = 4
                if self.action == Constantes.HAUT:
                    self.action = Constantes.BAS
                else:
                    self.action = Constantes.HAUT
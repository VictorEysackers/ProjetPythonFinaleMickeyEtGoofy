import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import pygame
import time
from constantes import *

class Presentation:
    def __init__(self):
        pygame.init()

        # charger toutes les images du jeu

        self.imgFondEcran = pygame.image.load("images/autre/fond_ecran.png")

        self.imgEchec = pygame.image.load("images/autre/echec.png")
        self.imgCrochet = pygame.image.load("images/autre/crochet.png")

        self.imgMickey1Bas = pygame.image.load("images/mickey/mickey1_bas.png")
        self.imgMickey1Haut = pygame.image.load("images/mickey/mickey1_haut.png")
        self.imgMickey2 = pygame.image.load("images/mickey/mickey2.png")
        self.imgMickey3 = pygame.image.load("images/mickey/mickey3.png")

        self.imgMickeyMinnie1 = pygame.image.load("images/mickey/mickey_minnie1.png")
        self.imgMickeyMinnie2 = pygame.image.load("images/mickey/mickey_minnie2.png")
        self.imgMickeyMinnie3 = pygame.image.load("images/mickey/mickey_minnie3.png")

        self.imgGoofyBas = pygame.image.load("images/goofy/goofy_bas.png")
        self.imgGoofyHaut = pygame.image.load("images/goofy/goofy_haut.png")

        self.imgDonald1 = pygame.image.load("images/donald/donald1.png")
        self.imgDonald2 = pygame.image.load("images/donald/donald2.png")
        self.imgDonald3 = pygame.image.load("images/donald/donald3.png")
        self.imgDonaldEchec1 = pygame.image.load("images/donald/donald_echec1.png")
        self.imgDonaldEchec2 = pygame.image.load("images/donald/donald_echec2.png")

        self.imgGoutteMonteeNormal1 = pygame.image.load("images/goutte/goutte_normal1.png")
        self.imgGoutteMonteeNormal2 = pygame.image.load("images/goutte/goutte_normal2.png")
        self.imgGoutteMonteeNormal3 = pygame.image.load("images/goutte/goutte_normal3.png")
        self.imgGoutteMonteeNormal4 = pygame.image.load("images/goutte/goutte_normal4.png")
        self.imgGoutteMonteeAnormal1 = pygame.image.load("images/goutte/goutte_anormal1.png")
        self.imgGoutteMonteeAnormal2 = pygame.image.load("images/goutte/goutte_anormal2.png")
        self.imgGoutteMonteeAnormal3 = pygame.image.load("images/goutte/goutte_anormal3.png")
        self.imgGoutteMonteeAnormal4 = pygame.image.load("images/goutte/goutte_anormal4.png")
        self.imgGoutteMonteeFuite1 = pygame.image.load("images/goutte/goutte_fuite1.png")
        self.imgGoutteMonteeFuite2 = pygame.image.load("images/goutte/goutte_fuite2.png")
        self.imgGoutteDescenteNormalBas = pygame.image.load("images/goutte/goutte_normal_droite.png")
        self.imgGoutteDescenteAnormalBas = pygame.image.load("images/goutte/goutte_anormal_droite.png")

        self.imgFlammeBas1 = pygame.image.load("images/flamme/flamme_bas1.png")
        self.imgFlammeBas2 = pygame.image.load("images/flamme/flamme_bas2.png")
        self.imgFlammeBas3 = pygame.image.load("images/flamme/flamme_bas3.png")
        self.imgFlammeNormal = pygame.image.load("images/flamme/flamme_normal.png")
        self.imgFlammeHaut1 = pygame.image.load("images/flamme/flamme_haut1.png")
        self.imgFlammeHaut2 = pygame.image.load("images/flamme/flamme_haut2.png")

        self.imgChiffre0 = pygame.image.load("images/chiffres/0.png")
        self.imgChiffre1 = pygame.image.load("images/chiffres/1.png")
        self.imgChiffre2 = pygame.image.load("images/chiffres/2.png")
        self.imgChiffre3 = pygame.image.load("images/chiffres/3.png")
        self.imgChiffre4 = pygame.image.load("images/chiffres/4.png")
        self.imgChiffre5 = pygame.image.load("images/chiffres/5.png")
        self.imgChiffre6 = pygame.image.load("images/chiffres/6.png")
        self.imgChiffre7 = pygame.image.load("images/chiffres/7.png")
        self.imgChiffre8 = pygame.image.load("images/chiffres/8.png")
        self.imgChiffre9 = pygame.image.load("images/chiffres/9.png")

        # créer la fenêtre avec l'image du fond et le titre

        pygame.display.set_caption("Mickey & Donald")
        pygame.display.set_icon(pygame.image.load("images/autre/iconeFenetre.png"))
        self.ecran = pygame.display.set_mode((973, 774))
        self.ecran.blit(self.imgFondEcran, (0, 0))

        pygame.display.update()

    # ------------------------------------------------------------------------

    def lireEvenement(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key in [pygame.K_UP, pygame.K_RIGHT,
                                     pygame.K_DOWN, pygame.K_LEFT]:
                    return evenement.key
        return Constantes.AUCUN

    # ------------------------------------------------------------------------

    def attendreFermetureFenetre(self):
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(0.2)

    # ------------------------------------------------------------------------

    def afficherMickey(self, ligne, action = Constantes.AUCUN):
        if ligne == 1 and action == Constantes.BAS:
            self.afficherImage(91, 532, self.imgMickey1Bas)
        if ligne == 1 and action == Constantes.HAUT:
            self.afficherImage(91, 532, self.imgMickey1Haut)
        elif ligne == 2:
            self.afficherImage(65, 423, self.imgMickey2)
        elif ligne == 3:
            self.afficherImage(67, 218, self.imgMickey3)

    # ------------------------------------------------------------------------

    def afficherMickeyMinnie(self, num):
        if num == 1:
            self.afficherImage(440, 514, self.imgMickeyMinnie1)
        elif num == 2:
            self.afficherImage(440, 514, self.imgMickeyMinnie2)
        elif num == 3:
            self.afficherImage(440, 514, self.imgMickeyMinnie3)

    # ------------------------------------------------------------------------

    def afficherGoofy(self, action):
        if action == Constantes.BAS:
            self.afficherImage(178, 594, self.imgGoofyBas)
        elif action == Constantes.HAUT:
            self.afficherImage(178, 594, self.imgGoofyHaut)

    # ------------------------------------------------------------------------

    def afficherDonald(self, colonne):
        if colonne == 1:
            self.afficherImage(217, 36, self.imgDonald1)
        elif colonne == 2:
            self.afficherImage(307, 35, self.imgDonald2)
        elif colonne == 3:
            self.afficherImage(396, 36, self.imgDonald3)

    # ------------------------------------------------------------------------

    def afficherDonaldEchec(self, num):
        if num == 1:
            self.afficherImage(259, 140, self.imgFlammeHaut1)
            self.afficherImage(355, 140, self.imgFlammeHaut2)
            self.afficherImage(464, 7, self.imgDonaldEchec1)
        elif num == 2:
            self.afficherImage(259, 140, self.imgFlammeHaut1)
            self.afficherImage(355, 140, self.imgFlammeHaut2)
            self.afficherImage(474, 215, self.imgDonaldEchec2)

    # ------------------------------------------------------------------------

    def afficherCrochet(self):
        self.afficherImage(489, 167, self.imgCrochet)

    # ------------------------------------------------------------------------

    def afficherGoutteTuyau(self, ligne, type = Constantes.NORMAL):
        if type == Constantes.NORMAL:
            if ligne == 1:
                self.afficherImage(5, 667, self.imgGoutteMonteeNormal1)
            elif ligne == 2:
                self.afficherImage(-4, 585, self.imgGoutteMonteeNormal2)
            elif ligne == 3:
                self.afficherImage(-4, 507, self.imgGoutteMonteeNormal2)
            elif ligne == 4:
                self.afficherImage(-4, 417, self.imgGoutteMonteeNormal2)
            elif ligne == 5:
                self.afficherImage(-4, 337, self.imgGoutteMonteeNormal2)
            elif ligne == 6:
                self.afficherImage(-4, 257, self.imgGoutteMonteeNormal2)
            elif ligne == 7:
                self.afficherImage(31, 173, self.imgGoutteMonteeNormal3)
            elif ligne == 8:
                self.afficherImage(93, 154, self.imgGoutteMonteeNormal4)
        elif type == Constantes.ANORMAL:
            if ligne == 1:
                self.afficherImage(5, 667, self.imgGoutteMonteeAnormal1)
            elif ligne == 2:
                self.afficherImage(-5, 585, self.imgGoutteMonteeAnormal2)
            elif ligne == 3:
                self.afficherImage(-5, 507, self.imgGoutteMonteeAnormal2)
            elif ligne == 4:
                self.afficherImage(-5, 417, self.imgGoutteMonteeAnormal2)
            elif ligne == 5:
                self.afficherImage(-5, 337, self.imgGoutteMonteeAnormal2)
            elif ligne == 6:
                self.afficherImage(-5, 257, self.imgGoutteMonteeAnormal2)
            elif ligne == 7:
                self.afficherImage(31, 171, self.imgGoutteMonteeAnormal3)
            elif ligne == 8:
                self.afficherImage(93, 154, self.imgGoutteMonteeAnormal4)
        elif type == Constantes.FUITE:
            if ligne == 4:
                self.afficherImage(14, 466, self.imgGoutteMonteeFuite1)
            elif ligne == 7:
                self.afficherImage(21, 208, self.imgGoutteMonteeFuite2)

    # ------------------------------------------------------------------------

    def afficherGoutteVersFlammes(self, ligne, colonne, type):
        if colonne >= 1 and colonne <= 3:
            if type == Constantes.NORMAL:
                if ligne == 1:
                    self.afficherImage(228 + (colonne - 1) * 78, 555, self.imgGoutteDescenteNormalBas)
                elif ligne == 2:
                    self.afficherImage(228 + (colonne - 1) * 78, 516, self.imgGoutteDescenteNormalBas)
                elif ligne == 3:
                    self.afficherImage(228 + (colonne - 1) * 78, 454, self.imgGoutteDescenteNormalBas)
                elif ligne == 4:
                    self.afficherImage(228 + (colonne - 1) * 78, 392, self.imgGoutteDescenteNormalBas)
                elif ligne == 5:
                    self.afficherImage(228 + (colonne - 1) * 78, 308, self.imgGoutteDescenteNormalBas)
                elif ligne == 6:
                    self.afficherImage(228 + (colonne - 1) * 78, 246, self.imgGoutteDescenteNormalBas)
                elif ligne == 7:
                    self.afficherImage(228 + (colonne - 1) * 78, 185, self.imgGoutteDescenteNormalBas)
            elif type == Constantes.ANORMAL:
                if ligne == 1:
                    self.afficherImage(228 + (colonne - 1) * 78, 553, self.imgGoutteDescenteAnormalBas)
                elif ligne == 2:
                    self.afficherImage(228 + (colonne - 1) * 78, 516, self.imgGoutteDescenteAnormalBas)
                elif ligne == 3:
                    self.afficherImage(228 + (colonne - 1) * 78, 454, self.imgGoutteDescenteAnormalBas)
                elif ligne == 4:
                    self.afficherImage(228 + (colonne - 1) * 78, 392, self.imgGoutteDescenteAnormalBas)
                elif ligne == 5:
                    self.afficherImage(228 + (colonne - 1) * 78, 308, self.imgGoutteDescenteAnormalBas)
                elif ligne == 6:
                    self.afficherImage(228 + (colonne - 1) * 78, 246, self.imgGoutteDescenteAnormalBas)
                elif ligne == 7:
                    self.afficherImage(228 + (colonne - 1) * 78, 185, self.imgGoutteDescenteAnormalBas)

    # ------------------------------------------------------------------------

    def afficherFlamme(self, ligne, colonne):
        if colonne >= 1 and colonne <= 3:
            if ligne == 1:
                if colonne == 1:
                    self.afficherImage(243, 570, self.imgFlammeBas1)
                elif colonne == 2:
                    self.afficherImage(301, 565, self.imgFlammeBas2)
                elif colonne == 3:
                    self.afficherImage(358, 568, self.imgFlammeBas3)
            elif ligne == 2:
                self.afficherImage(228 + (colonne - 1) * 79, 536, self.imgFlammeNormal)
            elif ligne == 3:
                self.afficherImage(228 + (colonne - 1) * 79, 474, self.imgFlammeNormal)
            elif ligne == 4:
                self.afficherImage(228 + (colonne - 1) * 79, 412, self.imgFlammeNormal)
            elif ligne == 5:
                self.afficherImage(228 + (colonne - 1) * 79, 328, self.imgFlammeNormal)
            elif ligne == 6:
                self.afficherImage(228 + (colonne - 1) * 79, 266, self.imgFlammeNormal)
            elif ligne == 7:
                self.afficherImage(228 + (colonne - 1) * 79, 206, self.imgFlammeNormal)

    # ------------------------------------------------------------------------

    def afficherEchecs(self, nbEchecs):
        for i in range(nbEchecs):
            self.afficherImage(718 + (i * 49), 445, self.imgEchec)

    # ------------------------------------------------------------------------

    def afficherScore(self, score):
        self.afficherChiffre(692, int(score / 1000))
        self.afficherChiffre(741, int(score / 100) % 10)
        self.afficherChiffre(790, int(score / 10) % 10)
        self.afficherChiffre(839, score % 10)

    # ------------------------------------------------------------------------

    def afficherChiffre(self, position, chiffre):
        if chiffre == 0:
            self.afficherImage(position, 289, self.imgChiffre0)
        elif chiffre == 1:
            self.afficherImage(position, 289, self.imgChiffre1)
        elif chiffre == 2:
            self.afficherImage(position, 289, self.imgChiffre2)
        elif chiffre == 3:
            self.afficherImage(position, 289, self.imgChiffre3)
        elif chiffre == 4:
            self.afficherImage(position, 289, self.imgChiffre4)
        elif chiffre == 5:
            self.afficherImage(position, 289, self.imgChiffre5)
        elif chiffre == 6:
            self.afficherImage(position, 289, self.imgChiffre6)
        elif chiffre == 7:
            self.afficherImage(position, 289, self.imgChiffre7)
        elif chiffre == 8:
            self.afficherImage(position, 289, self.imgChiffre8)
        elif chiffre == 9:
            self.afficherImage(position, 289, self.imgChiffre9)

    # ------------------------------------------------------------------------

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.ecran.blit(image, rect)

    # ------------------------------------------------------------------------

    def effacerImageInterne(self):
        self.ecran.blit(self.imgFondEcran, (0, 0, 973, 774), (0, 0, 973, 774))

    # ------------------------------------------------------------------------

    def actualiserFenetreGraphique(self):
        pygame.display.update()
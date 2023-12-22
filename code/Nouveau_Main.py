# coding utf-8:
'''
HARRY POTTER SE FAIT LA MALLE

REGLES:
CLASSEMENT ET CSV:
Les données tirés de l'univers d'Harry Potter sont importés du fichier CSV
BONUS:
Le jeu possède également une interface graphique dont le code commence à la ligne.....
AUTEURS:
Eliot CAIMARI LAUNAY, Arthur CHARUEL, Cyprien VENARD 
LICENCE:
Aucune
VERSION:
2.1
DATE DE DERNIERE REVISION:
20/12/2023
ADRESSE GITHUB: 
https://github.com/Cypri3n/La-Malle
'''

#import des modules
import pygame
import sys

def main_menu():
    current_background = pygame.image.load("images/main.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(current_background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/jouer.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/settingsbleu.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("La-Malle-main/images/logout_1828427.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    current_background = pygame.image.load("path/to/play/background.jpg")
                    play()
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    current_background = pygame.image.load("path/to/options/background.jpg")
                    options()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



def fleury_et_bott(a_rendre_fleury_et_bott):
    '''
    Permet de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est infini.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus

    DOCTEST:
    >>> fleury_et_bott(0)
    
    >>> fleury_et_bott(60)
  
    >>> fleury_et_bott(63)
 
    >>> fleury_et_bott(231)
     
    >>> fleury_et_bott(899)
    
    '''
    
    dico_billets = {500 : 0,
                    200 : 0,
                    100 : 0,
                    50 : 0,
                    20 : 0,
                    10 : 0,
                    5 : 0,
                    2 : 0,
                    1 : 0}
    
    
    if a_rendre_fleury_et_bott <= 0:
        print("Je suis navré, mais je ne peux pas vous rembourser une somme inéxistante")
    else:
       print(f"Je vais dès à présent vous rendre {a_rendre_fleury_et_bott} euros : ")
       print()
    
    
    
    
    for billet in dico_billets:
        if a_rendre_fleury_et_bott >= billet:
            nb_billets = a_rendre_fleury_et_bott // billet
            dico_billets[billet] = nb_billets
            a_rendre_fleury_et_bott -= nb_billets * billet
    for j in dico_billets:
        if dico_billets[j] >= 1:
            print(f"Je vous dois {dico_billets[j]} billet(s) de {j}")
    print()
    
    
    
    
    return dico_billets




def madame_guipure(a_rendre_madame_guipure):
    '''
    Permet de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est limitée.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus
    
        DOCTEST:
    >>> madame_guipure(0)
    
    >>> madame_guipure(17)
  
    >>> madame_guipure(68)
 
    >>> madame_guipure(231)
     
    >>> madame_guipure(497)

    >>> madame_guipure(842)
    '''

    caisse = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    rendu_monnaie_1 = {}

    print(f"Bonjour Harry, je vous dois {a_rendre_madame_guipure} euros.")

    for coupure in caisse:
        if coupure <= a_rendre_madame_guipure and caisse[coupure] > 0:
            nb_coupures = min(a_rendre_madame_guipure // coupure, caisse[coupure])
            rendu_monnaie_1[coupure] = nb_coupures
            a_rendre_madame_guipure -= nb_coupures * coupure
            caisse[coupure] -= nb_coupures
            
    if a_rendre_madame_guipure > 0:
        print("Je ne peux pas vous remboursez totalement, mais je vous verse le contenu de ma caisse.")
        rendu_monnaie_2 = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    else:
        print("Je peux donc vous rendre la monnaie.")
        rendu_monnaie_2 = rendu_monnaie_1
    
    for j in rendu_monnaie_1:
        print(f"Je vous rend {rendu_monnaie_1[j]} billet(s) de {j}")
    return rendu_monnaie_2            



def ollivander(a_rendre_gallions, a_rendre_mornilles, a_rendre_noises):
    '''
    Permet de rendre la monnaie à Harry avec le moins de pièces
    possibles en sachant que la caisse du libraire est infinie et qu'il faut convetir les monnaies en plusieurs devises.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus
    
        DOCTEST:
    >>> madame_guipure(0)
    
    >>> madame_guipure(17)
  
    >>> madame_guipure(68)
 
    >>> madame_guipure(231)
     
    >>> madame_guipure(497)

    >>> madame_guipure(842)
    '''
    
    
    dico_billets = {493: 0, 29: 0, 1: 0}
    
    dico_billets[493] = a_rendre_gallions
    dico_billets[29] = a_rendre_mornilles
    dico_billets[1] = a_rendre_noises
    
    if a_rendre_gallions <= 0 and a_rendre_mornilles <= 0 and a_rendre_noises <= 0:
        print("Je ne peux pas te rembourser si je ne te dois rien !")
    else:
        for i in dico_billets:
            while dico_billets[1] >= 29:
                dico_billets[29] += 1 
                dico_billets[1] -= 29
            while dico_billets[29] >= 17:
                dico_billets[493] += 1
                dico_billets[29] -= 17            
        print(f"Je te rends {dico_billets[493]} Gallions, {dico_billets[29]} Mornilles, et {dico_billets[1]} Noises !")
        return dico_billets




#   PARTIE 2 : Interface homme machine 

def boutiques():
    '''
    Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.'
    Entrées : Le nom de la boutique sous forme de chaine de caractères
              
    Sorties : Redirige le joueur vers une autre fonction
              Renvoie le résultat lié a cette dernière (documentés separemment)  
    '''
    liste_valeurs_fleury_et_bott = [0, 60, 63, 231, 899]
    liste_valeurs_madame_guipure = [0, 17, 68, 231, 497, 842]
    liste_valeurs_ollivander = [(0, 0, 0), (0, 0, 654), (2, 11, 9), (7, 531, 451)]
    
    choix_chemin_traverse = int(input("Souhaitez vous rester sur le chemin de traverse ? Saisissez 1 pour oui et 2 pour non : "))
    if choix_chemin_traverse == 1:
        print("Dans quelle boutique souhaitez vous aller ?")
        choix_boutiques = int(input("Saisissez 1 pour aller chez Fleury et Bott, 2 pour aller Cherz Madame Guipure, et 3 pour aller chez Ollivander : "))

        assert choix_boutiques in {1, 3}, "Veuillez entrer 1 ou 2 pour effectuer une action"

        if choix_boutiques == 1:
            main_menu()
            choix_somme_rendre = int(input("Souhaitez vous essayer les sommes à rendre du magasin en tappant 1, ou essayer vos propres sommes en tappant 2 : "))
            if choix_somme_rendre == 1:
                for valeur in liste_valeurs_fleury_et_bott:
                    fleury_et_bott(valeur)
            else:
                choix_somme_a_rendre = int(input("Quelle somme souhaitez vous tester ? "))
                fleury_et_bott(choix_somme_a_rendre)
            choix_rester = int(input("Veuillez entrer 1 pour rester ou 2 pour retourner au chemin de traverse : "))
            while choix_rester == 1:
                    choix_somme_rendre = int(input("Souhaitez vous essayer les sommes à rendre du magasin en tappant 1, ou essayer vos propres sommes en tappant 2 : "))
                    if choix_somme_rendre == 1:
                        for valeur in liste_valeurs_fleury_et_bott:
                            fleury_et_bott(valeur)
                        print("Souhaitez vous maintenant rester dans notre boutique ou retourner au chemin de traverse")
                        choix_rester = int(input("Saisissez 1 pour rester ou 2 pour retourner au chemin de traverse : "))
                    else:
                        choix_somme_a_rendre = int(input("Quelles somme souhaitez vous tester ? "))
                        fleury_et_bott(choix_somme_a_rendre)
                        print("Souhaitez vous maintenant rester dans notre boutique ou retourner au chemin de traverse")
                        choix_rester = int(input("Saisissez 1 pour rester ou 2 pour retourner au chemin de traverse : "))
            else:
                boutiques()
        
        
        
        elif choix_boutiques == 2:
            main_menu()
            a_rendre_madame_guipure = int(input("Bonjour et bienvenu chez Madame Guipure, quelle somme dois-je vous rendre ? "))
            madame_guipure(a_rendre_madame_guipure)
        
        
        
        
        else:
            main_menu()
            a_rendre_galions = int(input("Bonjour et bienvenu chez Ollivander, combien de Galions dois-je te rendre ? "))
            a_rendre_mornilles = int(input("Maintenant, combien de Mornilles te dois-je ? "))
            a_rendre_noises = int(input("Finallement, combien de petite Noises te faut-il ? "))
            ollivander(a_rendre_galions, a_rendre_mornilles, a_rendre_noises)
    else:
        print("Au revoir Harry !")
boutiques()









pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Akhy se fait la malle")
TEXT_COLOR = (255, 255, 255)

def get_font(size):
    return pygame.font.Font("La-Malle-main/Roboto/Roboto-Black.ttf", size)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.original_image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.original_image is None:
            self.image = self.text
        else:
            button_size = (200, 80)  # Set the desired button size (width, height)
            self.image = self.resize_image(self.original_image, button_size)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def resize_image(self, image, size):
        # Resize the image while preserving the aspect ratio
        aspect_ratio = image.get_width() / image.get_height()
        new_width = int(size[1] * aspect_ratio)
        return pygame.transform.scale(image, (new_width, size[1]))

    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.original_image is None:
            screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            return True
        return False

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)




    

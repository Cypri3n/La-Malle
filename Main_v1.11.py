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
1.1


DATE DE DERNIERE REVISION:
24/11/2023


ADRESSE GITHUB: 
https://github.com/Cypri3n/La-Malle

'''

#coding: utf-8
#import des modules

from random import randint





'''
Fonction qui rembourse Harry lors de ses achats des livres.
'''
def fleury_et_bott():
    print()
    print("Bienvenu chez Fleury et Bott !")
    a_rendre = int(input("Veuillez saisir la somme à rendre pour l'achat des livres': "))
    choix_achat = input("Souhaitez vous acheter ces livres ? ")
    if choix_achat == 'oui' or choix_achat == 'Oui':
        print(f"Je dois vous rembourser {a_rendre} euros")
        liste_billets = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        liste_pieces = []
        i = len(liste_billets) - 1
        while a_rendre > 0:
            valeur = liste_billets[i]
            if a_rendre < valeur:
                i -= 1
            else:
                liste_pieces.append(valeur)
                a_rendre -= valeur
            
        print()
        for i in range(len(liste_pieces)):
            print(f"Je te dois 1 billets de {liste_pieces[i]} euros")
    else:
        print("Vous êtes sorti de chez FLeury et Bott !")
    print()
    choix_retour = input("Souhaitez vous retourner au Chemin de Traverse ? ")
    if choix_retour == 'oui' or choix_retour == 'Oui':
        boutiques()
        
    
            
    
    



def madame_guipure():
    print()
    print("Bienvenu chez Madame Guipure !")
    #cout de la robe noire 
    prix = randint(800, 1000)
    prix_reduit = randint(8, 800)
    reponse = input(f"Bonjour l'ami Potter, la robe noire est en promotion à {prix_reduit} euros au lieu de {prix} euros, souhaitez vous l'acheter ?")
    if reponse == 'oui':               
        print(f'Splendide ! Vous me devez {prix_reduit} euros jeune sorcier')
    dico_billets = { 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0 }
    dico_billets_a_rendre = {
    200: 1,
    100: 3,
    50: 1,
    20: 1,
    10: 1,
    5: 1,
    2: 5,
    }

    


def ollivander():
    un_gallion = 493
    une_mornille = 29
    une_noise = 1
    baguette = 1151
    argent_donne_akhy = 2465
    print(une_mornille)
    
    



'''
Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.'
'''

def boutiques():
    liste_boutiques = ['Chez Fleury et Bott', 'chez fleury et bott', 'fleury et bott', 'Chez Madame Guipure', 'chez madame guipure', 'madame guipure', 'Chez Ollivander']
    print(liste_boutiques[2])
    choix_boutiques = input("Dans quelle boutique souhaitez vous aller: Chez Fleury et Bott, Chez Madame Guipure, ou Chez Ollivander ?  ")
    if choix_boutiques not in liste_boutiques:
        print("Vous êtes sorti du Chemin de Traverse...")
    if choix_boutiques == liste_boutiques[0] or choix_boutiques == liste_boutiques[1] or choix_boutiques == liste_boutiques[2]:
        fleury_et_bott()
    elif choix_boutiques == liste_boutiques[3] or choix_boutiques == liste_boutiques[4] or choix_boutiques == liste_boutiques[5]:
        madame_guipure()
    elif choix_boutiques == liste_boutiques[5]:
        ollivander()
boutiques()

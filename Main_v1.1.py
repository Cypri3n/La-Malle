# coding: utf-8

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



#import des modules

from random import randint
from pygame import *




'''
Fonction qui rembourse Harry lors de ses achats des livres.
'''
def fleury_et_bott():
    cout = 0
    prix_livre_un = randint (10,150)
    prix_livre_deux = randint(50,200)
    prix_livre_trois = randint(75,250)
    cout = prix_livre_un + prix_livre_deux + prix_livre_trois
    print(f"Le prix total des livres est de {cout} euros, ( {prix_livre_un} + {prix_livre_deux} + {prix_livre_trois} )")
    money_gave_by_harry = randint(cout,1000)
    print(f"Harry donne {money_gave_by_harry} euros")
    prix_repay = money_gave_by_harry - cout
    print(f"Je dois te rembourser {prix_repay} euros")
    



def madame_guipure():
    e
    


def ollivander():
    e
    
    



'''
Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.'
'''
def boutiques():
    liste_boutiques = ['Chez Fleury et Bott', 'Chez Madame Guipure', 'Chez Ollivander']
    liste_boutiques = ['Chez Fleury et Bott', 'Chez Madame Guipure', 'Chez Ollivander']
    choix_boutiques = input("Dans quelle boutique souhaitez vous aller? ")
    if choix_boutiques == liste_boutiques[0]:
        fleury_et_bott()
    elif choix_boutiques == liste_boutiques[1]:
        madame_guipure()
    else:
        ollivander()

boutiques()
        
    

        
 
            
            

            
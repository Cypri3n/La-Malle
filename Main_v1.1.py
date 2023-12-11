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
    cout = 0
    prix_livre_un = randint (10,150)
    prix_livre_deux = randint(50,200)
    prix_livre_trois = randint(75,250)
    cout = prix_livre_un + prix_livre_deux + prix_livre_trois
    print(f"Le prix total des livres est de {cout} euros, ( {prix_livre_un} + {prix_livre_deux} + {prix_livre_trois} )")
    money_given_by_harry = randint(cout,1000)
    print(f"Harry donne {money_given_by_harry} euros")
    prix_repay = money_given_by_harry - cout
    print(f"Je dois vous rembourser {prix_repay} euros")

    liste_billets = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    # liste des pièces à rendre
    lst_pieces = []
    # indice de la première pièce comparer à la somme à rendre
    i = len(systeme_monnaie) - 1
    # somme à rendre
    somme_a_rendre = 87
    # boucle de construction de la liste des pièces
    while somme_a_rendre > 0:
        valeur = systeme_monnaie[i]
        if somme_a_rendre < valeur:
            i -= 1
        else:
            lst_pieces.append(valeur)
            somme_a_rendre -= valeur





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
    a = 0





'''
Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.'
'''

#Pas optimal mes gatés vu que la phrase est trop précise, mieux vaut avoir des valeurs pour chaque boutique et en plus ca marche pas 
def boutiques():
    liste_boutiques = ['Chez Fleury et Bott', 'chez fleury et bott', 'Chez Madame Guipure', 'chez madame guipure', 'Chez Ollivander']
    print(liste_boutiques[2])
    choix_boutiques = input("Dans quelle boutique souhaitez vous aller? ")

    assert choix_boutiques in liste_boutiques, "Veuillez saisir une boutiques existante"

    if choix_boutiques == liste_boutiques[0] or choix_boutiques == liste_boutiques[1]:
        fleury_et_bott()
    elif choix_boutiques == liste_boutiques[2] or choix_boutiques == liste_boutiques[3]:
        madame_guipure()
    else:
        ollivander()

boutiques()

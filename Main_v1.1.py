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






                
            




def ollivander():
    noises = randint(0, 1000)
    mornilles = randint(0,700)
    gallions = randint(0, 15)
    monnaie_Akhy = 5*17*29
    print(f'La baguette de sureau t'as choisi Akhy, c'est génial, d'atant plus que tu me dois {gallions} gallions, {mornilles} mornilles ainsi que {noises} petites noises')
    a_rendre = monnaie_Akhy - gallions




#   PARTIE 2 : Interface homme machine 


#Pas optimal mes gatés vu que la phrase est trop précise, mieux vaut avoir des valeurs pour chaque boutique et en plus ca marche pas 
def boutiques():
    '''
    Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.'
    Entrées : Le nom de la boutique sous forme de chaine de caractères
              
    Sorties : Redirige le joueur vers une autre fonction
              Renvoie le résultat lié a cette dernière (documentés separemment)  
    '''
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

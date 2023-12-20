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

#coding: utf-8
#import des modules

from random import randint




def fleury_et_bott(a_rendre_fleury_et_bott):
    '''
    Fonction permettant de rendre la monnaie à Harry avec le moins de billets
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
    
    print(f"Bonjour Harry, je vais dès à présent vous rendre {a_rendre_fleury_et_bott} euros.")
    
    
    for billet in dico_billets:
        if a_rendre_fleury_et_bott >= billet:
            nb_billets = a_rendre_fleury_et_bott // billet
            dico_billets[billet] = nb_billets
            a_rendre_fleury_et_bott -= nb_billets * billet
    for j in dico_billets:
        if dico_billets[j] >= 1:
            print(f"Je vous dois {dico_billets[j]} billet(s) de {dico_billets[...]}")
    return dico_billets




def madame_guipure(a_rendre_madame_guipure):
    '''
    Fonction permettant de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est finie.

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
    
    
    return rendu_monnaie_2            



def ollivander(a_rendre_gallions, a_rendre_mornilles, a_rendre_noises):
    '''
    Fonction permettant de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est finie et de convetir des monnaies de differentes devises.

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
    
    
    dico_billets = {493 : 0, 29 : 0, 1 : 0}
    dico_billets[493] = a_rendre_gallions
    dico_billets[29] = a_rendre_mornilles
    dico_billets[1] = a_rendre_noises
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
    
    liste_boutiques = ['Chez Fleury et Bott', 'chez fleury et bott', 'Chez Madame Guipure', 'chez madame guipure', 'Chez Ollivander']
    print(liste_boutiques[2])
    choix_boutiques = input("Dans quelle boutique souhaitez vous aller? ")

    assert choix_boutiques in liste_boutiques, "Veuillez saisir une boutiques existante"

    if choix_boutiques == liste_boutiques[0] or choix_boutiques == liste_boutiques[1]:
        a_rendre_fleury_et_bott = int(input("Bonjour et bienvenu chez Fleury et Bott, quelle somme dois-je vous rendre ? "))
        fleury_et_bott(a_rendre_fleury_et_bott)
    elif choix_boutiques == liste_boutiques[2] or choix_boutiques == liste_boutiques[3]:
        a_rendre_madame_guipure = int(input("Bonjour et bienvenu chez Madame Guipure, quelle somme dois-je vous rendre ? "))
        madame_guipure(a_rendre_madame_guipure)
    else:
        a_rendre_galions = int(input("Bonjour et bienvenu chez Ollivander, combien de Galions dois-je te rendre ? "))
        a_rendre_mornilles = int(input("Maintenant, combien de Mornilles te dois-je ? "))
        a_rendre_noises = int(input("Finallement, combien de petite Noises te faut-il ? "))
        ollivander(a_rendre_galions, a_rendre_mornilles, a_rendre_noises)

boutiques()


    
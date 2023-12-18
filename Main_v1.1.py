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




def fleury_et_bott(a_rendre):
    '''
    Fonction permettant de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est infini.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus
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
    
    print(f"Bonjour Harry, je vous dois {a_rendre} euros.")
    
    
    for billet in dico_billets:
        if a_rendre >= billet:
            nb_billets = a_rendre // billet
            dico_billets[billet] = nb_billets
            a_rendre -= nb_billets * billet
            
    return dico_billets




def madame_guipure(a_rendre):
    caisse = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    rendu_monnaie_1 = {}

    print(f"Bonjour Harry, je vous dois {a_rendre} euros.")

    for coupure in caisse:
        if coupure <= a_rendre and caisse[coupure] > 0:
            nb_coupures = min(a_rendre // coupure, caisse[coupure])
            rendu_monnaie_1[coupure] = nb_coupures
            a_rendre -= nb_coupures * coupure
            caisse[coupure] -= nb_coupures
            
    if a_rendre > 0:
        print("Je ne peux pas vous remboursez totalement, mais je vous verse le contenu de ma caisse.")
        rendu_monnaie_2 = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    else:
        print("Je peux donc vous rendre la monnaie.")
        rendu_monnaie_2 = rendu_monnaie_1
    
    
    return rendu_monnaie_2            




def ollivander():
    noises = 451
    mornilles = 531
    gallions = 7
    # convertions
    prix = (mornilles * 29) + (gallions * 17 * 29) + noises
    monnaie_Akhy = 5 * 17 * 29
    print(f"La baguette de sureau t'as choisi Akhy, c'est génial, d'atant plus que tu me dois {gallions} gallions,
        {mornilles} mornilles ainsi que {noises} petites noises, ce qui fait {prix} noises très exactement')
    a_rendre = monnaie_Akhy - prix




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

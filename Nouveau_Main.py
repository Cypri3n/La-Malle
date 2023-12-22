# coding utf-8:
'''
HARRY POTTER SE FAIT LA MALLE...
Harry Potter découvre le Chemin de Traverse et part à la conquête des nombreuses boutiques magiques 
caractéristiques du Chemin de Traverse. Pendant son périple, Harry pourra entrer dans les trois boutiques suivantes :

Chez Fleury et Botts
Chez Madame Guipure
Chez Ollivander
Vos achats se feront depuis la console, et le programme déterminera la somme à rendre.

AUTEURS:
Eliot CAIMARI LAUNAY, Arthur CHARUEL, Cyprien VENARD

LICENCE:
Aucune
VERSION:
3.1
DATE DE DERNIERE REVISION:
22/12/2023
ADRESSE GITHUB: 
https://github.com/Cypri3n/La-Malle
'''


def rendre_monnaie_fleury_et_bott(a_rendre_fleury_et_bott):
    '''
    Permet de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est infinie.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus

    DOCTEST:
    >>> rendre_monnaie_fleury_et_bott(0)
        
    >>> rendre_monnaie_fleury_et_bott(60)
  
    >>> rendre_monnaie_fleury_et_bott(63)
 
    >>> rendre_monnaie_fleury_et_bott(231)
     
    >>> rendre_monnaie_fleury_et_bott(899)
    
    '''
    
    dico_billets = {500: 0,
                    200: 0,
                    100: 0,
                    50: 0,
                    20: 0,
                    10: 0,
                    5: 0,
                    2: 0,
                    1: 0}
    
    if a_rendre_fleury_et_bott <= 0:
        print("Je suis navré, mais je ne peux pas vous rembourser une somme inexistante.")
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


def rendre_monnaie_madame_guipure(a_rendre_madame_guipure):
    '''
    Permet de rendre la monnaie à Harry avec le moins de billets
    possibles en sachant que la caisse du libraire est limitée.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus
    
    DOCTEST:
    >>> rendre_monnaie_madame_guipure(0)
    Bonjour Harry, je vous dois 0 euros.
    >>> rendre_monnaie_madame_guipure(17)
    Je vous rends 1 billet(s) de 10
    Je vous rends 1 billet(s) de 5
    Je vous rends 1 billet(s) de 2
    >>> rendre_monnaie_madame_guipure(68)
    Je ne peux pas vous rembourser totalement, mais je peux vous verser le contenu de ma caisse.
    Je vous rends 1 billet(s) de 50
    Je vous rends 1 billet(s) de 10
    Je vous rends 1 billet(s) de 5
    Je vous rends 1 billet(s) de 2
    >>> rendre_monnaie_madame_guipure(231)
    Je ne peux pas vous rembourser totalement, mais je peux vous verser le contenu de ma caisse.
    Je vous rends 1 billet(s) de 200
    Je vous rends 1 billet(s) de 20
    Je vous rends 1 billet(s) de 10
    >>> rendre_monnaie_madame_guipure(497)
    Je vous rends 1 billet(s) de 200
    Je vous rends 2 billet(s) de 100
    Je vous rends 1 billet(s) de 50
    Je vous rends 1 billet(s) de 20
    Je vous rends 1 billet(s) de 10
    Je vous rends 1 billet(s) de 5
    Je vous rends 5 billet(s) de 2
    >>> rendre_monnaie_madame_guipure(842)
    Je vous rends 1 billet(s) de 200
    Je vous rends 3 billet(s) de 100
    Je vous rends 1 billet(s) de 50
    Je vous rends 1 billet(s) de 20
    Je vous rends 1 billet(s) de 10
    Je vous rends 1 billet(s) de 5
    Je vous rends 5 billet(s) de 2
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
        print("\nJe ne peux pas vous rembourser totalement, mais je peux vous verser le contenu de ma caisse.")
        rendu_monnaie_2 = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    else:
        print("\nJe ne vous dois donc pas d'argent.")
        rendu_monnaie_2 = rendu_monnaie_1
    
    for j in rendu_monnaie_1:
        print(f"Je vous rends {rendu_monnaie_1[j]} billet(s) de {j}\n")

    return rendu_monnaie_2            


def rendre_monnaie_ollivander(a_rendre_gallions, a_rendre_mornilles, a_rendre_noises):
    '''
    Permet de rendre la monnaie à Harry avec le moins de pièces
    possibles en sachant que la caisse du libraire est infinie et qu'il faut convertir les monnaies en plusieurs devises.

    Entrée : entier correspondant à la somme à rendre par le libraire.
    
    Sortie : dictionnaire correspondant au nombre de billets rendus
 
    '''
    dico_billets = {493: 0, 29: 0, 1: 0}
    
    dico_billets[493] = a_rendre_gallions
    dico_billets[29] = a_rendre_mornilles
    dico_billets[1] = a_rendre_noises
    
    print(f"Je te dois {dico_billets[493]} Gallions, {dico_billets[29]} Mornilles, et {dico_billets[1]} Noises.")
    
    if a_rendre_gallions <= 0 and a_rendre_mornilles <= 0 and a_rendre_noises <= 0:
        print("Je ne peux pas te rembourser si je ne te dois rien !\n")
        
    else:
        for i in dico_billets:
            while dico_billets[1] >= 29:
                dico_billets[29] += 1 
                dico_billets[1] -= 29
            while dico_billets[29] >= 17:
                dico_billets[493] += 1
                dico_billets[29] -= 17            
        print(f"Je te rends {dico_billets[493]} Gallions, {dico_billets[29]} Mornilles, et {dico_billets[1]} Noises !\n")
        return dico_billets


def boutiques():
    '''
    Fonction qui demande à l'utilisateur quelle boutique il souhaite visiter, puis affiche les fonctions de ces boutiques.
    
    Entrées : Le nom de la boutique sous forme de chaîne de caractères
              
    Sorties : Redirige le joueur vers une autre fonction
              Renvoie le résultat lié à cette dernière (documentés séparément)  
    '''
    liste_valeurs_fleury_et_bott = [0, 60, 63, 231, 899]
    liste_valeurs_madame_guipure = [0, 17, 68, 231, 497, 842]
    liste_valeurs_ollivander = [(0, 0, 0), (0, 0, 654), (2, 11, 9), (7, 531, 451)]
    
    choix_chemin_traverse = int(input("Vous êtes sur le chemin de traverse, souhaitez-vous y rester ? Saisissez 1 pour oui et 2 pour non : "))
    if choix_chemin_traverse == 1:
        print("Dans quelle boutique souhaitez-vous aller ?")
        choix_boutiques = int(input("Saisissez 1 pour aller chez Fleury et Bott, 2 pour aller chez Madame Guipure, et 3 pour aller chez Ollivander : "))

        assert choix_boutiques in [1, 2, 3], "Veuillez entrer 1, 2 ou 3 pour effectuer une action."

        if choix_boutiques == 1:
            choix_somme_rendre = int(input("Souhaitez-vous essayer les sommes à rendre du magasin en tapant 1, ou essayer vos propres sommes en tapant 2 : "))
            if choix_somme_rendre == 1:
                for valeur in liste_valeurs_fleury_et_bott:
                    rendre_monnaie_fleury_et_bott(valeur)
            else:
                choix_somme_a_rendre = int(input("Quelle somme souhaitez-vous tester ? "))
                rendre_monnaie_fleury_et_bott(choix_somme_a_rendre)
            choix_rester = int(input("Veuillez entrer 1 pour rester ou 2 pour retourner au chemin de traverse : "))
            while choix_rester == 1:
                choix_somme_rendre = int(input("Souhaitez-vous essayer les sommes à rendre du magasin en tapant 1, ou essayer vos propres sommes en tapant 2 : "))
                if choix_somme_rendre == 1:
                    for valeur in liste_valeurs_fleury_et_bott:
                        rendre_monnaie_fleury_et_bott(valeur)
                    print("Souhaitez-vous maintenant rester dans notre boutique ou retourner au chemin de traverse ?")
                    choix_rester = int(input("Saisissez 1 pour rester ou 2 pour retourner au chemin de traverse : "))
                else:
                    choix_somme_a_rendre = int(input("Quelle somme souhaitez-vous tester ? "))
                    rendre_monnaie_fleury_et_bott(choix_somme_a_rendre)
                    print("Souhaitez-vous maintenant rester dans notre boutique ou retourner au chemin de traverse ?")
                    choix_rester = int(input("Saisissez 1 pour rester ou 2 pour retourner au chemin de traverse : "))
            else:
                boutiques()

        elif choix_boutiques == 2:
            choix_somme_rendre = int(input("Souhaitez-vous essayer les sommes à rendre du magasin en tapant 1, ou essayer vos propres sommes en tapant 2 : "))
            if choix_somme_rendre == 1:
                for valeur in liste_valeurs_madame_guipure:
                    rendre_monnaie_madame_guipure(valeur)
            else:
                choix_somme_a_rendre = int(input("Quelle somme souhaitez-vous tester ? "))
                rendre_monnaie_madame_guipure(choix_somme_a_rendre)
            choix_rester = int(input("Veuillez entrer 1 pour rester ou 2 pour retourner au chemin de traverse : "))
            while choix_rester == 1:
                choix_somme_rendre = int(input("Souhaitez-vous essayer les sommes à rendre du magasin en tapant 1, ou essayer vos propres sommes en tapant 2 : "))
                if choix_somme_rendre == 1:
                    for valeur in liste_valeurs_madame_guipure:
                        rendre_monnaie_madame_guipure(valeur)
                    print("Souhaitez-vous maintenant rester dans notre boutique ou retourner au chemin de traverse ?")
                    choix_rester = int(input("Saisissez 1 pour rester ou 2 pour retourner au chemin de traverse : "))
                else:
                    choix_somme_a_rendre = int(input("Quelle somme souhaitez-vous tester ? "))
                    rendre_monnaie_m


    

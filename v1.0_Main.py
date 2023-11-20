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
0.1


DATE DE DERNIERE REVISION:
20/11/2023


ADRESSE GITHUB: 
https://github.com/Cypri3n/La-Malle

'''



#import des modules

from random import randint

'''
fonction qui affiche le prix total et aléatoire des trois livres.
'''
cout = 0
def prix_total(cout):
    prix_livre_un = randint (10,150)
    prix_livre_deux = randint(50,200)
    prix_livre_trois = randint(75,250)
    cout = prix_livre_un + prix_livre_deux + prix_livre_trois
    print(f"Le prix total des livres est de {cout} euros, ( {prix_livre_un} + {prix_livre_deux} + {prix_livre_trois} )")
prix_total(cout)

'''
Fonction qui rembourse le petit Harry pour pas qu'il devienne pauvre.
'''
liste_billets = [1, 2, 5, 10, 20, 50, 100, 200, 500]
liste_billets.reverse()
print(liste_billets)
def atm(rembourse):
    for i in range(liste_billets):
        
        
 
            
            

            

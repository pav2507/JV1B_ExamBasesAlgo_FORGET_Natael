#partie 1
#exercice 2
import random

liste=[18,29,52,41,37]
plusGrand = liste[0]

for a in range (0,len(liste)):
    plusGrand=liste[a]
    for b in range(0+a, len(liste)):
        if(liste[b]<plusGrand):
            plusGrand = liste[a]
            liste[a] = liste[b]
            liste[b] = plusGrand

print(plusGrand)
print(liste)
#le tri a bulle est lent car il va controler les case une par une, il est difficile de ce faire une idée puisqu'elle est de l'ordre des milliseconde
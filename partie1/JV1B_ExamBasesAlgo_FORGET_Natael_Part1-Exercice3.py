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
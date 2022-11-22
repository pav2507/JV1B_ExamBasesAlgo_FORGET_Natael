#partie 1
#exercice 2
import random

liste=[1,2,5,4,3]
plusGrand=0

for a in range (0,len(liste)):
    for b in range(a, len(liste)):
        if(plusGrand<liste[a]):
            plusGrand = liste[a]
            
    stockage=liste[b]
    liste[4]=stock
    liste[2]=stockage

print(plusGrand)
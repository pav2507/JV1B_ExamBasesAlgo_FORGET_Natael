#partie 1
#exercice 2
import random

liste=[1,2,5,4,3]
plusGrand = liste[0]

for n in range(0,len(liste)):
    a=liste[n]
    for i in range(0+n,len(liste)):
        if liste[i]<a:
            a=liste[n]
            liste[n]=liste[i]
            liste[i]=a
        
print(liste)
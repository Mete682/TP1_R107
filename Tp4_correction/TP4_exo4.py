# élément le plus fréquent dans une liste

#remplissage aléatoire d'une liste
from random import randint

liste = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

"""for i in range(100):
    liste.append(randint(0,20))
"""
max=0
nmax=0

for j in range(len(liste)):
    n=0
    for i in range(len(liste)):
        if (liste[j]==liste[i]):
            n+=1
    if n>nmax:
        nmax = n
        max = j

print(f"L'élément le plus présent est {liste[max]} qui apparait {nmax} fois")

# seconde méthode
max = 0
nmax = liste.count(liste[0])
for j in range(1,len(liste)):
    n = liste.count(liste[j]) # remplace la boucle de parcours de la liste.
    if n> nmax:
        max = j
        nmax = n

print(f"L'élément le plus présent est {liste[max]} qui apparait {nmax} fois")

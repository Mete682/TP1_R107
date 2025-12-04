chaine = input("Entrez une phrase : ")

longueur = 0
for c in chaine:
    longueur = longueur + 1
print("Taille de la chaîne :", longueur)

nb_voyelles = 0
for c in chaine:
    if c in "aeiouyAEIOUY":
        nb_voyelles = nb_voyelles + 1

pourcentage = (nb_voyelles / longueur) * 100
print("Pourcentage de voyelles :", pourcentage, "%")

mot = "wagon"
nb_wagon = 0
premier_indice = -1
taille_mot = 5

for i in range(longueur - taille_mot + 1):
    sous_chaine = ""
    for j in range(taille_mot):
        sous_chaine = sous_chaine + chaine[i + j]

    if sous_chaine == mot:
        nb_wagon = nb_wagon + 1
        if premier_indice == -1:
            premier_indice = i

if premier_indice != -1:
    print("Le mot wagon commence à l'indice :", premier_indice)
else:
    print("Le mot wagon n'est pas présent.")

print("Nombre d'occurrences de wagon :", nb_wagon)
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

nombre_frequent = L1[0]
max_apparitions = 0

for nombre in L1:
    compteur = L1.count(nombre)

    if compteur > max_apparitions:
        max_apparitions = compteur
        nombre_frequent = nombre

print("Le nombre le plus frequent dans la liste est le :", nombre_frequent, "(" + str(max_apparitions) + " x)")
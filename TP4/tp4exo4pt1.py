L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

nombre_frequent = L1[0]
max_apparitions = 0

for i in range(len(L1)):
    nombre_actuel = L1[i]
    compteur = 0

    for j in range(len(L1)):
        if L1[j] == nombre_actuel:
            compteur = compteur + 1

    if compteur > max_apparitions:
        max_apparitions = compteur
        nombre_frequent = nombre_actuel

print("Le nombre le plus frequent dans la liste est le :", nombre_frequent, "(" + str(max_apparitions) + " x)")
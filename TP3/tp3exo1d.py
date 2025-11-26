x = int(input("entrez la valeur de x (supérieur a 1)"))

somme = 0
N =0
while somme + N <= x:
    somme += N
    N = N + 1

N = N - 1
print("le plus grand nombre est : ", N)
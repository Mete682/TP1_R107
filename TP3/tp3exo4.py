n = int(input("donnez la valeur de n : "))
choix = input("quel est votre choix (for/while) :")
resultat = 1

if choix == 'for':

    for i in range(1, n+1):
        resultat = resultat * i
        print(resultat)
    print("vous avez utilisé la boucle for")

else:
    i=1
    while i <= n:
        resultat = resultat * i
        i = i +1
        print(resultat)
    print("vous avez utilisé la boucle while")


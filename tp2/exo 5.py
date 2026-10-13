nb=int(input("Entrez un nombre entier:"))

if nb < 0 :
    signe=('négatif')
else :
    signe=('positif')


if nb == 0:
    print("Le nombre est zéro (et il est pair)")
elif nb % 2 == 0 :
    print("Le nombre est ",signe,"et pair")
else :
    print("Le nombre est",signe,"et impair")
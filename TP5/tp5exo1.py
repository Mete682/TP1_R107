nom1 = input("Entrez le premier nom : ")
prenom1 = input("Entrez le premier prénom : ")
nom2 = input("Entrez le deuxième nom : ")
prenom2 = input("Entrez le deuxième prénom : ")

chaine1 = prenom1.capitalize() + " " + nom1.upper()
chaine2 = prenom2.capitalize() + " " + nom2.upper()

if nom1.upper() < nom2.upper():
    print(chaine1)
    print(chaine2)
elif nom2.upper() < nom1.upper():
    print(chaine2)
    print(chaine1)
else:
    if prenom1.capitalize() < prenom2.capitalize():
        print(chaine1)
        print(chaine2)
    else:
        print(chaine2)
        print(chaine1)
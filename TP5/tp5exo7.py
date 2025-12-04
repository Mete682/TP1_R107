import os.path
import datetime

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    taille1 = os.path.getsize(fichier1)
    taille2 = os.path.getsize(fichier2)
    print("Taille fichier 1 :", taille1, "octets")
    print("Taille fichier 2 :", taille2, "octets")

    ts1 = os.path.getmtime(fichier1)
    ts2 = os.path.getmtime(fichier2)

    date1 = datetime.datetime.fromtimestamp(ts1)
    date2 = datetime.datetime.fromtimestamp(ts2)

    print("Date modif fichier 1 :", date1)
    print("Date modif fichier 2 :", date2)

    if ts1 > ts2:
        print("Le fichier le plus récent est :", fichier1)
    elif ts2 > ts1:
        print("Le fichier le plus récent est :", fichier2)
    else:
        print("Les fichiers ont été modifiés au même moment")

else:
    print("Un des fichiers n'existe pas.")
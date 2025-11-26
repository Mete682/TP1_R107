hd = int(input("Donnez l'heure de début : "))
hf = int(input("Donnez l'heure de fin : "))

if hd < 0 or hd > 24 or hf < 0 or hf > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif hd == hf:
    print("Attention ! l'heure de fin est identique à l'heure de début.")
elif hd > hf:
    print("Attention ! le début de la location est après la fin ...")
else:
    ht1 = 0
    ht2 = 0

    for heure in range(hd, hf):
        if heure < 7 or heure >= 17:
            ht1 += 1
        else:
            ht2 += 1

    cout_total = ht1 * 1 + ht2 * 2

    print("Vous avez loué votre vélo pendant")
    if ht2 > 0:
        print(ht2, "heure au tarif horaire de 2 euro")
    if ht1 > 0:
        print(ht1, "heure au tarif horaire de 1 euro")
    print("Le montant total est", cout_total, "euro.")
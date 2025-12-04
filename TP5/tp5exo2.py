somme_notes = 0
somme_coeffs = 0
est_admis = True

for i in range(5):
    print("Veuillez entrer la note du module", i + 1, "et le coefficient correspondant :")
    saisie = input()
    morceaux = saisie.split(" ")
    note = float(morceaux[0])
    coeff = int(morceaux[1])

    if note < 8:
        est_admis = False

    somme_notes = somme_notes + (note * coeff)
    somme_coeffs = somme_coeffs + coeff

moyenne = somme_notes / somme_coeffs
print("Moyenne générale :", moyenne)

if moyenne > 10 and est_admis:
    print("L'étudiant est admis")
else:
    print("L'étudiant n'est pas admis")
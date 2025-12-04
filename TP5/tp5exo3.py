chaine = input("Entrez un mot ou une phrase : ")
chaine_epuree = ""

for caractere in chaine:
    if caractere.isalpha():
        chaine_epuree = chaine_epuree + caractere.lower()

chaine_inverse = ""
for caractere in chaine_epuree:
    chaine_inverse = caractere + chaine_inverse

if chaine_epuree == chaine_inverse:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
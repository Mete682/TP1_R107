a = 0
b = 0
c = 0

for i in range(10):
    n = int(input("entrez la valeur entre 0 et 20 :"))

    while n < 0 or n > 20:
        n = int(input("entrez une autre valeur entre 0 et 20 :"))

    if n < 10 :
        a = a + 1
    if n >= 10 and n < 15:
        b = b + 1
    if n >= 15 :
        c = c + 1

print("valeur en dessous de 10 :", a)
print("valeur supérieur ou égale à 10 et inférieur strictement à 15 :", b)
print("valeur supérieur ou égal a 15 :", c)
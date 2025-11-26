from random import randint

r = randint(1,100)
n = r + 1
s=0

while n != r:
    n = int(input("entrez la valeur de n"))

    if n < r:
        print("c'est plus ")

    if n > r:
        print("c'est moins")
    s=s+1

print("vous avez gagnez")
print("vous avez réussi en", s,"essai(s)")
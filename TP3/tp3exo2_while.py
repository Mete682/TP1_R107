from time import sleep

n = int(input("quel est la valeur de n : "))

while n > 0:
    sleep(1)
    n = n - 1
    print(n)


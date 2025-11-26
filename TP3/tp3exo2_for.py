from time import sleep
n = int(input("donnez la valeur de n"))

for i in range(n):
    sleep(1)
    n = n - 1
    print(n)
from time import sleep

from win32trace import flush

n = int(input("donnez la valeur de n"))

for i in range(n):
    sleep(1)
    n = n - 1
    print(n, flush= True)
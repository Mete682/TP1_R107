x=int(input("Entrez : x"))
y=int(input("Entrez : y"))
print("avant permutation")
print("x =",x,"\ny =",y)


print("apres permutation")
z = x + y
x = z - x
y = z - y

print("x =",x ,"\ny =",y)
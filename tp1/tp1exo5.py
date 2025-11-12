jour = int(input("Entrez le jour du mois (1-31) : "))
heure = int(input("Entrez l'heure (0-23) : "))
minute = int(input("Entrez les minutes (0-59) : "))
minutes_ecoule = (jour - 1) * 24 * 60 + heure * 60 + minute
minutes_ecoule = (jour - 1) * 24 * 60 + heure * 60 + minute
print(minutes_ecoule)
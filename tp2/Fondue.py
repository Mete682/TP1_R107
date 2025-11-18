BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

print("pour faire une fondue fribourgeoise pour",nbConvives,"personnes, il vous faut :\n","-",fromage,"gr de fromage\n","-",eau,"dl d'eau\n","-",ail,"gousses(s) d'ail\n","-",pain,"gr de pain")
import math
#Partie 8
# Y= 2X -2
def caracteristique_droite(m,b):
    pente = m
    ordonner_origine = b
    #abscisse y=0 => x = b/m
    abscisse_origine = b/m if m!=0 else None
    return pente,ordonner_origine,abscisse_origine
m = 2
b = -2
pente,ordonner_origine,abscisse_origine=caracteristique_droite(m,b)
print(pente)
print(ordonner_origine)
print(abscisse_origine)
#partie 9
# m = y2-y1/x2-x1 A(2, 2) B(6, 10)
def caracteristi_pente_distance(p1,p2):
    x1,x2 =p1
    y1,y2 =p2
    #calcul de la pente 
    pente = y2-y1/x2-x1 if x2-x1!= 0 else None
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return pente,distance
#les points donner
point1 = (2, 2)
point2 = (6, 10)
pente_point,distance_point =caracteristi_pente_distance(point1,point2)
print(pente_point)
print(distance_point)
#comparaison des deux 
if caracteristique_droite == caracteristi_pente_distance:
    print("les 2 sont egals ")
else:
    print("les deux sont differents ")    



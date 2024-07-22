#Vérifiez si la saison est Automne, Hiver, Printemps ou Été.
# Si l'utilisateur saisit : Septembre, Octobre ou Novembre, la saison est Automne.
# Décembre, Janvier ou Février, la saison est Hiver. Mars, Avril ou Mai, la saison est Printemps. 
# Juin, Juillet ou Août, la saison est Été.
from cmath import sqrt
def determiner_saison(month):
    month = month.lower()
    if month in ['septembre', 'octobre', 'novembre']:
        return 'Automne'
    elif month in ['décembre', 'janvier', 'février']:
        return 'Hiver'
    elif month in ['mars', 'avril', 'mai']:
        return 'Printemps'
    elif month in ['juin', 'juillet', 'août']:
        return 'Été'
    else:
        return 'Mois invalide. Veuillez saisir un mois valide.'
mois = input("Veillez saisir le mois que vous souhaiter ")
saison= determiner_saison(mois)
print(f"la saison correspondante a {mois} est {saison}")
#6Écrivez une fonction appelée calculate_slope qui renvoie la pente d'une équation linéaire.
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("La valeur de x1 et celle de x2 doivent être différentes pour éviter la division par zéro.")
    return (y2 - y1) / (x2 - x1)

try:
    print(calculate_slope(0, 7, 3, 8))  
except ValueError as e:
    print(e)

try:
    print(calculate_slope(1, 3, 1, 9))  
except ValueError as e:
    print(e)
#Une équation quadratique se calcule comme suit : ax² + bx + c = 0. 
# Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    delta = b**2 -4*a*c
    #calcul des solutions 
    solt1 = (-b -sqrt(delta))/2*a
    solt2 = (-b +sqrt(delta))/2*a
    return solt1,solt2
print(solve_quadratic_eqn(2,8,9))
    
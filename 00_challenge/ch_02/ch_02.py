"""
 1-  Déclarez votre âge comme une variable entière. 
"""
age = 23

""" 
2-  Déclarez votre taille comme une variable flottante.
"""
taille = 1.65

""" 
3-  Déclarez une variable qui stocke un nombre complexe.
"""
nb_complexe = 3 +2j


""" 
4-  Écrivez un script qui demande à l'utilisateur d'entrer la base et la hauteur du triangle et de calculer l'aire de ce triangle (aire = 0,5 xbxh).
"""

base = int(input("Entrer base: "))
hauteur = int(input("Entrer Height: "))
aire = 0.5 * base * hauteur
print("The area of triangle is ", aire)


""" 
5-  Écrivez un script qui demande à l'utilisateur d'entrer les côtés a, b et c du triangle. Calculez le périmètre du triangle (périmètre = a + b + c).
"""

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
perimetre  = a+b+c
print("The perimeter of the triangle is ", perimetre)




""" 
6-  Obtenez la longueur et la largeur d'un rectangle en utilisant une invitation. Calculez son aire (aire = longueur x largeur) et son périmètre (périmètre = 2 x (longueur + largeur)).
"""

longeur = float(input("entrer la longeur du rectangle: "))
largeur = float(input("entrer la largeur du rectangle: "))
rect_perimetre = 2*(longeur + largeur)
rect_aire = longeur*largeur

print("Perimetre du rectangle est : ",rect_perimetre)
print("L'aire du rectangle est : ",rect_aire)


import math   #importation du module math pour acceder à PI sqrt ...

# 7. Obtenez le rayon d'un cercle en utilisant une invitation.
rayon = float(input("Entrez le rayon du cercle : "))

# Calculez l'aire (aire = pi * r * r) et la circonférence (c = 2 * pi * r) où pi = 3,14.
pi = 3.14
aire = pi * rayon * rayon
circonference = 2 * pi * rayon

print("L'aire du cercle est:", aire)
print("La circonférence du cercle est:", circonference)

# 8. Calculez la pente, l'ordonnée à l'origine et l'abscisse à l'origine de y = 2x -2.
# La pente est le coefficient de x (m = 2), l'ordonnée à l'origine est -2, et l'abscisse à l'origine est x lorsque y = 0
# 0 = 2x - 2 => x = 1
pente1 = 2
ordonnée_origine = -2
abscisse_origine = 1

print("La pente est:", pente1)
print("L'ordonnée à l'origine est:", ordonnée_origine)
print("L'abscisse à l'origine est:", abscisse_origine)

# 9. Trouvez la pente et la distance euclidienne entre le point (2, 2) et le point (6, 10).
x1, y1 = 2, 2
x2, y2 = 6, 10

pente2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("La pente entre les points (2, 2) et (6, 10) est:", pente2)
print("La distance euclidienne entre les points (2, 2) et (6, 10) est:", distance)

# 10. Comparez les pentes des tâches 8 et 9.
print("pente1 inferieur" if (pente1<pente2) else "pente 2 est inferieur")

# 11. Calculez la valeur de y (y = x^2 + 6x + 9). Essayez d'utiliser différentes valeurs de x et découvrez quelle valeur de x pour laquelle y sera égale à 0.
def calculer_y(x):
    return x ** 2 + 6 * x + 9

# Utilisation de y
valeurs_x = [-3, -2, -1, 0, 1, 2, 3]
for x in valeurs_x:
    y = calculer_y(x)
    print(f"Pour x = {x}, y = {y}")

# La valeur de x pour laquelle y est égal à 0 est x = -3.

# 12. Trouvez la longueur de 'python' et 'dragon' et faites une fausse déclaration de comparaison.
len_python = len("python")
len_dragon = len("dragon")
print("La longueur de 'python' est égale à 'dragon' :", len_python < len_dragon)

# 13. Utilisez l'opérateur et vérifiez si 'on' se trouve à la fois dans 'python' et 'dragon'.
print("'on' se trouve à la fois dans 'python' et 'dragon' :", 'on' in 'python' and 'on' in 'dragon')

# 14. 'J'espère que ce cours n'est pas plein de jargon' . Utilisez l'opérateur pour vérifier si le jargon est dans la phrase.
phrase = "J'espère que ce cours n'est pas plein de jargon."
print("Le mot 'jargon' est dans la phrase :", 'jargon' in phrase)

# 15. Il n'y a pas de 'on' dans 'dragon' et 'python'.
print("Il n'y a pas de 'on' dans 'dragon' et 'python' :", 'on' not in 'dragon' and 'on' not in 'python')

# 16. Trouvez la longueur du texte Python et convertissez la valeur en flottant puis en chaîne de caractères.
len_python = len("Python")
len_python_float = float(len_python)
len_python_str = str(len_python_float)
print("Longueur de 'Python' en flottant puis en chaîne de caractères :", len_python_str)

# 17. Les nombres pairs sont divisibles par 2 et le reste est zéro. Comment vérifier si un nombre est pair ou non en utilisant Python ?
nombre = 4
est_pair = nombre % 2 == 0
print(f"Le nombre {nombre} est pair :", est_pair)

# 18. Vérifiez si la division entière de 7 par 3 est égale à la valeur convertie en entier de 2,7.
resultat = 7 // 3 == int(2.7)
print("La division entière de 7 par 3 est égale à la valeur convertie en entier de 2,7 :", resultat)

# 19. Vérifiez si le type de « 10 » est égal au type de 10.
resultat = type("10") == type(10)
print("Le type de '10' est égal au type de 10 :", resultat)

# 20. Vérifiez si int('9.8') est égal à 10.
try:
    resultat = int(float('9.8')) == 10
except ValueError:
    resultat = False
print("int('9.8') est égal à 10 :", resultat)

# 21. Écrivez un script qui demande à l'utilisateur d'entrer les heures et le taux par heure. Calculez le salaire de la personne.
heures = float(input("Entrez les heures : "))
taux_par_heure = float(input("Entrez le taux par heure : "))
salaire = heures * taux_par_heure
print(f"Votre salaire hebdomadaire est de : {salaire}")

# 22. Écrivez un script qui demande à l'utilisateur d'entrer un nombre d'années. Calculez le nombre de secondes pendant lesquelles une personne peut vivre. Supposons qu'une personne puisse vivre cent ans.
annees = int(input("Entrez le nombre d'années que vous avez vécu : "))
secondes_vie = annees * 365 * 24 * 60 * 60
print(f"Vous avez vécu pendant {secondes_vie} secondes.")

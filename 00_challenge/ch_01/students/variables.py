

# =============NIVEAU  1====================================
# 1000 TeachLeaders programmation python


"""
1-  Déclarez une variable first_name et assignez-lui une valeur.
"""
first_name = "Etienne"

"""
2-  Déclarez une variable last_name et assignez-lui une valeur.
"""
last_name = "KAMANO"

"""
3-  Déclarez une variable full_name et assignez-lui une valeur.
"""
full_name = first_name + " " + last_name

"""
4-  Déclarez une variable pays et attribuez-lui une valeur.
"""
pays = "Guinée"

"""
5-  Déclarez une ville variable et attribuez-lui une valeur.
"""
ville = "Conakry"

"""
6-  Déclarez un âge variable et attribuez-lui une valeur.
"""
age = 24

"""
7-  Déclarez une année variable et attribuez-lui une valeur.
"""
année = 2024

"""
8-  Déclarez une variable is_married et assignez-lui une valeur.
"""
is_married = False

"""
9-  Déclarez une variable is_true et assignez-lui une valeur.
"""
is_true = True

"""
10- Déclarez une variable is_light_on et assignez-lui une valeur.
"""
is_light_on = True

"""
11- Déclarez plusieurs variables sur une seule ligne.
"""
var1, var2, var3 = 1, 2, 3



# =============NIVEAU  2====================================

"""
1-  Vérifiez le type de données de toutes vos variables en utilisant la fonction intégrée type().
"""
print("Le type de la variable first_name: " + str(type(first_name)))  
print("Le type de la variable last_name: " + str(type(last_name)))   
print("Le type de la variable full_name: " + str(type(full_name)))   
print("Le type de la variable pays: " + str(type(pays)))        
print("Le type de la variable ville: " + str(type(ville)))       
print("Le type de la variable age: " + str(type(age)))         
print("Le type de la variable année: " + str(type(année)))       
print("Le type de la variable is_married: " + str(type(is_married)))   
print("Le type de la variable is_true: " + str(type(is_true)))      
print("Le type de la variable is_light_on: " + str(type(is_light_on))) 
print("Le type de la variable var1: " + str(type(var1))) 
print("Le type de la variable var2: " + str(type(var2))) 
print("Le type de la variable var3: " + str(type(var3))) 


"""
    2-En utilisant la fonction intégrée len() , trouvez la longueur de votre prénom.
"""
print("la longeur de mon prenom est " , len(first_name))

'''
3-  Comparez la longueur de votre prénom et de votre nom de famille.
'''
print("prenom plus long que lenom" if len(first_name)<len(last_name) else "le nom est plus long que le prenom")



"""
4-Déclarez 5 comme num_one et 4 comme num_two.
"""
num_one = 5
num_two = 4

"""
4-1-    Additionnez num_one et num_two et assignez la valeur à une variable total.
"""
total = num_one + num_two

"""
4-2     Soustrayez num_two de num_one et assignez la valeur à une variable diff.
"""
diff = num_one - num_two

"""
4-3     Multipliez num_two et num_one et attribuez la valeur à une variable produit.
"""
produit = num_one * num_two

"""
4-4     Divisez num_one par num_two et assignez la valeur à une variable division.
"""
division = num_one / num_two

"""
4-5     Utilisez la division par modulo pour trouver num_two divisé par num_one et assignez la valeur à une variable reste.
"""
reste = num_one % num_two

"""
4-6     Calculez num_one à la puissance de num_two et assignez la valeur à une variable exp.
"""
exp = num_one ** num_two

"""
4-7     Trouvez la division entière de num_one par num_two et assignez la valeur à une variable floor_division.
"""
floor_division = num_one // num_two

# Affichez les résultats
print("total:", total)
print("diff:", diff)
print("produit:", produit)
print("division:", division)
print("reste:", reste)
print("exp:", exp)
print("floor_division:", floor_division)




import math

"""
5   Le rayon d'un cercle est de 30 mètres.
"""
rayon = 30

"""
    5-1     Calculez l'aire d'un cercle et attribuez la valeur à une variable nommée area_of_circle.
"""
area_of_circle = math.pi * rayon ** 2

"""
    5-2     Calculez la circonférence d'un cercle et attribuez la valeur à une variable nommée circum_of_circle.
"""
circum_of_circle = 2 * math.pi * rayon

# Affichez les résultats
print("area_of_circle:", area_of_circle)
print("circum_of_circle:", circum_of_circle)

"""
Prenez le rayon comme entrée utilisateur et calculez l'aire.
"""
rayon_utilisateur = float(input("Entrez le rayon du cercle : "))
area_of_circle_user = math.pi * rayon_utilisateur ** 2

# Affichez le résultat
print("L'aire du cercle avec un rayon de", rayon_utilisateur, "mètres est:", area_of_circle_user)





"""
5   Utilisez la fonction d'entrée intégrée pour obtenir le prénom, le nom de famille, le pays et l'âge d'un utilisateur 
et stockez la valeur dans les variables correspondantes.
"""
first_name = input("Entrez votre prénom : ")
last_name = input("Entrez votre nom de famille : ")
pays = input("Entrez votre pays : ")
age = int(input("Entrez votre âge : "))

# Affichez les informations recueillies
print("Prénom:", first_name)
print("Nom de famille:", last_name)
print("Pays:", pays)
print("Âge:", age)

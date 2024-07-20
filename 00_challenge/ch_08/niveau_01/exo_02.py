
"""# 2-  
Comparez les valeurs de my_age et your_age en utilisant if ... else. 
Qui est le plus âgé (moi ou vous) ? Utilisez input("Entrez votre âge : ")
pour obtenir l'âge en entrée. Vous pouvez utiliser une condition imbriquée pour imprimer 'year'
pour une différence d'un an, 'years' pour les différences plus importantes, et un texte personnalisé 
si my_age = your_age. Exemple de sortie :
"""
my_age = 24
while True:
    try:
        your_age = int(input("Entrez votre âge : "))
        break
    except ValueError:
     print("L'age entré est invalide, reprenez correctement: \n")   

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age.")


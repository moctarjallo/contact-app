#Exo2
# Comparez les valeurs de my_age et your_age en utilisant if ... else. Qui est le plus âgé (moi ou vous) ?
 #Utilisez input("Enter your age: ") pour obtenir l'âge en entrée. 
 #Vous pouvez utiliser une condition imbriquée pour imprimer 'year' pour une différence d'un an, 'years' pour des différences plus importantes,
# et un texte personnalisé si my_age = your_age.
# je declare mon Age
my_age = 22
your_age = int(input("Enter your age: "))
if my_age < your_age:
    difference_age = your_age - my_age
    if difference_age == 1:
        print(f"Tu est plus age que moi de {difference_age} year")
    else:
        print(f"Tu est plus age que moi de {difference_age } years")
elif my_age > your_age:
    difference_age = my_age - your_age
    if difference_age ==1:
        print(f"je suis plus age que toi de {difference_age} year")
    else:
        print(f"je suis plus age toi de {difference_age} years ")
else:
    print("Nous avons les mêmes ages ")  

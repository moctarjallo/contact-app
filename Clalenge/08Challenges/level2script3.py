liste_fruits = ['banana', 'orange', 'mango', 'lemon']
#Si un fruit n'existe pas dans la liste, ajoutez-le à la liste et imprimez la liste modifiée.
#  Si le fruit existe, imprimez 'Ce fruit existe déjà dans la liste.
fruit = input("veillez enter le fruit ")
fruit = fruit.lower()
if fruit  in liste_fruits:
    print("Ce fruit existe déjà dans la liste")
else:
    liste_fruits.append(fruit)
    print(liste_fruits)


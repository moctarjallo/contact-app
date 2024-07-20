
"""La liste suivante contient quelques fruits :

fruits = ['banana', 'orange', 'mango', 'lemon']
Si un fruit n'existe pas dans la liste, ajoutez-le à la liste et imprimez la liste modifiée. Si le fruit existe, imprimez « Ce fruit existe déjà dans la liste. »)
"""
# Liste des fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
print(f"Les Fruits presents: {fruits}")
# Demande de l'entrée utilisateur pour un fruit
nouveau_fruit = input("Entrez un nouveau fruit : ").lower()

# Vérification si le fruit existe déjà dans la liste
if nouveau_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(nouveau_fruit)
    print("Le fruit a été ajouté à la liste.")
    print("La liste des fruits mise à jour est :", fruits)

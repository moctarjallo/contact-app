#1-  Obtenez l'entrée utilisateur en utilisant input("Entrez votre âge : ").

while True:
    try:
        age = int(input("Entrez votre âge : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

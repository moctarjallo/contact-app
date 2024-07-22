#level1
#Obtenez l'entrée utilisateur en utilisant input("Enter your age: "). 
# Si l'utilisateur a 18 ans ou plus, donnez un retour : You are old enough to learn to drive.. Si l'utilisateur a moins de 18 ans,
#  donnez un retour pour indiquer le nombre d'années manquantes. Exemple de sortie :
age_utilisateur = int(input("Enter your age: "))
if age_utilisateur >= 18:
    print("You are old enough to learn to drive")
else:
    print(f"il vous manque {18 - age_utilisateur} ans pour atteintre les 18 ans " )



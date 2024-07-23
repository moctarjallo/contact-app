"""
Height requirements checking in a theme park.
"""

def main():
    # Demandez la taille de l'utilisateur en centimètres et stockez le résultat dans une variable : height
    height = int(input("Veuillez entrer votre taille en centimètres : "))

    # Afficher le message approprié en fonction de la taille
    if height < 100:
        print("Désolé, vous êtes trop petit pour ce manège. Essayez un autre carrousel.")
    elif 100 <= height <= 150:
        print("Profitez de votre tour !")
    else:
        print("Désolé, vous êtes trop grand pour celui-ci !")

if __name__ == '__main__':
    main()

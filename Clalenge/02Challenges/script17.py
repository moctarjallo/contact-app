def verification_nombre(nombre):
    if nombre % 2 == 0:
        return f"le nombre {nombre} est paire"
    else:
        return f"le nombre {nombre} est impaire"
# pour demander a l'utilisateur de saisir le nombre 
try:
    saisie_utilisateur = int(input("saisir le nombre: "))
    resultat = verification_nombre(saisie_utilisateur)
    print(resultat)
except ValueError:
    print("Veillez saisir un nombre entier valide")

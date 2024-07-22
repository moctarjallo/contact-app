nombre10_1 = type('10')
nombre10_2 = type(10)
verification = nombre10_1 == nombre10_2
print(verification)
#Script20
nombre1 = int('9')
nombre2 = type(10)
egalite = nombre1 == nombre2
print(egalite)
try:
    nombre = type("entrez lz nombre") # Cela va lever une erreur car 'intput' n'existe pas.
except NameError as e:
    print(f"Erreur : {e}")
   # script21
heure = int(input("Entrez votre heure"))
taux_par_heure =int(input("Entrez votre taux par heure "))
calcul_salaire =heure * taux_par_heure
print(calcul_salaire) 
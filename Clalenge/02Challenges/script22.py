annees = int(input("Enrez le nombre d'anee que vous voulez vivre "))
max_annee = 100
if annees>max_annee:
    print("une personne ne peut vivre que j'usqu'à 100 ans ")
    annees = max_annee
    # Calculer le nombre de secondes
# 1 année = 365.25 jours (compte tenu des années bissextiles)
# 1 jour = 24 heures
# 1 heure = 60 minutes
# 1 minute = 60 secondes
seconde_annee = 365.25*24*60*60
seconde_vecu =seconde_annee*annees
print(f"vous avez vecue pendans{seconde_vecu} secondes")







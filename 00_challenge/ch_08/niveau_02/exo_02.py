

saisons = {
    'Automne': ['SEPTEMBRE', 'OCTOBRE', 'NOVEMBRE'],
    'Hiver': ['DÉCEMBRE', 'JANVIER', 'FÉVRIER'],
    'Printemps': ['MARS', 'AVRIL', 'MAI'],
    'Été': ['JUIN', 'JUILLET', 'AOÛT']
}

mois = input("Entrez le mois : ").upper()

saison = 'Inconnue'
for cle, valeur in saisons.items():
    if mois in valeur:
        saison = cle
        break

print(f"La saison est {saison}")

#20Coupez l'entreprise ou les entreprises IT du milieu de la liste.
i_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Imprimez la liste originale
print("Liste originale des entreprises IT :", i_companies)

# Déterminez l'index du milieu
milieu = len(i_companies) // 2

# Vérifiez si la longueur de la liste est paire ou impaire
if len(i_companies) % 2 == 0:
    # Si la liste a un nombre pair d'éléments, coupez deux entreprises au milieu
    i_companies = i_companies[:milieu-1] + i_companies[milieu+1:]
else:
    # Si la liste a un nombre impair d'éléments, coupez une entreprise au milieu
    i_companies = i_companies[:milieu] + i_companies[milieu+1:]

# Imprimez la liste après avoir coupé l'entreprise ou les entreprises au milieu
print("Liste après avoir coupé l'entreprise ou les entreprises au milieu :", i_companies)
#level 2
#Triez la liste et trouvez l'âge minimum et maximum.
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
tri_age = sorted(ages)
index_min = tri_age[0]
index_max = tri_age[-1] 
print(f"le tableau trier {tri_age}")
print(f"l'index du minimum est {index_min}")
print(f"l'index du maximm est {index_max}")

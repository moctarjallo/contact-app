# 1Concaténation des chaînes 'Thirty', 'Days', 'Of', 'Python'
chaine1 = 'Thirty'
chaine2 = 'Days'
chaine3 = 'Of'
chaine4 = 'Python'

# Utilisation de l'opérateur +
chaine_concatenee_1 = chaine1 + ' ' + chaine2 + ' ' + chaine3 + ' ' + chaine4
print(chaine_concatenee_1)  

#2 Concaténation des chaînes 'Coding', 'For', 'All'
chaine5 = 'Coding'
chaine6 = 'For'
chaine7 = 'All'

# Utilisation de l'opérateur +
chaine_concatenee_2 = chaine5 + ' ' + chaine6 + ' ' + chaine7
print(chaine_concatenee_2)  

# 3Déclaration de la variable 'company' et assignation de la valeur 'Coding For All'
company = 'Coding For All'
#4
print(company)  
#5 lonheur de la chaine en utilisant print() et len()
print(len(company))
#6changer les caracteres en maj en utilisant upper()
caracere_upper = company.upper()
print(caracere_upper)
#7Changez tous les caractères en minuscules en utilisant la méthode lower
caractere_lower = company.lower()
print(caractere_lower)
#8Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne Coding For All.
caractere_capitalize = company.capitalize()
print("le capitalize est", caractere_capitalize)
caractere_title = company.title()
print("le title  est ",caractere_title)
caractere_swapcase = company.swapcase()
print("le swipcase est ",caractere_swapcase)
#9Coupez (slice) le premier mot de la chaîne Coding For All.
mots_separer = company.split()
print(mots_separer)
mots_sans_le_premier_caract = mots_separer[1:]
print(mots_sans_le_premier_caract)
#script9
idex_espace = company.find(' ')
if idex_espace != -1:
    company_sans_premier = company[idex_espace +1:]
else:
    company_sans_premier = company
print("le mot est " + company_sans_premier)    
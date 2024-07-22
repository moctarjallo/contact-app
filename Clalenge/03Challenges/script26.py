#Trouvez la position de la première occurrence du mot 'because' dans la phrase suivante : 
# 'You cannot end a sentence with because because because is a conjunction'.
mot = 'because'
phrase = 'You cannot end a sentence with because because because is a conjunction'
index_occurence = phrase.find(mot)
print(index_occurence)
#27Coupez la phrase 'because because because' dans la phrase suivante : 
# 'You cannot end a sentence with because because because is a conjunction'.
phrases = 'because because because'
phrases2 = 'You cannot end a sentence with because because because is a conjunction'
#utilisation de split()  piur diviser  phrase2 par phrases 
diviser = phrases2.split(phrases)
# utilisation de joint() pour joindre phrases2 sans phrases 
mot_joint = ''.join(diviser).strip()
print(mot_joint)
#28La chaîne ''Coding For All' commence-t-elle par une sous-chaîne Coding ?
chaîne = 'Coding For All'
sous_chaîne = 'Coding'
verification = chaîne.startswith(sous_chaîne)
print(verification)
#29La chaîne 'Coding For All' se termine-t-elle par une sous-chaîne coding ?
chaine = 'Coding For All'
sous_chaine = 'Coding'
verif = chaine.endswith(sous_chaine)
print(verif)
#30'   Coding For All      '  , supprimez les espaces à gauche et à droite dans la chaîne donnée.
chaine3 = '   Coding For All      ' 
mot_sans_espace = chaine3.strip()
print(mot_sans_espace)
#31La liste suivante contient les noms de certaines bibliothèques python : ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Joignez la liste avec une chaîne de caractères hash avec espace.
bibliothèques = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joindre_bibliotheque = ' # '.join(bibliothèques)
print(joindre_bibliotheque)
#32Utilisez la séquence d'échappement de nouvelle ligne pour séparer les phrases suivantes.
premier = "I am enjoying this challenge"
deuxieme = "I just wonder what is next"
sequence = premier + '\n' + deuxieme
print(sequence)
#33Utilisez la séquence d'échappement de tabulation pour écrire les lignes suivantes.
ligne1 = "Name\tAge\tCountry\tCity" 
ligne2 = "Asabeneh\t250\tFinland\tHelsinki "
print(ligne1)
print(ligne2)
#34
# Déclaration des variables
radius = 10
area = 3.14 * radius ** 2

# Utilisation de la méthode .format() pour formater la chaîne
message = "The area of a circle with radius {} is {:.2f} meters square.".format(radius, area)

# Affichage du résultat
print(message)





 
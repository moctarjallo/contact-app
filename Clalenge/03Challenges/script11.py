#11Remplacez le mot coding dans la chaîne 'Coding For All' par Python.
# utilisation de la fonction replace
chaine = "Coding For All"
nouvelle_chaine = chaine.replace("Coding","Python")
print(nouvelle_chaine)
#12Changez Python for Everyone en Python for All en utilisant la méthode replace ou d'autres méthodes.
chaine1 = "Python for Everyone "
nouvelle_chaine1 = chaine1.replace("Python for Everyone","Python for All")
print(nouvelle_chaine1) 
#13 Divisez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()).
chaine2 = "Coding For All"
espace_mots = chaine2.split()
print(espace_mots)
#14"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divisez la chaîne au niveau de la virgule.
chaine3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
chaine_virgule = chaine3.split(',')
print(chaine_virgule)
#15Quel est le caractère à l'index 0 dans la chaîne Coding For All.
chaine4 = "Coding For All"
premier_caractere = chaine4[0]
print(premier_caractere)
#16Quel est le dernier index de la chaîne Coding For All.
dernier_index = len(chaine) -1
print(dernier_index)
#17 Quel caractère se trouve à l'index 10 dans la chaîne "Coding For All".
index_caractere = chaine4[10]
print(index_caractere)
#18Créez un acronyme ou une abréviation pour le nom 'Python For Everyone'.
nom = "Python For Everyone"
mot_separer =nom.split()
extrait_mot = [mot[0] for mot in mot_separer]
join_mot = ''.join(extrait_mot)
print(join_mot)
#19Créez un acronyme ou une abréviation pour le nom 'Coding For All'.
mots = "Coding For All"
separer_mot = mots.split()
#extraire les la premiere lettre de chaque mots
mots_extrait = [mot[0] for mot in separer_mot]
#joindre ces mots 
mot_join = ''.join(mots_extrait)
print(mot_join)
#20Utilisez l'index pour déterminer la position de la première occurrence de C dans Coding For All.
chaine5 = "Coding For All"
index_C = chaine5.index('C')
print(f"l'index de C dans {chaine5} est {index_C}")
#21Utilisez l'index pour déterminer la position de la première occurrence de F dans Coding For All.
index_F = chaine5.index('F')
print(f"l'index de de F dans {chaine5} est {index_F}")
#22Utilisez rfind pour déterminer la position de la dernière occurrence de l dans Coding For All People.
chaine6 = "Coding For All People"
index_L = chaine6.rfind('l')
print(index_L)
#23Utilisez index ou find pour trouver la position de la première occurrence du mot 'because' dans la phrase suivante 
# : 'You cannot end a sentence with because because because is a conjunction'.
#Utilisation de l'index
mot = "because"
phrase = "You cannot end a sentence with because because because is a conjunction"
occurence_mot = phrase.index(mot)
print(occurence_mot)
#utilisation de find
occ_mot = phrase.find(mot)
print(occ_mot)
#24Utilisez rindex pour trouver la position de la dernière occurrence du mot because dans la phrase suivante :
#  'You cannot end a sentence with because because because is a conjunction'.
mot2 = "because"
phrase2 = "You cannot end a sentence with because because because is a conjunction"
occu_der_mot = phrase2.rindex(mot2)
print(occu_der_mot)
#25Coupez la phrase 'because because because' dans la phrase suivante :
#  'You cannot end a sentence with because because because is a conjunction'.
because = "because because because"
remplace = "You cannot end a sentence with because because because is a conjunction"
# Utilisation de split() pour diviser la phrase par la sous-chaîne
separe = remplace.split(because)
# utilisation de join() pour recombiner sans la sous-chaîne
joint = ''.join(separe).strip()
print(joint)

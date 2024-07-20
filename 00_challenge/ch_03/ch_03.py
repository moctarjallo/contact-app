import math

# 1. Concaténez les chaînes de caractères
concatenation1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
concatenation2 = ' '.join(['Coding', 'For', 'All'])

# 2. Déclarez une variable nommée société et attribuez-lui la valeur initiale "Coding For All".
societe = "Coding For All"

# 3. Imprimez la variable société en utilisant print().
print(societe)

# 4. Imprimez la longueur de la chaîne de l'entreprise en utilisant la méthode len() et print().
print(len(societe))

# 5. Modifiez tous les caractères majuscules en utilisant la méthode upper().
print(societe.upper())

# 6. Modifiez tous les caractères en minuscules en utilisant la méthode lower().
print(societe.lower())

# 7. Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne Coding For All.
print(societe.capitalize())
print(societe.title())
print(societe.swapcase())

# 8. Coupez le premier mot de la chaîne Coding For All.
print(societe.split(' ', 1)[1])

# 9. Vérifiez si la chaîne Coding For All contient le mot Coding en utilisant les méthodes index, find ou autres méthodes.
print(societe.find('Coding') != -1)

# 10. Remplacez le mot coding dans la chaîne 'Coding For All' par Python.
print(societe.replace('Coding', 'Python'))

# 11. Passez de Python for Everyone à Python for All en utilisant la méthode replace ou d'autres méthodes.
phrase = 'Python for Everyone'
print(phrase.replace('Everyone', 'All'))

# 12. Divisez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()).
print(societe.split())

# 13. « Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon » divisent la chaîne au niveau de la virgule.
entreprises = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(entreprises.split(', '))

# 14. Quel est le caractère à l'index 0 dans la chaîne Coding For All.
print(societe[0])

# 15. Quel est le dernier index de la chaîne Coding For All.
print(societe[-1])

# 16. Quel caractère se trouve à l'index 10 dans la chaîne « Coding For All ».
print(societe[10])

# 17. Créez un acronyme ou une abréviation pour le nom « Python pour tous ».
print(''.join([mot[0] for mot in 'Python For All'.split()]))

# 18. Créez un acronyme ou une abréviation pour le nom « Coding For All ».
print(''.join([mot[0] for mot in 'Coding For All'.split()]))

# 19. Utilisez l'index pour déterminer la position de la première occurrence de C dans Coding For All.
print(societe.index('C'))

# 20. Utilisez l'index pour déterminer la position de la première occurrence de F dans Coding For All.
print(societe.index('F'))

# 21. Utilisez rfind pour déterminer la position de la dernière occurrence de l dans Coding For All People.
print('Coding For All People'.rfind('l'))

# 22. Utilisez index ou find pour trouver la position de la première occurrence du mot 'because' dans la phrase suivante : 
# 'Vous ne pouvez pas terminer une phrase par parce que parce que parce que est une conjonction'.
phrase_because = 'Vous ne pouvez pas terminer une phrase par parce que parce que parce que est une conjonction'
print(phrase_because.find('parce que'))

# 23. Utilisez rindex pour trouver la position de la dernière occurrence du mot because dans la phrase suivante :
print(phrase_because.rindex('parce que'))

# 24. Coupez la phrase 'parce que parce que parce que' dans la phrase suivante :
phrase_courte = phrase_because.replace('parce que parce que parce que', '')
print(phrase_courte)

# 25. La chaîne ''Coding For All'' commence-t-elle par une sous-chaîne Coding ?
print(societe.startswith('Coding'))

# 26. La chaîne 'Coding For All' se termine-t-elle par une sous-chaîne coding ?
print(societe.endswith('coding'))

# 27. « Coding For All », supprimez les espaces à gauche et à droite dans la chaîne donnée.
societe_espace = "   Coding For All   "
print(societe_espace.strip())

# 28. La liste suivante contient les noms de certaines bibliothèques python : ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Rejoignez la liste avec une chaîne de caractères hash avec espace.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# 29. Utilisez la séquence d'échappement de nouvelle ligne pour séparer les phrases suivantes.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 30. Utilisez la séquence d'échappement de tabulation pour écrire les lignes suivantes.
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 31. Utilisez la méthode de formatage de chaîne pour afficher ce qui convient :
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 32. Réalisez ce qui suit en utilisant les méthodes de formatage de chaîne :
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

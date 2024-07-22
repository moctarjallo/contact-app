#Vérifiez si la chaîne Coding For All contient le mot Coding en utilisant les méthodes index, find ou autres méthodes.
chaine = "Coding For All"
mot = "Coding"
#utilisation de la methode find()
index = chaine.find(mot)
if index != -1:
    print(f"{mot} apparait dans {chaine}")
else:
    print(f"{mot} n'apparait pas dans {chaine}")




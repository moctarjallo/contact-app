#1Déclarez une liste vide.
liste_vide = []
#2Déclarez une liste avec plus de 5 éléments.
liste_element =["Balde","Lamine", "Bougatti","ferari", 1702]
#3Trouvez la longueur de votre liste.
longeur_liste = len(liste_element)
print(longeur_liste)
#4Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste.
premier_element = liste_element[0]
element_milieu = liste_element[len(liste_element) //2]
dernier_element = liste_element[-1]
print(premier_element)
print(element_milieu)
print(dernier_element)
#5Déclarez une liste appelée mixed_data_types, mettez-y votre(name, age, height, marital status, address)
mixed_data_types = ["Balde",21,183,"Celibataire","Dixinn"]
#6Déclarez une variable de liste nommée it_companies et assignez-lui les valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))
element_premier =it_companies[0]
moyenne = len(it_companies)/2
derniere = it_companies[-1]
print(element_premier)
print(moyenne)
print(derniere)
it_companies[4]="Faraday"
print(it_companies)
it_companies.append("IT")
print(it_companies)
#12Insérez une entreprise IT au milieu de la liste des entreprises.
midle=len(it_companies)// 2
it_companies.insert(midle,"IT")
print(it_companies) 
#13Changez l'un des noms des it_companies en majuscules (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break
print(it_companies)
#14Joignez les it_companies avec une chaîne de caractères '#;  '
joint_int_com = '#;  '.join(it_companies)
print(joint_int_com)
#15Vérifiez si une certaine entreprise existe dans la liste it_companies.
def verifi_existance(nom_compagny):
    if nom_compagny in it_companies:
        print(f"la compagny {nom_compagny} existe sur la liste")
    else:
        print(f"la compagny {nom_compagny} n'existe pas sur la liste")
verifi_existance("Google")
verifi_existance("Sanou")
#16Triez la liste en utilisant la méthode sort().
i_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
i_companies.sort()
print(i_companies)
#17Inversez la liste dans l'ordre décroissant en utilisant la méthode reverse().
i_companies.reverse()
print(i_companies)
#18Coupez les 3 premières entreprises de la liste.
i_companies = i_companies[3:]
print(i_companies)
#19Coupez les 3 dernières entreprises de la liste.
li_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
li_companies = li_companies[:-3]
print(li_companies)









# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1-  Trouvez la longueur de l'ensemble it_companies.
print(f"la longeur de l'ensemble it_companiese est {len(it_companies)}")

# 2-  Ajoutez 'Twitter' à it_companies.
it_companies.add("Twitter")
print(f"Apres Ajour de Twitter: {it_companies}")
print(f"la longeur de l'ensemble it_companiese est {len(it_companies)}")

mon_set = set(("etienne",3,True,5,False,True))

# 3-   Insérez plusieurs entreprises IT à la fois dans l'ensemble it_companies.
it_companies.update(["Youtube","Spotify","Tiktok"])
print(it_companies)


# 4- Supprimez l'une des entreprises de l'ensemble it_companies.
it_companies.remove("Tiktok")
print(it_companies)

# 5- Quelle est la différence entre remove et discard ?
'''
    la différence entre les méhtodes remove et discard est la gestion de l'exception:
        ensemble.remove(element):Essaie de supprimer un "element" de "ensemble" et renvoie une exception Keyerror si "element" n'existe pas
        ensemble.discard(element):Essaie de supprimer un "element" de "ensemble" en ne revoie rien (pa d'erreur) meme si "element" n'existe pas dans "ensemble"
    
'''
# it_companies.remove("Meta")  #tentative de suppression avec status d'erreur en cas d'inexistence d'element&vjjj ;,f 
it_companies.discard("Meta")  #tentative de suppression sans status d'erreur en cas d'inexistence d'element



#  =================NIVEAU 2 ========================


# 1 - Joignez A et B

print(f"Union de A et B :{A.union(B)}")

# 2-      Trouvez l'intersection de A et B.

print(f"Intersection de A et B :{A.intersection(B)}")

# 3-  A est-il un sous-ensemble de B ?
print(f"A est-il un sous-ensemble de B ? :{A.issubset(B)}")


# 4-  A et B sont-ils des ensembles disjoints ?

print(f"A et B sont-ils des ensembles disjoints ?: {A.isdisjoint(B)}")

# 5-  Joignez A avec B et B avec A.

print(f"AUB: {A.union(B)}\n BUA {B.union(B)}")
# 6-  Quelle est la différence symétrique entre A et B ?
print(f"la Différence Symétrique de A et B est: {A.symmetric_difference(B)}")

# 7-  Supprimez complètement les ensembles.

del A
del B


# ================NIVEAU 3 ===================

# 1-  Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble, lequel est plus grand ?

ages_set = set(age)
print(f"la taille des l'ensemble :{ages_set} est inferieur que la taille de la liste {age}?: {ages_set<age}")

"""2-  
Expliquez la différence entre les types de données suivants : chaîne, liste, tuple et ensemble.

Chaîne (string) : Une séquence immuable de caractères.
Liste (list) : Une collection ordonnée et modifiable d'éléments.
Tuple : Une collection ordonnée mais immuable d'éléments.
Ensemble (set) : Une collection non ordonnée de valeurs uniques, modifiable.
"""


# 3-  Je suis enseignant et j'aime inspirer et enseigner les gens. 
# Combien de mots uniques ont été utilisés dans la phrase ? 
# Utilisez les méthodes split et set pour obtenir des mots uniques

phrase = "Je suis enseignant et j'aime inspirer et enseigner les gens"
unique_words = set(phrase.split())
print(len(unique_words))

#level1
#1Créez un tuple vide.
tuple_vide =()
#2Créez un tuple contenant les noms de vos sœurs et de vos frères (des frères et sœurs imaginaires sont acceptables).
tuple_famille = ("Tanou","Souleymane","Sanou","Oumou")
#3Joignez les tuples des frères et sœurs et assignez-le à siblings.
siblings = tuple_vide + tuple_famille
#4Combien de frères et sœurs avez-vous ?
nombre_f_s = len(tuple_famille)
print(nombre_f_s)
#5Modifiez le tuple siblings et ajoutez le nom de votre père et de votre mère et assignez-le à family_members.
tuple_famille = list(tuple_famille)
tuple_famille.extend(["Fatimato","Moamed yero"])
tuple_famille = tuple(tuple_famille)
print(tuple_famille)
#level2
#2Créez des tuples fruits, vegetables et animal products.
# Joignez les trois tuples et assignez-les à une variable appelée food_stuff_tp.
tuple_fruits =("Mangue","Orange","Banane")
tuple_vegetables =("Mais","Gombo")
tuple_animal=("Lion","Chat","Chien")
food_stuff_tp = tuple_fruits + tuple_vegetables + tuple_animal
#3Changez le tuple food_stuff_tp en une liste food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)

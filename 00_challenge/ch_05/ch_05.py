# 1- Create an empty tuple
void_tuple = ()

# 2- Create a tuple containing the names of your sisters and brothers
brothers = ("Laurent", "Gilbert")
sisters = ("Josephine", "Philomène", "Madeleine", "Rebeka")
print(f"Mes Frères : {brothers}")
print(f"Mes Soeurs : {sisters}")
# 3-  Joignez les tuples des frères et sœurs et assignez-le à siblings.
siblings = brothers + sisters
print(f"Mes Frères et Soeurs : {siblings}")

# 4- Combien de frères et sœurs avez-vous ??
print(f"j'ai {len(brothers)} Frères et {len(sisters)} Soeurs.")

# 5- Modifiez le tuple siblings et ajoutez le nom de votre père et de votre mère et assignez-le à family_members.
parents = ("Aly David", "Heleine Kadouno")
family_members = parents + siblings
print(f"My family members: {family_members}")

#============================== NIVEAU 2==================
# 5- Déballez siblings et parents à partir de family_members
print(f"Parents: {parents}")
print(f"Siblings: {siblings}")
print(f"Family Members: {family_members}")

# 6- Créez des tuples fruits, vegetables et animal products. Joignez les trois tuples et assignez-les à une variable appelée food_stuff_tp.
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "lettuce")
animal_products = ("milk", "cheese", "eggs")

food_stuff_tp = fruits + vegetables + animal_products
print(f"Food Stuff Tuple: {food_stuff_tp}")

#7   Changez le tuple food_stuff_tp en une liste food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print(f"Food Stuff List: {food_stuff_lt}")

# 8- Coupez l'élément ou les éléments du milieu du tuple food_stuff_tp ou de la liste food_stuff_lt.
length = len(food_stuff_lt)
middle_index = length // 2

if length % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index:middle_index + 1]

print(f"Middle Items: {middle_items}")

# 9- Coupez les trois premiers éléments et les trois derniers éléments de la liste food_stuff_lt.
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(f"First Three Items: {first_three}")
print(f"Last Three Items: {last_three}")

# 11- Supprimez complètement le tuple food_stuff_tp.
del food_stuff_tp

# 12- Check if an item exists in the tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print(f"Est-ce que 'Estonia' est un pays Nordique? {'Estonia' in nordic_countries}")
print(f"Est-ce que  'Iceland' est un pays Nordique? {'Iceland' in nordic_countries}")



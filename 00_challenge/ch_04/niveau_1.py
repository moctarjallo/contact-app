# 1. Déclarez une liste vide.
list_vide = []

# 2. Déclarez une liste avec plus de 5 éléments.
elements_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Trouvez la longueur de votre liste.
print(len(elements_list))

# 4. Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste.
premier_element = elements_list[0]
element_milieur = elements_list[len(elements_list) // 2]
dernier_element = elements_list[-1]
print(premier_element, element_milieur, dernier_element)

# 5. Déclarez une liste appelée mixed_data_types, mettez-y votre(name, age, height, marital status, address)
mixed_data_types = ["Kamano Etienne", 24, 165, "Célibataire Endurci", "Aviation Marché"]

# 6. Déclarez une variable de liste nommée it_companies et attribuez-lui les valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimez la liste en utilisant print()
print(it_companies)

# 8. Imprimez le nombre d'entreprises dans la liste.
print(len(it_companies))

# 9. Imprimez la première, la moyenne et la dernière entreprise.
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10. Imprimez la liste après avoir modifié l'une des entreprises.
it_companies[0] = "Meta"
print(it_companies)

# 11. Ajoutez une entreprise IT à it_companies.
it_companies.append("Twitter")
print(it_companies)

# 12. Insérez une entreprise IT au milieu de la liste des entreprises.
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Spotify")
print(it_companies)

# 13. Changez l'un des noms des sociétés informatiques en majuscules (IBM exclu !)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Rejoignez les it_companies avec une chaîne de caractères '#; '
joined_companies = ' #; '.join(it_companies)
print(joined_companies)

# 15. Vérifiez si une certaine entreprise existe dans la liste it_companies.
print("Google" in it_companies)

# 16. Essayez la liste en utilisant la méthode sort().
it_companies.sort()
print(it_companies)

# 17. Inversez la liste dans l'ordre décroissant en utilisant la méthode reverse().
it_companies.reverse()
print(it_companies)

# 18. Coupez les 3 premières entreprises de la liste.
print(it_companies[:3])

# 19. Coupez les 3 dernières entreprises de la liste.
print(it_companies[-3:])

# 20. Coupez l'entreprise ou les entreprises IT du milieu de la liste.
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

# 21. Supprimez la première entreprise IT de la liste.
it_companies.pop(0)
print(it_companies)

# 22. Supprimez l'entreprise ou les entreprises IT du milieu de la liste.
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# 23. Supprimez la dernière entreprise IT de la liste.
it_companies.pop()
print(it_companies)

# 24. Supprimez toutes les entreprises IT de la liste.
it_companies.clear()
print(it_companies)

# 25. Détruisez la liste des entreprises IT.
del it_companies

# 26. Rejoignez les listes suivantes :
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# 27. Après avoir joint les listes dans la question 26. Copiez la liste jointe et assignez-la à une variable full_stack.
# Ensuite, insérez Python et SQL après Redux.
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

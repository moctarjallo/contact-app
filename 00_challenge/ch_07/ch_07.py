# 1. Créez un dictionnaire `dog`
dog = {}

# 2. Ajoutez `name`, `color`, `breed`, `legs`, `age` au dictionnaire `dog`
dog['name'] = 'Doggy'
dog['color'] = 'marron'
dog['breed'] = 'Chien Africain'
dog['legs'] = 4
dog['age'] = 5
print("Dictionnaire dog:", dog)

# 3. Créez un dictionnaire `student` et ajoutez `first_name`, `last_name`, `gender`, `age`, `marital_status`, `skills`, `country`, `city` comme clés du dictionnaire.
student = {
    'first_name': 'Etienne',
    'last_name': 'Kamano',
    'gender': 'Masculin',
    'age': 22,
    'marital_status': 'Célibataire pro',
    'skills': ['Python', 'Java','C/C++','C#'],
    'country': 'Guinée',
    'city': 'Guéckédou'
}
print("Dictionnaire student:", student)

# 4. Obtenez la longueur du dictionnaire `student`
print("Longueur du dictionnaire student:", len(student))

# 5. Obtenez la valeur de `skills` et vérifiez le type de données, cela devrait être une liste.
skills = student['skills']
print("Compétences :", skills)
print("Le type de skills:", type(skills))

# 6. Modifiez les valeurs de `skills` en ajoutant une ou deux compétences.
student['skills'].append('PHP')
student['skills'].append('JavaScript')
print("Compténces Mises à jour:", student['skills'])

# 7. Obtenez les clés du dictionnaire sous forme de liste.
keys = list(student.keys())
print("Clés:", keys)

# 8. Obtenez les valeurs du dictionnaire sous forme de liste.
values = list(student.values())
print("Values:", values)

# 9. Modifiez le dictionnaire dans une liste de tuples en utilisant la méthode `items()`.
items = list(student.items())
print("Items:", items)

# 10. Supprimez un des éléments du dictionnaire.
del student['marital_status']
print("Student dictionary after deletion:", student)

# 11. Supprimez un des dictionnaires.
del dog
# print(dog)  # Uncommenting this will raise an error because 'dog' is deleted

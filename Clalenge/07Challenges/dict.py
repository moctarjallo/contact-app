# Créez un dictionnaire vide appelé dog.
dog = {}

# Ajoutez name, color, breed, legs, age au dictionnaire dog.
dog['name'] = 'Rex'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Créez un dictionnaire student et ajoutez les clés spécifiées.
student = {'first_name': 'John','last_name': 'Doe','gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],  # Assurez-vous que cela est bien une liste
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# Obtenez la longueur du dictionnaire student.
student_length = len(student)

# Obtenez la valeur de skills et vérifiez le type de données.
skills = student['skills']
print(skills)
skills_type = type(skills)
print(skills_type)

# Vérifiez que skills est bien une liste, sinon convertissez-la en liste.
if  isinstance(skills, list):
    skills = [skills]  # Convertissez en liste si ce n'est pas déjà le cas
    student['skills'] = skills

# Modifiez les valeurs de skills en ajoutant une ou deux compétences.
student['skills'].append('C++')
student['skills'].append('JavaScript')

# Obtenez les clés du dictionnaire sous forme de liste.
student_keys = list(student.keys())

# Obtenez les valeurs du dictionnaire sous forme de liste.
student_values = list(student.values())

# Changez le dictionnaire en une liste de tuples en utilisant la méthode items().
student_items = list(student.items())

# Supprimez un des éléments du dictionnaire.
del student['address']

# Supprimez un des dictionnaires.
del dog

# Résumé
print(f"Longueur du dictionnaire student: {student_length}")
print(f"Valeur de skills: {skills}, Type de données: {skills_type}")
print(f"Clés du dictionnaire student: {student_keys}")
print(f"Valeurs du dictionnaire student: {student_values}")
print(f"Dictionnaire student en liste de tuples: {student_items}")
print(f"Dictionnaire student après suppression d'une clé: {student}")

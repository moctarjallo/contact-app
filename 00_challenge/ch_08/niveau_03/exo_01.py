person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Vérifiez si le dictionnaire person a la clé 'skills'
if 'skills' in person:
    # Imprimez la compétence du milieu dans la liste 'skills'
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"La compétence du milieu est : {skills[middle_index]}")
    
    # Vérifiez si la personne a la compétence 'Python' et imprimez le résultat
    if 'Python' in skills:
        print("La personne a la compétence 'Python'.")
    else:
        print("La personne n'a pas la compétence 'Python'.")
    
    # Vérifiez les compétences pour déterminer le type de développeur
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("Il est un développeur front end.")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("Il est un développeur back end.")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("Il est un développeur fullstack.")
    else:
        print("Titre inconnu.")
        
# Vérifiez si la personne est mariée et vit en Finlande
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vit en Finlande. Il est marié.")

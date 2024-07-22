person = {
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
    skills = person['skills']
     # Imprimez la compétence du milieu dans la liste 'skills'
    middle_skill_index = len(skills) // 2
    print(f"La compétence du milieu est: {skills[middle_skill_index]}")
    # Vérifiez si la personne a la compétence 'Python' et imprimez le résultat
    has_python_skill = 'Python' in skills
    print(f"La personne a la compétence 'Python': {has_python_skill}")
    # Vérifiez les compétences et imprimez le titre correspondant
    if set(skills) == {'JavaScript', 'React'}:
        print("Il est un développeur front end")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("Il est un développeur back end")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("Il est un développeur fullstack")
    else:
        print("titre inconnu")

# Si la personne est mariée et vit en Finlande, imprimez les informations
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vit en {person['country']}. Il est marié.")

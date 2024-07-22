# Demandez à l'utilisateur d'entrer son score
score = int(input("Enter the student's score: "))

# Attribuer une note en fonction du score
if score >= 90:
    note = 'A'
elif score >= 80:
    note = 'B'
elif score >= 70:
    note = 'C'
elif score >= 60:
    note = 'D'
else:
    note = 'F'

# Afficher la note
print(f"la note de l'etudiant est : {note}")

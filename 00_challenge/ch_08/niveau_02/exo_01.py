"""Écrivez un code qui attribue une note aux étudiants en fonction de leurs scores :

 ```
 80-100, A
 70-89, B
 60-69, C
 50-59, D
 0-49, F
 ```
 
 """



while True:
    try: 
        score = int(input("Enter your score: "))
        break
    except ValueError:
        print("Entrer un score valide")

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is {grade}")

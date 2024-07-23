"""Obtenez deux noms d'utilisateur en utilisant une invitation d'entrée. Si a est plus grand que b, renvoyez a est plus
grand que b, si a est plus petit que b, renvoyez a est plus petit que b, sinon renvoyez a est égal à b. Exemple 
de sortie :

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
while True:
    try:
        a = int(input("Enter number one: "))
        b = int(input("Enter number two: "))
        break
    except ValueError:
        print("Il faut que tous soient des nombres: ")

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")
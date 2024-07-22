#Obtenez deux nombres de l'utilisateur en utilisant une invite d'entrée.
#  Si a est plus grand que b, renvoyez a is greater than b, 
# si a est plus petit que b, renvoyez a is smaller than b, 
# sinon renvoyez a is equal to b
a = int(input("Entrez la valeur de a "))
b = int(input("Entrez la valeur de b "))
if a > b:
    print("a is greater than b ")
elif a < b :
    print("a is smaller than b")
else:
    print("a is equal to b")
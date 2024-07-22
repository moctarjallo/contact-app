from math import pi
from cmath import sqrt
def add_two_numbers(nomb1,nomb2):
    somme = nomb1 + nomb2
    return somme
#2L'aire d'un cercle se calcule comme suit : area = π x r x r. Écrivez une fonction qui calcule area_of_circle.
def area_of_circle(r):
    area = pi*r* r
    return area
lair = area_of_circle(5)
print(f"l'air du cercle est {lair}")
#3Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et les additionne.
#Vérifiez si tous les éléments de la liste sont de type nombre. Sinon, donnez un retour d'information raisonnable.
def add_all_nums(*args):
    for arg in args:
        if not isinstance(arg ,(int,float)):
            return "Tous les arguments doivent etre des nombres "
    total = sum(args)
    return total
print(add_all_nums(3,6,9,1))
print(add_all_nums(2,"a",4,8))
#4La température en °C peut être convertie en °F en utilisant cette formule : °F = (°C x 9/5) + 32. 
# Écrivez une fonction qui convertit °C en °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celcius):
    degre_faraneit = (celcius*9/5)
    return degre_faraneit
celsius_temp = 30
fahrenheit_temp = convert_celsius_to_fahrenheit(celsius_temp)
print(fahrenheit_temp)
#6Écrivez une fonction appelée calculate_slope qui renvoie la pente d'une équation linéaire.
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("La valeur de x1 et celle de x2 doivent être différentes.")
    pente = (y2 - y1) / (x2 - x1)
    return pente

try:
    x1 = float(input("Entrez la valeur de x1 : "))
    y1 = float(input("Entrez la valeur de y1 : "))
    x2 = float(input("Entrez la valeur de x2 : "))
    y2 = float(input("Entrez la valeur de y2 : "))

    pente = calculate_slope(x1, y1, x2, y2)
    print(f"La pente de la droite passant par les points ({x1}, {y1}) et ({x2}, {y2}) est : {pente}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
#7Une équation quadratique se calcule comme suit : ax² + bx + c = 0. 
# Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    delta = b**2 -4*a*c
    solt1 = -b -sqrt(delta)/2*a
    solt2 = -b +sqrt(delta)/2*a
    return solt1,solt2
print(solve_quadratic_eqn(2,4,5))
#8Déclarez une fonction nommée print_list. Elle prend une liste comme paramètre et affiche chaque élément de la liste.
def print_list(lst):
    for elemet in lst:
        print(elemet)
ma_liste =["Lenz","lamine",17]
print(ma_liste)
#9Déclarez une fonction nommée reverse_list. 
#Elle prend un tableau comme paramètre et renvoie le tableau inversé (utilisez des boucles).
def reverse_list(lst):
    
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Exemple d'utilisation
ma_liste = ["Lenz","lamine",17]
liste_inversee = reverse_list(ma_liste)
print("Liste originale:", ma_liste)
print("Liste inversée:", liste_inversee)
#10. Déclarez une fonction nommée  `capitalize_list_items`.
# Elle prend une liste comme paramètre et renvoie une liste d'éléments en majuscules.
def capitalize_list_items(lst):
    element_majus = [item.upper()  for item in lst]
    return element_majus
elements = ["Lenz","lamine","Mohamed"]
print(capitalize_list_items(elements))
#11Déclarez une fonction nommée `add_item`. Elle prend une liste et un paramètre d'élément.
#Elle renvoie une liste avec l'élément ajouté à la fin.
def add_item(lst,element):
    lst.append(element)
    return(lst)
mange = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(mange,'Eau'))
mes_elements = [2,3,4,5,3]
print(add_item(mes_elements,8))
#12Déclarez une fonction nommée remove_item. Elle prend une liste et un paramètre d'élément. Elle renvoie une liste avec l'élément supprimé.
def remove_item(lst,elements):
    if elements in lst:
        lst.remove(elements)
        return lst
    else:
        return("l'element selectionner ne se trouve pas dans la liste")

mange = ['Potato', 'Tomato', 'Mango', 'Milk','Eau']
print(remove_item(mange,'Dos'))
#13Déclarez une fonction nommée sum_of_numbers. Elle prend un paramètre de nombre et additionne tous les nombres dans cette plage.
def sum_of_numbers(n):
    som_nombre = 0
    for i in range(1,n + 1) :
        som_nombre += i
    return som_nombre
print(sum_of_numbers(5))
#14Déclarez une fonction nommée sum_of_odds. Elle prend un paramètre de nombre et additionne tous les nombres impairs dans cette plage.
def sum_of_odds(n):
    total_impair = 0
    for i in range(1,n+1):
        if i % 2 !=0:
            total_impair += i
    return total_impair
print(sum_of_odds(10))
#15Déclarez une fonction nommée sum_of_even. Elle prend un paramètre de nombre et additionne tous les nombres pairs dans cette plage.
def sum_of_even(n):
    total_pair = 0
    for i in range(1,n+1):
        if i % 2 ==0:
            total_pair += i
    return total_pair
print(sum_of_even(10))        

    
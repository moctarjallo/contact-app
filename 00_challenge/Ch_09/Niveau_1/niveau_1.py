import math

# 1. Déclarez une fonction add_two_numbers. Elle prend deux paramètres et renvoie une somme.
def add_two_numbers(a, b):
    return a + b

# 2. L'aire d'un cercle se calcule comme suit : area = π x r x r. Écrivez une fonction qui calcule area_of_circle.
def area_of_circle(radius):
    return math.pi * radius ** 2

# 3. Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et les additionne.
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Tous les éléments doivent être des nombres."
        total += num
    return total

# 4. Écrivez une fonction qui convertit °C en °F.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Écrivez une fonction appelée check_season qui prend un paramètre de mois et renvoie la saison.
# def check_season(month):

#  RETOUR A ../ch_08/exo_02.py


# 6. Écrivez une fonction appelée calculate_slope qui renvoie la pente d'une équation linéaire.
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# 7. Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique.
import math
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        # dans le cas où il y a deux solutions (distinctes ou identiques)
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # dans le cas  où il n'ya qu'une seule solution
        root = -b / (2 * a)
        return root, None
    else:
        # dans le cas où il n'ya pas de solution possible
        return None,None

# 8. Déclarez une fonction nommée print_list. Elle prend une liste comme paramètre et affiche chaque élément de la liste.
def print_list(lst):
    for item in lst:
        print(item)

# 9. Déclarez une fonction nommée reverse_list. Elle prend un tableau comme paramètre et renvoie le tableau inversé.
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 10. Déclarez une fonction nommée capitalize_list_items. Elle prend une liste comme paramètre et renvoie une liste d'éléments en majuscules.
def capitalize_list_items(lst):
    return [item.upper() for item in lst]


# 11. Déclarez une fonction nommée add_item. Elle prend une liste et un paramètre d'élément. Elle renvoie une liste avec l'élément ajouté à la fin.
def add_item(lst, item):
    lst.append(item)
    return lst


# 12. Déclarez une fonction nommée remove_item. Elle prend une liste et un paramètre d'élément. Elle renvoie une liste avec l'élément supprimé.
def remove_item(lst, item):
    lst.remove(item)
    return lst


# 13. Déclarez une fonction nommée sum_of_numbers. Elle prend un paramètre de nombre et ajoute tous les nombres dans cette plage.
def sum_of_numbers(n):
    return sum(range(n + 1))


# 14. Déclarez une fonction nommée sum_of_odds. Elle prend un paramètre de nombre et ajoute tous les nombres impairs dans cette plage.
def sum_of_odds(n):
    return sum(num for num in range(n + 1) if num % 2 != 0)

# 15. Déclarez une fonction nommée sum_of_even. Elle prend un paramètre de nombre et ajoute tous les nombres pairs dans cette plage.
def sum_of_even(n):
    return sum(num for num in range(n + 1) if num % 2 == 0)

# Exercices : Niveau 2
# 1. Déclarez une fonction nommée evens_and_odds. Elle prend un entier positif comme paramètre et compte le nombre de nombres pairs et impairs.
def evens_and_odds(n):
    evens = len([num for num in range(n + 1) if num % 2 == 0])
    odds = len([num for num in range(n + 1) if num % 2 != 0])
    return f"The number of evens are {evens}. The number of odds are {odds}."

# 2. Appelez votre fonction factorielle, elle prend un nombre entier comme paramètre et renvoie la factorielle du nombre.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Appelez votre fonction is_empty, elle prend un paramètre et vérifie s'il est vide ou non.
def is_empty(param):
    return param == []

# 4. Écrivez différentes fonctions qui prennent des listes. Ils devraient calculer_moyenne, calculer_médiane, calculer_mode, calculer_plage, calculer_variance, calculer_std (écart type).
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        median = (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        median = lst[n//2]
    return median

def calculate_mode(lst):
    return max(set(lst), key=lst.count)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

# Exercices : Niveau 3
# 1. Écrivez une fonction appelée is_prime, qui vérifie si un nombre est premier.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# 2. Écrivez les fonctions qui sont vérifiées si tous les éléments sont uniques dans la liste.
def all_unique(lst):
    return len(lst) == len(set(lst))


# 3. Écrivez une fonction qui vérifie si tous les éléments de la liste sont du même type de données.
def all_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

from Ch_09.Niveau_1.countries_data import pays
# 4. Créez une fonction appelée les langues les plus parlées dans le monde. Elle doit renvoyer les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.
def most_spoken_language(pays=pays, top_n=10,croissant=True):
    # Dictionnaire pour stocker les populations par langue
    langues_population = {}
    
    # Parcourir la liste des pays
    for pays in pays:
        population = pays["population"]
        for langue in pays["languages"]:
            if langue in langues_population:
                langues_population[langue] += population
            else:
                langues_population[langue] = population
    
    # Trier les langues par population décroissante
    langues_tries = sorted(langues_population.items(), key=lambda x: x[1], reverse=True)
    
    # Renvoyer les top_n langues
    if not croissant:
       langues_tries.reverse()
    return langues_tries[:top_n]

# 5. Créez une fonction appelée les pays les plus peuplés. Elle doit renvoyer les 10 ou 20 pays les plus peuplés par ordre décroissant.
def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

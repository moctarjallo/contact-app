#Déclarez une fonction nommée evens_and_odds. Elle prend un entier positif comme paramètre et compte le nombre de nombres pairs et impairs.
def count_evens_and_odds(n):
  
    count_pair = 0
    count_impair = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            count_pair += 1
        else:
            count_impair += 1

    return count_pair, count_impair

print(count_evens_and_odds(25))  
#1Appelez votre fonction factorial, elle prend un nombre entier comme paramètre et renvoie la factorielle du nombre.
def factorial(n):
   
    if n < 0:
        return ("La factorielle d'un nombre negatif n'existe pas .")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(-1))   
print(factorial(1))   
print(factorial(5))   
print(factorial(10))  
#15Appelez votre fonction is_empty, elle prend un paramètre et vérifie s'il est vide ou non.
def is_empty(param):
    return param is None or param =="" 
print(is_empty(""))
print(is_empty(None))
#3Écrivez différentes fonctions qui prennent des listes. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
   
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    mean = sum(numbers) / len(numbers)
    return mean
def calculate_median(numbers):
    
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    if n % 2 == 0:
        median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
    else:
        median = numbers_sorted[n // 2]
    return median
from collections import Counter

def calculate_mode(numbers):
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [num for num, count in counter.items() if count == max_count]
    return mode
def calculate_range(numbers):
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    min_num = min(numbers)
    max_num = max(numbers)
    range_val = max_num - min_num
    return range_val
def calculate_variance(numbers):
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance
import math

def calculate_std(numbers):
    if not numbers:
        return ValueError("La liste ne doit pas être vide")

    variance = calculate_variance(numbers)
    std_deviation = math.sqrt(variance)
    return std_deviation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))


       
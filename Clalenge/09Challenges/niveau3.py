def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True  

    # Vérifier les diviseurs potentiels jusqu'à la racine carrée de number
    limit = int(number ** 0.5) + 1
    for i in range(2, limit):
        if number % i == 0:
            return False
    return True
def are_all_unique(items):
    return len(items) == len(set(items))
def are_all_same_type(items):
    if not items:
        return True
    first_type = type(items[0])
    return all(isinstance(item, first_type) for item in items)

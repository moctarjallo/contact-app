# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
it_companies.add("Twitter")
it_companies.remove("Amazon")
print(it_companies)
#level3
ages_list = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages_list)

len_list = len(ages_list)
len_set = len(ages_set)

print("Longueur de la liste :", len_list)
print("Longueur de l'ensemble :", len_set)

if len_set > len_list:
    print("L'ensemble a plus d'éléments que la liste.")
elif len_list > len_set:
    print("La liste a plus d'éléments que l'ensemble.")
else:
    print("La liste et l'ensemble ont le même nombre d'éléments.")


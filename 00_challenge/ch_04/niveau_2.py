import math

# Liste des âges
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Triez la liste et trouvez l'âge minimum et maximum.
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Âge minimum: {min_age}, Âge maximum: {max_age}")

# 2. Ajoutez de nouveau l'âge minimum et l'âge maximum à la liste.
ages.append(min_age)
ages.append(max_age)
print(f"Liste des âges après ajout: {ages}")

# 3. Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux).
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print(f"Âge médian: {median_age}")

# 4. Trouvez l'âge moyen (somme de tous les éléments divisés par leur nombre).
average_age = sum(ages) / len(ages)
print(f"Âge moyen: {average_age}")

# 5. Trouvez l'écart des âges (max moins min).
age_range = max_age - min_age
print(f"Écart des âges: {age_range}")

# 6. Comparez la valeur de (min - moyenne) et (max - moyenne), utilisez la méthode abs().
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"Différence min-moyenne: {min_avg_diff}, Différence max-moyenne: {max_avg_diff}")

# Liste des pays
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 
'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 
'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'] 

# 7. Trouvez le(s) pays du milieu dans la liste des pays.
middle_index_countries = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index_countries - 1:middle_index_countries + 1]
else:
    middle_countries = countries[middle_index_countries]
print(f"Pays du milieu: {middle_countries}")

# 8. Divisez la liste des pays en deux listes égales si le nombre est pair, sinon ajoutez un pays de plus à la première moitié.
if len(countries) % 2 == 0:
    first_half = countries[:middle_index_countries]
    second_half = countries[middle_index_countries:]
else:
    first_half = countries[:middle_index_countries]
    first_half.append("Ivory Coast")

print(first_half)
print(second_half)
 
 
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Déballez les trois premiers pays et le reste en tant que pays scandinaves.
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandinav_countries = countries2[:3]
first_tree_countries = countries2[3:]

print("les pays scandinave",scandinav_countries)
print("les 3 premisers pays",first_tree_countries)
from datetime import datetime, timedelta
heure_actuelle = datetime.now()
heure = heure_actuelle.hour
minute = heure_actuelle.minute
secondes = heure_actuelle.second
temps_en_seconde_depuis_epoque = heure_actuelle.timestamp()
jours_depuis_epoque = int(temps_en_seconde_depuis_epoque // (24*360))
print(heure_actuelle)
print(heure)
print(minute)
print(secondes)
print(temps_en_seconde_depuis_epoque)
print(jours_depuis_epoque)


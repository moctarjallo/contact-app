"""Écrire une classe Vehicle:
Un véhicule est défini par les attributs year, brand, color, wheels, consumption, fuel, kilometers. Il a aussi speed qui est toujours zéro lorsque le véhicule est instancié.
Écrivez les méthodes pour start, stop, accelerateet brake avec un incrément ou un décrément de la vitesse de 10 à chaque fois que la méthode est appelée.
Démarrer un chronomètre lorsque le véhicule startet arrêter le chronomètre lorsque le véhicule stop. Pendant ce temps, mettez à jour les kilometerset le fuel en fonction de la conduite ( speed, accelerateet stop).

Écrire deux nouvelles classes Caret Motorbikes. Imaginez ce qui pourrait changer dans les attributs et les méthodes.

Revoir l'accès au contrôle dans toutes les classes précédentes.

Votre programme doit être écrit dans vehicle.py. Vous devez pouvoir instancier des cercles et jouer avec eux directement depuis votre console iPython.
"""
import time
class Vehicle:
    def __init__(self,year, brand, color,wheels,fuel,consumption):
        self.year = year
        self.brand = brand
        self.color = color
        self.wheels = wheels
        self.consumption = consumption # le nombre de litre par kilometre que consome le vehicule
        self.fuel = fuel
        self.kilometers = 0
        self.speed = 0
        self.start_time = None
        self.is_started = False
    
    # methode start
    def start(self):
        
        if self.is_started: 
            print(f"le vehicule {self.brand} est deja en marche:")
        else:
            print("Demarrage ...")
            self.is_started = True
            self.start_time = time.time()
    # Methode d'arrete du vehicule
    def stop(self):
        if not self.is_started:
            print(f"le Vehicule {self.brand} est déja arreté")
        else:
            print("Arret")
            self.is_started = False
            self.start_time =None
            self.speed = 0
            
            # Mise à jours des parametres
            # temps_mis = (time.time()-self.start_time)/3600 #Recupération et conversion en heure du temps mis
            # self.kilometers += temps_mis * self.speed
            # self.fuel -= self.consumption * self.kilometers
            
            
    def accelerate(self):
        
        if not self.is_started:
            print(f"Le Vehicule {self.brand} n'est pas en marche")
        else:
            print("Accéleration")
            self.update_fuel()
            self.update_kilometers(self.speed)
            self.speed +=10            

    def brake(self):
        if self.speed >=10:
            print("Freinage")
            self.speed -=10
            self.update_fuel()
            self.update_kilometers(self.speed)

    def update_kilometers(self,speed): # la mise à jour du kilometrage à chaque modification du speed
        self.kilometers += ((time.time()-self.start_time)/3600) * speed

    def update_fuel(self):
        if  self.fuel != 0:
            self.fuel -= self.consumption * self.kilometers
        else:
            print("Vous n'avez pas de carburant")
            self.is_started = False
            
            
            
class Car(Vehicle):
    def __init__(self,year, brand, color,fuel,consumption):
        super().__init__(year, brand, color,4,fuel,consumption)


            
class Motobike(Vehicle):
    def __init__(self,year, brand, color,fuel,consumption):
        super().__init__(year, brand, color,2,fuel,consumption)


            
motoHonda = Motobike(year=2000,brand="Honda",color="blue",fuel=10,consumption=0.5) 

motoHonda.start()
print(f" distance parcourue : {motoHonda.kilometers} km")
print(f"Vitesse: {motoHonda.speed} km/h")

motoHonda.accelerate()
time.sleep(5)
print(f" distance parcourue : {motoHonda.kilometers} km")
print(f"Vitesse: {motoHonda.speed} km/h")
motoHonda.accelerate()
time.sleep(2)
print(f" distance parcourue : {motoHonda.kilometers} km")
print(f"Vitesse: {motoHonda.speed} km/h")

motoHonda.brake()
time.sleep(2)
print(f" distance parcourue : {motoHonda.kilometers} km")
print(f"Vitesse: {motoHonda.speed} km/h")

motoHonda.brake()
time.sleep(2)
print(f" distance parcourue : {motoHonda.kilometers} km")
print(f"Vitesse: {motoHonda.speed} km/h")

motoHonda.stop()
print(f"le carburant restant est :{motoHonda.fuel}litres " )



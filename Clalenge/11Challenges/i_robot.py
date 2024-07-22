
import math

def calculate_distance(x, y):
    """
    Calcule la distance entre le point (x, y) et l'origine (0, 0).

    Paramètres :
    x (int): Coordonnée x actuelle.
    y (int): Coordonnée y actuelle.

    Retourne :
    int: Distance arrondie à l'entier le plus proche.
    """
    return round(math.sqrt(x**2 + y**2))

def main():
    # Position initiale du robot
    x, y = 0, 0

    while True:
        # Demander à l'utilisateur le prochain mouvement
        move = input("What's your next move?\n>> ").strip().lower()
        
        # Si l'utilisateur entre "quit", sortir de la boucle
        if move == "quit":
            break
        
        # Analyser la direction et le nombre de pas
        try:
            direction, steps = move.split()
            steps = int(steps)
        except ValueError:
            print("Invalid input. Please enter the direction followed by the number of steps (e.g., 'up 5').")
            continue

        # Mettre à jour la position en fonction de la direction
        if direction == "up":
            y += steps
        elif direction == "down":
            y -= steps
        elif direction == "left":
            x -= steps
        elif direction == "right":
            x += steps
        else:
            print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
            continue
        
        # Afficher la nouvelle position
        print(f"New position : ({x}, {y})")

    # Calculer la distance par rapport à l'origine
    distance = calculate_distance(x, y)
    
    # Afficher la distance
    print(f"Distance from origin: {distance}")



    
        
        

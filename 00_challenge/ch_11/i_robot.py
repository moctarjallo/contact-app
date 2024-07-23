"""
Control the movements of a basic robot
"""
import math

# Code

class Robot:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.init_pos = (pos_x, pos_y)
        self.moving = False

    def start(self):
        print("Robot started")
        self.moving = True

    def stop(self):
        print("Robot stopped")
        self.moving = False

    @property
    def position(self):
        return (self.pos_x, self.pos_y)
        
    def up(self, pas):
        self.pos_y += pas
        self.print_position()

    def right(self, pas):
        self.pos_x += pas
        self.print_position()

    def down(self, pas):
        self.pos_y -= pas
        self.print_position()

    def left(self, pas):
        self.pos_x -= pas
        self.print_position()

    def print_position(self):
        print(f"New position : {self.position}\n")

    @property
    def distance(self):
        return ((self.init_pos[0] - self.pos_x)**2 + \
                (self.init_pos[1] - self.pos_y)**2)**.5


def main():
    robot = Robot(0, 0)
    robot.start()
    print("Initial position: ", robot.position)
    while robot.moving:
        move = input("What's your next move? \n>> ")
        if move == "quit":
            robot.stop()
            # Si la distance est un flottant, 
            # alors imprimez simplement l'entier le plus proche.
            print(f"Distance from origin: {round(robot.distance)}")
            break
        action, pas = move.split()
        pas = int(pas)
        if action == "up":
            robot.up(pas)
        if action == "right":
            robot.right(pas)
        if action == "down":
            robot.down(pas)
        if action == "left":
            robot.left(pas)

    """
Initial position: (0, 0)
What's your next move?
>> up 5
New position : (0, 5)
What's your next move?
>> right 4
New position : (4, 5)
What's your next move?
>> down 11
New position : (4, -6)
What's your next move?
>> left 1i!ç^=
New position : (3, -6)
What's your next move?
>> quit
Distance from origin: 7
    """

if __name__ == '__main__':
    main()
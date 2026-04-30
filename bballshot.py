'''Algorithmic logic steps:
1. Set the starting position of the ball
2. Set the position of the hoop.
3. Take in the shot angle and power
4. Convert those values into movement of the ball
5. update the balls position overtime (loop)
6. check if enters hoop area
7. output whether score or miss'''

import math

# graphic/plotting, from chatGPT
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("Welcome to Hoop House!")

# set ball start
ball_x = 0
ball_y = 0
# set hoop position
hoop_x = 20
hoop_y = 10

# initial shot settings
angle = 45
power = 5

print("Set up your shot!")
print("Type 'a' to increase your angle")
print("Type 'd' to decrease your angle")
print("Type 'p' to strengthen your power")
print("Type 'w' to weaken your power")
print("Type 'shoot' when ready")

while True:
    print("Calculated angle:", angle)
    print("Power accumulated:", power)

    move = input("Enter choice: ")

    if move == "a":
        angle = angle + 5     # = assigns new value, == checks equality
    elif move == "d":
        angle = angle - 5
    elif move == "p":
        power = power + 1
    elif move == "w":
        power = power - 1
    elif move == "shoot":
        break
    else:
        print("Invalid choice, please type only the letter or phrase intended")

angle_rad = math.radians(angle)

# convert angle + power to movement
x_chg = power * math.cos(angle_rad)
y_chg = power * math.sin(angle_rad)

gravity = 1 # arbitary, made a variable so its easier to change

trajectory = []
scored = False

for step in range(15):  # one step = one position update
    trajectory.append((ball_x, ball_y))

    # debug + visuals later? looks MESSY
    print("Step:", step)
    print("Ball position:", ball_x, ball_y)
    print("Current changes:", x_chg, y_chg)

    if abs(ball_x - hoop_x) <= 1 and abs(ball_y - hoop_y) <=1:
        print("Score")
        scored = True
        break

    # update ball pos
    ball_x = ball_x + x_chg
    ball_y = ball_y + y_chg

    # gravity pulls ball down
    y_chg = y_chg - gravity
    if ball_y < 0:
        break

if scored == False:
    print("Miss!")

print(trajectory)


# no way to exit
#want to also welcome them to the game


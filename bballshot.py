'''Algorithmic logic steps:
1. Set the starting position of the ball
2. Set the position of the hoop.
3. Take in the shot angle and power
4. Convert those values into movement of the ball
5. update the balls position overtime (loop)
6. check if enters hoop area
7. output whether score or miss'''

import math

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
print(")

angle_rad = math.radians(angle)

# convert angle + power to movement, from chatgpt
x_chg = power * math.cos(angle_rad)
y_chg = power * math.sin(angle_rad)

gravity = 1 # arbitary, made a variable so its easier to change

trajectory = []
scored = False

for step in range(15):  # one step = one position update
    trajectory.append((ball_x, ball_y))

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





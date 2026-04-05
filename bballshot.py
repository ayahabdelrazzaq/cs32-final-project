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

trajectory = []
scored = False

# ball movement
y_chg = 3
x_chg = 2

for step in range(15):  # one step = one position update
    trajectory.append((ball_x, ball_y))

    if abs(ball_x - hoop_x) <= 1 and abs(ball_y - hoop_y) <=1:
        print("Score")
        scored = True
        break

    ball_x = ball_x + x_chg

    # the ball starts falling
    if step > 4: # arbitrary
        y_chg = y_chg -1

if scored == False:
    print("Miss!")

print(trajectory)





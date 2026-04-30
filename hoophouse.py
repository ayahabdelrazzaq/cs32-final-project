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
import matplotlib.animation as animation

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
print("Type 'quit' to exit the game")

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
        if power > 1:   # prevent negative power
            power = power - 1
    elif move == "shoot":
        break
    elif move == "quit":
        print("Thanks for playing Hoop House!")
        exit()
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
        print("Score!!!")
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


# Visualizing shot
x_vals = []
y_vals = []

for point in trajectory:
    x_vals.append(point[0])
    y_vals.append(point[1])


# helper function to draw hoop
def draw_hoop(ax):
    # backboard
    ax.plot([hoop_x + 1, hoop_x + 1], [hoop_y - 1.5, hoop_y + 1.5], linewidth=3)

    # rim
    ax.plot([hoop_x - 1, hoop_x + 1], [hoop_y, hoop_y], linewidth=3)

    # net
    ax.plot([hoop_x - 1, hoop_x - 0.6], [hoop_y, hoop_y - 1], linewidth=1)
    ax.plot([hoop_x - 0.5, hoop_x - 0.2], [hoop_y, hoop_y - 1], linewidth=1)
    ax.plot([hoop_x, hoop_x], [hoop_y, hoop_y - 1], linewidth=1)
    ax.plot([hoop_x + 0.5, hoop_x + 0.2], [hoop_y, hoop_y - 1], linewidth=1)
    ax.plot([hoop_x + 1, hoop_x + 0.6], [hoop_y, hoop_y - 1], linewidth=1)
    ax.plot([hoop_x - 0.6, hoop_x + 0.6], [hoop_y - 1, hoop_y - 1], linewidth=1)


# FIRST: animation figure
fig, ax = plt.subplots()

ax.set_title("Basketball Shot Animation")
ax.set_xlabel("x-position")
ax.set_ylabel("y-position")

ax.axhline(y=0)

ax.set_xlim(-1, max(x_vals) + 5)
ax.set_ylim(-1, max(max(y_vals), hoop_y) + 5)

# draw start point
ax.plot(x_vals[0], y_vals[0], marker='o', color='pink', label="Start")

# draw hoop
draw_hoop(ax)

# create moving ball and trail
ball_plot, = ax.plot([], [], marker='o', color='orange', markersize=12, label="Ball")
trail_plot, = ax.plot([], [], color='blue', linewidth=2, label="Ball trajectory")

ax.legend()

# update function for animation
def update(frame):
    ball_plot.set_data([x_vals[frame]], [y_vals[frame]])
    trail_plot.set_data(x_vals[:frame + 1], y_vals[:frame + 1])
    return ball_plot, trail_plot

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x_vals),
    interval=800,
    repeat=False,
    blit=False
)

plt.show()
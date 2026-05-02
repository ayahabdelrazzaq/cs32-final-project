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

available_power_up = "none"
play_again = "yes"

while play_again == "yes":

    # reset shot variables
    ball_x = 0
    ball_y = 0
    hoop_x = 20
    hoop_y = 10
    angle = 45
    power = 5
    scored = False
    trajectory = []

    current_power_up = available_power_up


    print("Set up your shot!")
    print("Type 'a' to increase your angle")
    print("Type 'd' to decrease your angle")
    print("Type 'p' to strengthen your power")
    print("Type 'w' to weaken your power")
    print("Type 'shoot' when ready")
    print("Type 'quit' to exit the game")
    print("Power-up for this shot:", current_power_up)

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
            

    if current_power_up == "curve":
        target_angle = 50

        if angle < target_angle:
            angle = angle + 5
        elif angle > target_angle:
            angle = angle - 5

    angle_rad = math.radians(angle)

    # convert angle + power to movement
    x_chg = power * math.cos(angle_rad)
    y_chg = power * math.sin(angle_rad)

    gravity = 0.5 
    time_step = 0.5

    trajectory = []
    scored = False

    hoop_tolerance = 1.5
    if current_power_up == "accuracy":
        hoop_tolerance = 2.5

    for step in range(30):  # one step = one position update
        trajectory.append((ball_x, ball_y))

        # debug + visuals later? looks MESSY
        print("Step:", step)
        print("Ball position:", ball_x, ball_y)
        print("Current changes:", x_chg, y_chg)

        if abs(ball_x - hoop_x) <= hoop_tolerance and abs(ball_y - hoop_y) <= hoop_tolerance:
            print("Score!!!")
            scored = True
            break

        # update ball pos
        ball_x = ball_x + x_chg * time_step
        ball_y = ball_y + y_chg * time_step 

        # gravity pulls ball down
        y_chg = y_chg - gravity * time_step
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
        # bigger backboard
        ax.plot([hoop_x + 1.5, hoop_x + 1.5], [hoop_y - 2, hoop_y + 2], linewidth=4)

        # bigger rim
        ax.plot([hoop_x - 1.5, hoop_x + 1.5], [hoop_y, hoop_y], linewidth=4)

        # bigger net
        ax.plot([hoop_x - 1.5, hoop_x - 1.0], [hoop_y, hoop_y - 1.5], linewidth=1.5)
        ax.plot([hoop_x - 0.75, hoop_x - 0.3], [hoop_y, hoop_y - 1.5], linewidth=1.5)
        ax.plot([hoop_x, hoop_x], [hoop_y, hoop_y - 1.5], linewidth=1.5)
        ax.plot([hoop_x + 0.75, hoop_x + 0.3], [hoop_y, hoop_y - 1.5], linewidth=1.5)
        ax.plot([hoop_x + 1.5, hoop_x + 1.0], [hoop_y, hoop_y - 1.5], linewidth=1.5)
        ax.plot([hoop_x - 1.0, hoop_x + 1.0], [hoop_y - 1.5, hoop_y - 1.5], linewidth=1.5)


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
    trail_plot, = ax.plot([], [], color='purple', linewidth=2, linestyle='--', label="Ball trajectory")

    adlib_text = ax.text(0.72, 0.90, "", transform=ax.transAxes, fontsize=14)
    ax.text(0.02, 0.95, "Power-up: " + current_power_up, transform=ax.transAxes, fontsize=10)

    ax.legend()

    # update function for animation
    def update(frame):
        ball_plot.set_data([x_vals[frame]], [y_vals[frame]])
        trail_plot.set_data(x_vals[:frame + 1], y_vals[:frame + 1])

        # only show adlib once ball reaches/passes hoop,
        # or at the very end if it never gets there
        if x_vals[frame] >= hoop_x or frame == len(x_vals) - 1:
            if scored:
                adlib_text.set_text("SWISH!")
            else:
                adlib_text.set_text("MISS!")
        else:
            adlib_text.set_text("")

        return ball_plot, trail_plot, adlib_text

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(x_vals),
        interval=800,
        repeat=False,
        blit=False
    )

    plt.show()

    if scored:
        print("You made the shot! Choose a power-up for your NEXT shot: none, accuracy, or curve")
        available_power_up = input("Next power-up: ").lower()

        if available_power_up not in ["none", "accuracy", "curve"]:
            available_power_up = "none"
    else:
        available_power_up = "none"

    play_again = input("Play again? yes or no: ").lower()
'''Algorithmic logic steps:
1. Start the game and set default values for the ball, hoop, angle, power, and power-up
2. Let the player adjust angle and power or quit before taking the shot
3. Apply any active power-up effects to the shot setup
4. Convert the final angle and power into x and y movement
5. Simulate the shot over time, storing the ball's trajectory
6. Check whether the ball enters the hoop area and determine score or miss
7. Animate the shot and display visuals, including the hoop, trajectory, and "adlib text"
8. If the player scores, let them choose a power-up for the next shot
9. Ask whether the player wants to play again or exit the game
'''

import math

# graphic/plotting, from chatGPT
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
#

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
    print("------------------------------") #separation
    print("ANGLE RANGE: 15 to 75")
    print("Type 'a' to increase your angle")
    print("Type 'd' to decrease your angle")
    print("------------------------------")
    print("POWER RANGE: 1 to 15")
    print("Type 'p' to strengthen your power")
    print("Type 'w' to weaken your power")
    print("------------------------------")
    print("Type 'shoot' when ready")
    print("Type 'quit' to exit the game")
    print("Power-up for this shot:", current_power_up)
    print("------------------------------")

    # Setting up the shot
    while True:
        print("Calculated angle:", angle)
        print("Power accumulated:", power)

        move = input("Enter choice: ")

        if move == "a":
            if angle < 75:
                angle = angle + 5
            else:
                print("Angle is already at the maximum.")

        elif move == "d":
            if angle > 15:
                angle = angle - 5
            else:
                print("Angle is already at the minimum.")

        elif move == "p":
            if power < 15:
                power = power + 1
            else:
                print("Power is already at the maximum.")

        elif move == "w":
            if power > 1:
                power = power - 1
            else:
                print("Power is already at the minimum.")

        elif move == "shoot":
            break

        elif move == "quit":
            print("Thanks for playing Hoop House!")
            exit()
        
        else:
            print("Invalid command. Please type: a, d, p, w, shoot, or quit")

    # Curve power-up
    if current_power_up == "curve":
        target_angle = 50

        if angle < target_angle:
            angle = angle + 5
        elif angle > target_angle:
            angle = angle - 5

    angle_rad = math.radians(angle)

    # convert angle and power to movement
    x_chg = power * math.cos(angle_rad)
    y_chg = power * math.sin(angle_rad)

    gravity = 0.5 
    time_step = 0.5

    trajectory = []
    scored = False

    normal_tolerance = 1.5
    hoop_tolerance = normal_tolerance
    used_accuracy_help = False 

    # Accuracy power-up
    if current_power_up == "accuracy":
        hoop_tolerance = 2.5
    

    for step in range(15):  # one step = one position update
        trajectory.append((ball_x, ball_y))

        if abs(ball_x - hoop_x) <= hoop_tolerance and abs(ball_y - hoop_y) <= hoop_tolerance:
            print("Score!!!")
            scored = True

            if current_power_up == "accuracy":
                if abs(ball_x - hoop_x) > normal_tolerance or abs(ball_y - hoop_y) > normal_tolerance:
                    used_accuracy_help = True

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


    # Visualizing shot, from chatGPT
    x_vals = []
    y_vals = []
    
    for point in trajectory:
        x_vals.append(point[0])
        y_vals.append(point[1])

    # helper function to draw hoop, from chatGPT
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


    # animation figure, from chatGPT
    fig, ax = plt.subplots()

    ax.set_title("Basketball Shot Animation")
    ax.set_xlabel("x-position")
    ax.set_ylabel("y-position")

    ax.axhline(y=0)

    ax.set_xlim(-1, 35)
    ax.set_ylim(-1, 15)

    # draw start point
    ax.plot(x_vals[0], y_vals[0], marker='o', color='pink', label="Start")

    # draw hoop
    draw_hoop(ax)

    if current_power_up == "accuracy":
        accuracy_box = patches.Rectangle(
            (hoop_x - hoop_tolerance, hoop_y - hoop_tolerance),
            2 * hoop_tolerance,
            2 * hoop_tolerance,
            linewidth=2,
            edgecolor='green',
            facecolor='green',
            linestyle='--',
            alpha=0.15
        )
        ax.add_patch(accuracy_box)

    # create moving ball and trail, from chatGPT
    ball_plot, = ax.plot([], [], marker='o', color='orange', markersize=12, label="Ball")
    trail_plot, = ax.plot([], [], color='purple', linewidth=2, linestyle='--', label="Ball trajectory")

    adlib_text = ax.text(0.72, 0.90, "", transform=ax.transAxes, fontsize=14)
    ax.text(0.02, 0.95, "Power-up: " + current_power_up, transform=ax.transAxes, fontsize=10)

    ax.legend()
    #

    # update function for animation
    def update(frame):
        ball_plot.set_data([x_vals[frame]], [y_vals[frame]])
        trail_plot.set_data(x_vals[:frame + 1], y_vals[:frame + 1])

        # only show adlib once ball reaches/passes hoop, or at end if no score
        if x_vals[frame] >= hoop_x or frame == len(x_vals) - 1:
            if scored:
                if current_power_up == "accuracy":
                    adlib_text.set_text("SCORE! Sweet accuracy!")
                elif current_power_up == "curve":
                    adlib_text.set_text("SCORE! Eagled it in!")
                else:
                    adlib_text.set_text("SWISH!")
            else:
                adlib_text.set_text("MISS!")
        else:
            adlib_text.set_text("")

        return ball_plot, trail_plot, adlib_text

    # create animation, from chatGPT 
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(x_vals),
        interval=800,
        repeat=False,
        blit=False
    )

    plt.show()
    #
    
    if scored:
        print("You made the shot!")
        print("Choose a power-up for your NEXT shot: none, accuracy, or curve")
        print("Type 'quit' to exit the game")

        while True:
            available_power_up = input("Next power-up: ").lower()

            if available_power_up in ["none", "accuracy", "curve"]:
                break
            elif available_power_up == "quit":
                print("Thanks for playing Hoop House!")
                exit()
            else:
                print("Invalid power-up. Please type: none, accuracy, curve, or quit")
    else:
        available_power_up = "none"

    play_again = input("Play again? yes or no: ").lower()
    if play_again != "yes":
        print("Thanks for playing Hoop House!")
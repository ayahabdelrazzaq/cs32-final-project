# cs32-final-project
My CS32 Final Project

# Project description

This project is a basketball shooting game inspired by the dramatic style of sports in animes (e.g. Kuroko's Basketball). The player (the user) sets up a shot by choosing the ball's angle and power, and the program tracks the movement of the ball through the air. Based on the ball's trajectory, the code determines whether the shot goes in the hoop or misses.

The current version of the project allows the user to play multiple rounds, adjust angle and power within set ranges (so they have a better idea of the values they should use), and watch the shot through an animated visual created with `matplotlib`. The game also includes power-ups that can be earned after making a shot and then used on the next round. These currently include:
- **accuracy**, which increases the effective hoop area
- **curve**, which adjusts the shot angle to help guide the ball

The program also includes simple game feedback, such as score (swish) or miss messages, "adlib text" during the animation, and a replay option so the user can continue playing.

# How to run the program
1. Run the program with: python3 hoophouse.py
2. When the program starts, it will ask the user to set up a shot and instructs how:

Angle control:
"Type 'a' to increase your angle"
"Type 'd' to decrease your angle"

Power control:
"Type 'p' to strengthen your power"
"Type 'w' to weaken your power"

Other commands:
"Type 'shoot' when ready"
"Type 'quit' to exit the game"

3. The program then simulates the shot, animates the ball’s trajectory, and displays whether the shot was made or missed.

If the player makes the shot, they are prompted to choose a power-up for the next round:
- None
- Accuracy
- Curve

At the end of each round, the player can choose whether to play again, and they can exit at any point.

# Special setup
- Python’s built-in math module for trigonometric calculations
- matplotlib for animation and game visuals
- matplotlib.patches for extra visual elements, such as the accuracy zone

If matplotlib is not already installed, use:
    python -m pip install matplotlib

# External Contributors

## Online tutorials

Used in learning/refreshing about list operations and related basics:
https://docs.python.org/3/tutorial/datastructures.html 

This helped me ensure I was using the operations properly.

Used in learning matplotlib:
https://matplotlib.org/stable/users/explain/quick_start.html#quick-start
https://matplotlib.org/stable/api/index.html
https://matplotlib.org/stable/users/explain/animations/animations.html#animations
https://matplotlib.org/stable/users/explain/colors/colors.html
https://matplotlib.org/stable/users/explain/text/index.html
https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html
https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
https://matplotlib.org/stable/api/patches_api.html

Used in learning about the math module and trig functions for projectile motion:
https://youtu.be/AHNdVt58eQE?si=3e7e14GN2A9V5Fd3
https://youtu.be/uXBf9yYG-TA?si=QhPJdR0c35f20TbG
https://youtu.be/ZxJs4M0qPqA?si=Y7qOuNNxh2cjwDyZ

These helped me better understand how to use trigonometric functions and angle conversion in Python, despite still using chatGPT for help (see below).


## Generative AI
I used ChatGPT as a support tool while working on my project. It helped me understand how to model a basketball shot with projectile motion and how to connect my game logic to an actual visual, and further, a visual animation.

Here are the code pieces it assisted me with:


angle_rad = math.radians(angle)
x_chg = power * math.cos(angle_rad)
y_chg = power * math.sin(angle_rad)

This code takes the user’s chosen angle and power and turns them into horizontal and vertical movement for the ball.
- math.radians(angle) converts the angle from degrees to radians, because Python’s trig functions use radians.
- math.cos(angle_rad) gives the horizontal portion of the shot.
- math.sin(angle_rad) gives the vertical portion of the shot.
Multiplied by power so the ball moves faster or slower depending on how much power the user selected.


def draw_hoop(ax):
    ax.plot([hoop_x + 1.5, hoop_x + 1.5], [hoop_y - 2, hoop_y + 2], linewidth=4)

    ax.plot([hoop_x - 1.5, hoop_x + 1.5], [hoop_y, hoop_y], linewidth=4)

    ax.plot([hoop_x - 1.5, hoop_x - 1.0], [hoop_y, hoop_y - 1.5], linewidth=1.5)
    ax.plot([hoop_x - 0.75, hoop_x - 0.3], [hoop_y, hoop_y - 1.5], linewidth=1.5)
    ax.plot([hoop_x, hoop_x], [hoop_y, hoop_y - 1.5], linewidth=1.5)
    ax.plot([hoop_x + 0.75, hoop_x + 0.3], [hoop_y, hoop_y - 1.5], linewidth=1.5)
    ax.plot([hoop_x + 1.5, hoop_x + 1.0], [hoop_y, hoop_y - 1.5], linewidth=1.5)
    ax.plot([hoop_x - 1.0, hoop_x + 1.0], [hoop_y - 1.5, hoop_y - 1.5], linewidth=1.5) 

This function draws the hoop on the graph. I used a helper function here so I could keep the hoop-drawing code in one place and call it whenever I needed to draw the hoop on the figure.

The first ax.plot line draws the backboard as a vertical line, the second ax.plot line draws the rim as a horizontal line, and the remaining lines draw a simple net underneath the rim. It's all pretty straightforward code, but because I was unfamiliar with the ax.plot function I needed help from chatGPT. 
ax.plot() tells matplotlib to draw a line on the graph. Within the first brackets, we have the x-coordinates of the 2 endpoints. When we look specifically at the backboard line, for example, because both x values are the same, the line doesn't move horizontally, so it just produces a vertical line. Within the second brackets, we have the y-coordinates of the 2 endpoints. Looking at the backboard line again, subtracting and adding 2 from hoop_y (the hoop center) means the vertical line starts 2 units below and ends 2 units above the hoop center (height of the backboard). Linewidth just makes the lines easier to see for the user. This same logic is used for the rim and net. AI here was useful for getting the correct values when plotting each of these lines.


ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x_vals),
    interval=800,
    repeat=False,
    blit=False
)

plt.show()

This block turns the graph into a live animation for the user. Despite briefly reading about matplotlib animation tools, it was still intimidating to approach by itself, chatGPT made it a lot easier than just reading the documentation. 
animation.FuncAnimation() repeadetly calls my update function. fig is just the graph being animated. update is the function that moves the ball, extends the trail, and updates the "adlib text" each frame, frames=len(x_vals) means the animation runs once for each point (x value) in the trajectory. interval=800 sets the delay between the frames in ms, controlling the speed of the animation. repeat=False means the animation plays just once. blit=False tells matplotlib to redraw the figure each frame, which is simpler and worked better for my project. plt.show() displays the figure to the user.
# cs32-final-project
My CS32 Final Project

# Project description

This project is a basketball shooting game inspired by the dramatic style of sports in animes (e.g. Kuroko's Basketball). The player (the user) sets up a shot by choosing the ball's angle and power, and the program tracks the movement of the ball through the air. Based on the ball's trajectory, the code determines whether the shot goes in the hoop or misses.

The current version of the project allows the user to play multiple rounds, adjust angle and power within set ranges (so they have a better idea of the values they should use), and watch the shot through an animated visual created with `matplotlib`. The game also includes power-ups that can be earned after making a shot and then used on the next round. These currently include:
- **accuracy**, which increases the effective hoop area
- **curve**, which adjusts the shot angle to help guide the ball

The program also includes simple game feedback, such as score (swish) or miss messages, "adlib text" during the animation, and a replay option so the user can continue playing.

# How to run the program
1. Run the program with: python3 bballshot.py
2. When the program starts, it will ask the user to se up a shot and instructs how:

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

# References
Used in learning about the math module:
https://youtu.be/AHNdVt58eQE?si=3e7e14GN2A9V5Fd3
https://youtu.be/uXBf9yYG-TA?si=QhPJdR0c35f20TbG
https://youtu.be/ZxJs4M0qPqA?si=Y7qOuNNxh2cjwDyZ

I used ChatGPT as a support tool while working on my project. Namely, I used it to help me understand how to model a basketball shot using projectile motion. The specific code it wrote for me was:

angle_rad = math.radians(angle)
x_chg = power * math.cos(angle_rad)
y_chg = power * math.sin(angle_rad)

I copied these lines into my project so that the user’s chosen angle and power could be converted into horizontal and vertical movement of the ball. However, I made sure I understood the overall purpose of the code before using it.

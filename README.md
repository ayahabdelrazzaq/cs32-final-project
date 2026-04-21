# cs32-final-project
My CS32 Final Project

# Project description

This project is a basketball shooting game inspired by the dramatic style of sports in animes (e.g. Kuroko's Basketball). The player (the user) sets up a shot by choosing the ball's angle and power, and the program simulates the movement of the ball through the air. Based on the ball's trajectory, the code determines whether the shot goes in the hoop or misses.

Right now, the project focuses on simulating one basketball shot to make the program more manageable. The current version allows the user to adjust shot settings, lanuches the ball using projectile motion logic, tracks the ball's position over time, and checks whether the ball enters the hoop area.

In later versions, I hope to expand the game with more features such as scoring systems, multiple shots, visuals, and power-ups (accuracy boost, 2nd chance, curve ball).

# How to run the program
1. Run the program with: python3 bballshot.py
2. When the program starts, it will ask the user to se up a shot and instructs how:
"Type 'a' to increase your angle"
"Type 'd' to decrease your angle"
"Type 'p' to strengthen your power"
"Type 'w' to weaken your power"
"Type 'shoot' when ready"
3. The program will then simulate the shot and print whether the result is a "Score!" or "Miss!" It will also print the trajectory of the ball as a list of coordinates (to be replaced by visuals)

# Special setup
This project uses Python's built-in math module for trig calculations. No extra package installation is required.

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

import numpy as np  # Importing the NumPy library, used for numerical computations like arrays and mathematical operations.
import matplotlib.pyplot as plt  # Importing Matplotlib's pyplot module to create plots and visualizations.
from matplotlib.animation import FuncAnimation  # Importing FuncAnimation to create animations in Matplotlib.

# Constants
g = 9.8  # The gravitational acceleration on Earth, in meters per second squared (m/s^2).

# User inputs
# Get the mass of the popper from the user as a floating-point number (in kilograms).
mass = float(input("Enter the mass of the popper (kg): "))
# Get the maximum height reached by the popper from the user (in meters).
max_height = float(input("Enter the maximum height reached by the popper (m): "))
# Get the number of frames to use in the animation, which controls the smoothness of the motion.
frame_count = int(input("Enter the number of frames for the animation: "))

# Total Mechanical Energy (TME)
# Calculate the total mechanical energy, which is the sum of potential and kinetic energy. 
# At the maximum height, TME is purely potential energy (mass * gravity * height).
TME = mass * g * max_height

# Height and Energy Calculations
# Create an array of time points evenly spaced from 0 to the total time of flight, based on frame_count.
times = np.linspace(0, 2 * (2 * max_height / g) ** 0.5, frame_count)
# Calculate heights using a sine-squared function to simulate symmetric motion (up and down).
heights = max_height * np.sin(np.pi * times / times[-1]) ** 2
# Calculate potential energy at each height: PE = mass * gravity * height.
potential_energies = mass * g * heights
# Calculate kinetic energy at each height: KE = Total Mechanical Energy - Potential Energy.
kinetic_energies = TME - potential_energies

# Setup the figure and axes
# Create a figure (`fig`) with two subplots arranged vertically (`ax` is a list of subplots).
fig, ax = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 2]})
# Split the axes into height (top plot) and energy (bottom plot).
height_ax, energy_ax = ax

# Top Plot: Popper Motion
# Set the horizontal axis (x-axis) limits for the height plot (it’s fixed, so we only care about height changes).
height_ax.set_xlim(0, 1)
# Set the vertical axis (y-axis) limits slightly above the maximum height for better visualization.
height_ax.set_ylim(0, max_height + 0.1)
# Add a title to the top plot to describe its purpose.
height_ax.set_title("Popper Motion and Height")
# Plot a circular marker to represent the popper, initially placed at x=0.5 and y=0.
popper, = height_ax.plot([0.5], [0], 'o', markersize=20, color='orange')
# Add a horizontal line at y=0 to represent the ground.
height_ax.axhline(y=0, color='black', linewidth=1)

# Bottom Plot: Energy Bars
# Set the horizontal axis (x-axis) limits for the energy bar plot.
energy_ax.set_xlim(0, 3)
# Set the vertical axis (y-axis) limits to slightly above the total mechanical energy for better visualization.
energy_ax.set_ylim(0, TME + 1)
# Define positions for the energy bar labels on the x-axis.
energy_ax.set_xticks([1, 2])
# Set labels for the energy bars: "Kinetic Energy" and "Potential Energy."
energy_ax.set_xticklabels(['Kinetic Energy (KE)', 'Potential Energy (PE)'])
# Add a title to the bottom plot to describe its purpose.
energy_ax.set_title("Kinetic and Potential Energy")
# Create a bar for kinetic energy, starting with its initial value (blue color).
ke_bar = energy_ax.bar(1, kinetic_energies[0], color='blue', width=0.4)
# Create a bar for potential energy, starting with its initial value (green color).
pe_bar = energy_ax.bar(2, potential_energies[0], color='green', width=0.4)

# Animation function
def update(frame):
    """
    Updates the animation for each frame.
    Args:
        frame: The current frame index.
    """
    # Calculate the current height of the popper based on the frame index.
    current_height = heights[frame]
    # Update the position of the popper marker in the height plot.
    popper.set_data([0.5], [current_height])

    # Update the height of the kinetic energy bar in the energy plot.
    ke_bar.patches[0].set_height(kinetic_energies[frame])
    # Update the height of the potential energy bar in the energy plot.
    pe_bar.patches[0].set_height(potential_energies[frame])

    # Return the updated elements to Matplotlib for rendering.
    return popper, ke_bar.patches[0], pe_bar.patches[0]

# Animate
# Create the animation using FuncAnimation. It updates the plot using the `update` function.
# `fig` is the figure to animate, `update` is the function called for each frame, and `frames` is the number of frames.
# `interval` specifies the time between frames in milliseconds (50 ms = 20 frames per second).
ani = FuncAnimation(fig, update, frames=frame_count, interval=50, blit=True)

# Save as GIF or MP4
# Prompt the user to save the animation as a GIF or MP4, or skip saving.
save_option = input("Save animation? Enter 'gif' or 'mp4' (or press Enter to skip): ").strip().lower()
if save_option == 'gif':
    # Save the animation as a GIF using the ImageMagick writer.
    ani.save("popper_motion.gif", writer='imagemagick', fps=30)
    print("Animation saved as 'popper_motion.gif'.")
elif save_option == 'mp4':
    # Save the animation as an MP4 video using the FFmpeg writer.
    ani.save("popper_motion.mp4", writer='ffmpeg', fps=30)
    print("Animation saved as 'popper_motion.mp4'.")

# Display the animation in a Matplotlib window.
plt.show()

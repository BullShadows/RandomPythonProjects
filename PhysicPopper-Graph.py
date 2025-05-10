import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.image as mpimg
import pygame

# Constants
g = 9.8  # gravitational acceleration (m/s^2)

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matplotlib in Pygame with Sliders")

# Colors and fonts
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 36)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Slider properties
slider_mass_x, slider_mass_y = 100, 50
slider_height_x, slider_height_y = 100, 150
slider_width, slider_height = 300, 10
slider_radius = 10
min_mass, max_mass = 0.01, 2.0  # Min and max values for mass
min_height, max_height = 0.1, 5.0  # Min and max values for height
mass_position = slider_mass_x
height_position = slider_height_x
is_dragging_mass = False
is_dragging_height = False

# Matplotlib figure and canvas
fig, ax = plt.subplots(2, 1, figsize=(4, 6), gridspec_kw={'height_ratios': [3, 2]})
canvas = FigureCanvas(fig)  # Attach an Agg canvas to the figure
height_ax, energy_ax = ax

# Load the image
popper_image = mpimg.imread("MoldySanta.png")
image_artist = height_ax.imshow(
    popper_image,
    extent=[0.45, 0.55, 0, 0.1],
    aspect='auto'
)

# Function to update calculations and plot
def update_calculations_and_plot(mass, max_height, frame_count):
    TME = mass * g * max_height
    times = np.linspace(0, 2 * (2 * max_height / g) ** 0.5, frame_count)
    heights = max_height * np.sin(np.pi * times / times[-1]) ** 2
    potential_energies = mass * g * heights
    kinetic_energies = TME - potential_energies
    return TME, heights, potential_energies, kinetic_energies

# Initial parameters
frame_count = 60
initial_mass = 1.0
initial_max_height = 2.0
TME, heights, potential_energies, kinetic_energies = update_calculations_and_plot(initial_mass, initial_max_height, frame_count)

# Matplotlib plot setup
height_ax.set_xlim(0, 1)
height_ax.set_ylim(0, initial_max_height + 0.5)
height_ax.set_title("Popper Motion and Height")
height_ax.axhline(y=0, color='black', linewidth=1)

energy_ax.set_xlim(0, 3)
energy_ax.set_ylim(0, TME)
energy_ax.set_xticks([1, 2])
energy_ax.set_xticklabels(['KE', 'PE'], fontsize=6)  # Smaller font size
energy_ax.set_title("Kinetic and Potential Energy")
ke_bar = energy_ax.bar(1, kinetic_energies[0], color='blue', width=0.4)
pe_bar = energy_ax.bar(2, potential_energies[0], color='green', width=0.4)

image_scaler = 1
# Global lists to store the current values for the 5 heights
height_ke_pe_lists = [[] for _ in range(10)]  # Initialize 5 empty lists

def update(frame):
    """
    Update function for the animation. Dynamically adjusts the image position and plot scaling.
    """
    global kinetic_energies, potential_energies, heights
    global height_ke_pe_lists  # Use the global lists

    # Get 5 evenly spaced heights
    selected_heights = heights[::len(heights)//10]  # 5 evenly spaced heights

    # Retrieve corresponding KE and PE values
    selected_ke = [kinetic_energies[np.where(heights == h)[0][0]] for h in selected_heights]
    selected_pe = [potential_energies[np.where(heights == h)[0][0]] for h in selected_heights]

    # Update the global lists dynamically for the current values
    for i in range(10):
        # Overwrite each list with the latest (height, KE, PE) tuple
        height_ke_pe_lists[i] = [selected_heights[i], selected_ke[i], selected_pe[i]]
    for i, data in enumerate(height_ke_pe_lists):
        height, ke, pe = data
        print(f"Height {i+1}: {height:.2f} m, KE: {ke:.2f} J, PE: {pe:.2f} J")
    print(height_ke_pe_lists[0][1], "\n",height_ke_pe_lists[9])    


    if TME<=1:
        image_scaler = TME*HEIGHT*current_mass**np.log(HEIGHT*TME)
        if image_scaler >=2:
            image_scaler = 2
        if image_scaler<=1:
            image_scaler = TME*HEIGHT*current_mass+1*np.tan(HEIGHT)

    elif TME>=30:
        image_scaler = TME*.3
    elif TME>=1 and TME<=30:
        image_scaler = 1 - (TME - 1) * (0.3 - 30) / (30 - 1)  # Linear interpolation


    if image_scaler>=20:
        image_scaler = 17
    

    current_height = heights[frame]

    # Update the extent of the image
    image_artist.set_extent([
        0.45, 0.55,                # X-coordinates (fixed width)
        current_height - 0.05,     # Bottom Y-coordinate
        current_height + 0.05*(image_scaler)      # Top Y-coordinate
    ])
    #print(image_scaler)

    # Update axis limits dynamically based on user inputs
    height_ax.set_ylim(0, max(heights) + 0.5)
    energy_ax.set_ylim(0, max(TME ,0.01))

    # Update the energy bars
    ke_bar.patches[0].set_height(kinetic_energies[frame])
    pe_bar.patches[0].set_height(potential_energies[frame])

    canvas.draw()  # Redraw the canvas

def draw_matplotlib():
    """
    Convert the Matplotlib figure into a pygame surface.
    """
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()
    size = canvas.get_width_height()
    return pygame.image.frombuffer(raw_data, size, "RGBA")

# Function to render slider values

def format_value(value, unit):
    return f"{value:.4f} {unit}"  # Display values to 4 decimal places

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if slider_mass_x < mouse_x < slider_mass_x + slider_width and slider_mass_y - slider_radius < mouse_y < slider_mass_y + slider_radius:
                is_dragging_mass = True
            if slider_height_x < mouse_x < slider_height_x + slider_width and slider_height_y - slider_radius < mouse_y < slider_height_y + slider_radius:
                is_dragging_height = True

        elif event.type == pygame.MOUSEBUTTONUP:
            is_dragging_mass = is_dragging_height = False

        elif event.type == pygame.MOUSEMOTION:
            if is_dragging_mass:
                mouse_x, _ = pygame.mouse.get_pos()
                mass_position = max(slider_mass_x, min(mouse_x, slider_mass_x + slider_width))
            if is_dragging_height:
                mouse_x, _ = pygame.mouse.get_pos()
                height_position = max(slider_height_x, min(mouse_x, slider_height_x + slider_width))

    # Calculate new mass and height from slider positions
    current_mass = min_mass + (mass_position - slider_mass_x) / slider_width * (max_mass - min_mass)
    current_height = min_height + (height_position - slider_height_x) / slider_width * (max_height - min_height)

    # Update Matplotlib data
    TME, heights, potential_energies, kinetic_energies = update_calculations_and_plot(current_mass, current_height, frame_count)
    update(frame)
    frame = (frame + 1) % frame_count

    # Draw in pygame
    screen.fill(BLACK)

    # Draw sliders
    pygame.draw.rect(screen, GRAY, (slider_mass_x, slider_mass_y - slider_height // 2, slider_width, slider_height))
    pygame.draw.circle(screen, RED, (mass_position, slider_mass_y), slider_radius)
    pygame.draw.rect(screen, GRAY, (slider_height_x, slider_height_y - slider_height // 2, slider_width, slider_height))
    pygame.draw.circle(screen, RED, (height_position, slider_height_y), slider_radius)

    # Draw text
    mass_text = font.render(format_value(current_mass, "kg"), True, WHITE)
    height_text = font.render(format_value(current_height, "m"), True, WHITE)
    screen.blit(mass_text, (slider_mass_x + slider_width + 20, slider_mass_y - slider_radius))
    screen.blit(height_text, (slider_height_x + slider_width + 20, slider_height_y - slider_radius))
    
    # Draw Matplotlib plot
    plot_surface = draw_matplotlib()
    screen.blit(plot_surface, (WIDTH - plot_surface.get_width() - 10, 10))



    # Draw text for chart

    TitleH = font.render("HEIGHT", True, WHITE)
    screen.blit(TitleH, (100,200))
    TitleK = font.render("KE", True, WHITE)
    screen.blit(TitleK, (300,200))
    Titlep = font.render("PE", True, WHITE)
    screen.blit(Titlep, (500,200))
    TME_TEXT = font.render("TME",True, WHITE)
    screen.blit(TME_TEXT, (700,200))
    #Height Text
    H1_Text = font.render(("1: "+format_value(height_ke_pe_lists[0][0], "m")), True, WHITE)
    H2_Text = font.render(("2: "+format_value(height_ke_pe_lists[1][0], "m")), True, WHITE)
    H3_Text = font.render(("3: "+format_value(height_ke_pe_lists[2][0], "m")), True, WHITE)
    H4_Text = font.render(("4: "+format_value(height_ke_pe_lists[3][0], "m")), True, WHITE)
    H5_Text = font.render(("5: "+format_value(height_ke_pe_lists[4][0], "m")), True, WHITE)
    H6_Text = font.render(("6: "+format_value(height_ke_pe_lists[5][0], "m")), True, WHITE)
    H7_Text = font.render(("7: "+format_value(height_ke_pe_lists[6][0], "m")), True, WHITE)
    H8_Text = font.render(("8: "+format_value(height_ke_pe_lists[7][0], "m")), True, WHITE)
    H9_Text = font.render(("9: "+format_value(height_ke_pe_lists[8][0], "m")), True, WHITE)

    #Kinetic Text
    K1_Text = font.render(format_value(height_ke_pe_lists[0][1], "J"), True, WHITE)
    K2_Text = font.render(format_value(height_ke_pe_lists[1][1], "J"), True, WHITE)
    K3_Text = font.render(format_value(height_ke_pe_lists[2][1], "J"), True, WHITE)
    K4_Text = font.render(format_value(height_ke_pe_lists[3][1], "J"), True, WHITE)
    K5_Text = font.render(format_value(height_ke_pe_lists[4][1], "J"), True, WHITE)
    K6_Text = font.render(format_value(height_ke_pe_lists[5][1], "J"), True, WHITE)
    K7_Text = font.render(format_value(height_ke_pe_lists[6][1], "J"), True, WHITE)
    K8_Text = font.render(format_value(height_ke_pe_lists[7][1], "J"), True, WHITE)
    K9_Text = font.render(format_value(height_ke_pe_lists[8][1], "J"), True, WHITE)

    P1_Text = font.render(format_value(height_ke_pe_lists[0][2], "J"), True, WHITE)
    P2_Text = font.render(format_value(height_ke_pe_lists[1][2], "J"), True, WHITE)
    P3_Text = font.render(format_value(height_ke_pe_lists[2][2], "J"), True, WHITE)
    P4_Text = font.render(format_value(height_ke_pe_lists[3][2], "J"), True, WHITE)
    P5_Text = font.render(format_value(height_ke_pe_lists[4][2], "J"), True, WHITE)
    P6_Text = font.render(format_value(height_ke_pe_lists[5][2], "J"), True, WHITE)
    P7_Text = font.render(format_value(height_ke_pe_lists[6][2], "J"), True, WHITE)
    P8_Text = font.render(format_value(height_ke_pe_lists[7][2], "J"), True, WHITE)
    P9_Text = font.render(format_value(height_ke_pe_lists[8][2], "J"), True, WHITE)

    #Height Draw
    screen.blit(H1_Text, (70,230))
    screen.blit(H2_Text, (70,270))
    screen.blit(H3_Text, (70,310))
    screen.blit(H4_Text, (70,350))
    screen.blit(H5_Text, (70,390))
    screen.blit(H6_Text, (70,430))
    screen.blit(H7_Text, (70,470))
    screen.blit(H8_Text, (70,510))
    screen.blit(H9_Text, (70,550))
    
    #Kinetic Text
    screen.blit(K1_Text, (300,230))
    screen.blit(K2_Text, (300,270))
    screen.blit(K3_Text, (300,310))
    screen.blit(K4_Text, (300,350))
    screen.blit(K5_Text, (300,390))
    screen.blit(K6_Text, (300,430))
    screen.blit(K7_Text, (300,470))
    screen.blit(K8_Text, (300,510))
    screen.blit(K9_Text, (300,550))

    #Potential Text
    screen.blit(P1_Text, (500,230))
    screen.blit(P2_Text, (500,270))
    screen.blit(P3_Text, (500,310))
    screen.blit(P4_Text, (500,350))
    screen.blit(P5_Text, (500,390))
    screen.blit(P6_Text, (500,430))
    screen.blit(P7_Text, (500,470))
    screen.blit(P8_Text, (500,510))
    screen.blit(P9_Text, (500,550))

    #TME Text
    TME_TEXTS = font.render(format_value(TME, "J"), True, WHITE)

    screen.blit(TME_TEXTS, (700,230))
    screen.blit(TME_TEXTS, (700,270))
    screen.blit(TME_TEXTS, (700,310))
    screen.blit(TME_TEXTS, (700,350))
    screen.blit(TME_TEXTS, (700,390))
    screen.blit(TME_TEXTS, (700,430))
    screen.blit(TME_TEXTS, (700,470))
    screen.blit(TME_TEXTS, (700,510))
    screen.blit(TME_TEXTS, (700,550))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()

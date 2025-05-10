import pygame
import math
from math import pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
# Initialize Pygame
pygame.init()
# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Click and Drag Rectangle")

# Clock for controlling frame rate
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Use default font, size 36

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
angle =0
hanging_mass_sliderx, hanging_mass_slidery = 300, 600
min_hanging_mass_sliderx = 300
max_hanging_mass_sliderx = 649
slider_massx, slider_massy = 100,600
min_massx = 100
max_massx = 350
slider_radx, slider_rady = 100, 25
slider_radradius = 10
offset_x = 0
offset_y = 0
is_dragging = False
mass_drag = False
hanging_drag = False
MAX_X = 350
min_x = 100
value=0
UPDATE_VALUE_EVENT = pygame.USEREVENT +1
pygame.time.set_timer(UPDATE_VALUE_EVENT, 1)  # 1000 milliseconds = 1 second
def plot_graph(radius_values, velocities):
    """Plot the velocity vs. radius graph."""
    fig, ax = plt.subplots(figsize=(4, 3))  # Adjust the figure size to fit Pygame screen
    ax.plot(radius_values, velocities, label='Velocity vs Radius', color='blue', linewidth=2)
    ax.set_title("Velocity vs Radius")
    ax.set_xlabel("Radius (m)")
    ax.set_ylabel("Velocity (m/s)")
    ax.legend()
    ax.grid(True)
    canvas = FigureCanvas(fig)
    canvas.draw()
    raw_data = canvas.tostring_rgb()
    size = canvas.get_width_height()
    plt.close(fig)  # Close the figure after rendering
    return pygame.image.fromstring(raw_data, size, "RGB")

def calculate_velocities(hanging_massval, mass_val, radius_range):
    """Calculate velocities for a range of radii."""
    velocities = []
    for r in radius_range:
        if r > 0:
            top = 2 * pi * math.sqrt(mass_val * r)
            bottom = math.sqrt(hanging_massval * 9.8)
            time_period = top / bottom if bottom > 0 else 0
            velocity = (2 * pi * r) / time_period if time_period > 0 else 0
            velocities.append(velocity)
        else:
            velocities.append(0)
    return velocities
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if slider_radx-slider_radradius < mouse_x < slider_radx + slider_radradius and slider_rady-slider_radradius < mouse_y < slider_rady + slider_radradius:
                    is_dragging = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - slider_radx
                    offset_y = mouse_y - slider_rady
                if slider_massx-slider_radradius < mouse_x < slider_massx + slider_radradius and slider_massy-slider_radradius < mouse_y < slider_massy + slider_radradius:
                    mass_drag = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - slider_massx
                    offset_y = mouse_y - slider_massy
                if hanging_mass_sliderx-slider_radradius < mouse_x < hanging_mass_sliderx + slider_radradius and hanging_mass_slidery-slider_radradius < mouse_y < hanging_mass_slidery + slider_radradius:
                    hanging_drag = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - hanging_mass_sliderx
                    offset_y = mouse_y - hanging_mass_slidery
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                is_dragging = False
                mass_drag = False
                hanging_drag = False
        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                # Update rectangle position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                slider_radx = mouse_x - offset_x
                if slider_radx > max_massx:
                    slider_radx = max_massx
                elif slider_radx < min_massx:
                    slider_radx = min_massx
            if mass_drag:
                # Update rectangle position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                slider_massx = mouse_x - offset_x
                if slider_massx > MAX_X:
                    slider_massx = MAX_X
                elif slider_massx < min_x:
                    slider_massx = min_x
            if hanging_drag:
                # Update rectangle position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                hanging_mass_sliderx = mouse_x - offset_x
                if hanging_mass_sliderx > max_hanging_mass_sliderx:
                    hanging_mass_sliderx = max_hanging_mass_sliderx
                elif hanging_mass_sliderx < min_hanging_mass_sliderx:
                    hanging_mass_sliderx = min_hanging_mass_sliderx

        #if event.type == UPDATE_VALUE_EVENT:

            #value += .001
    screen.fill("black")  # Clear the screen

    #timers = clock.tick(60) /1000  # Time in seconds since last tick

    g = 9.8  # Gravitational acceleration in m/s^2
    pi = math.pi

    bobradius = (slider_radx-100)

    
    mass_val = (slider_massx-100)/10
    hanging_massval = (hanging_mass_sliderx-299)/10
    circumference = 2*pi*bobradius

    # Calculate time period
    top = 2 * math.pi * math.sqrt(mass_val * bobradius)
    bottom = math.sqrt(hanging_massval * g)
    time_period = top / bottom


    #calculate velocity
    velocity = time_period*circumference
    #calculate angular velocity
    if time_period>0:
        angular_velocity = 2 * math.pi / time_period
    else:
        angular_velocity = 0

    #calculate angle
    angle += angular_velocity * (clock.get_time() / 1000.0)  # Increment angle based on time elapsed

    # Circular motion coordinates
    xs = math.cos(angle)
    ys = math.sin(angle)
    x = bobradius*xs
    y = bobradius*ys





    velocitysq = velocity**2
    pygame.draw.circle(screen, WHITE, (x+350, y+350), mass_val)  # mass moving circle
    pygame.draw.line(screen, WHITE, (350, 350), (x+350,y+350), 2)  # Line connecting mass to center

    pygame.draw.circle(screen, RED, (slider_radx, slider_rady), slider_radradius)  # Slider circle for radius
    pygame.draw.circle(screen, BLUE, (slider_massx, slider_massy), slider_radradius)  # Slider circle for mass of ball
    pygame.draw.circle(screen, "yellow", (hanging_mass_sliderx, hanging_mass_slidery), slider_radradius)  # Slider circle for hanging mass of ball

    #valuep = font.render(f"Value: {value}", True, (255, 255, 255)) # value text
    #screen.blit(valuep, (10, 10))

    massmovings = font.render(str(mass_val), True, BLUE) # movemass slider text
    screen.blit(massmovings, (slider_massx-6, 650))

    radius = font.render(str(bobradius), True, RED)  # Render text for radius
    screen.blit(radius, (slider_radx-6, 50))

    hangingmasse = font.render(str(hanging_massval), True, "yellow")  # Render text for hanging mass
    screen.blit(hangingmasse, (hanging_mass_sliderx-6, 650))
    timetext = font.render("Time: "+str(round(time_period,3)), True, WHITE)  # Render text for time
    screen.blit(timetext, (420, 100))
    veltext = font.render("Velocity: "+str(round(velocity,3)), True, WHITE)  # Render text for vekocity
    screen.blit(veltext, (420, 50))
    angveltext = font.render("Angular Velocity: "+str(round(angular_velocity,3)), True, WHITE)  # Render text for angular velocity
    screen.blit(angveltext, (420, 0))
    hangmasstex = font.render("Hanging Mass", True, "yellow")  # Render text for hangmass
    screen.blit(hangmasstex, (525, 680))
    velocitysqs = font.render("Velocity Squared"+str(round(velocitysq,2)), True, WHITE)  # Render text for hangmass
    screen.blit(velocitysqs, (330, 150))
    mastext = font.render("Mass", True, BLUE)  # Render text for mass
    screen.blit(mastext, (0, 680))
    radtex = font.render("Radius", True, RED)  # Render text for radius
    screen.blit(radtex, (0, 0))
    # Update the display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
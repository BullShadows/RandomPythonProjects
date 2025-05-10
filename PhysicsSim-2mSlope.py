import pygame
import math
from math import pi
# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Click and Drag Rectangle")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Rectangle properties
rect_color = BLUE
rect_x, rect_y = 400, 625
rect_width, rect_height = 50, 50
font = pygame.font.Font(None, 36)  # Use default font, size 36

#slider properties
slider_color = WHITE
slider_x, slider_y = 100, 25
slider_radius = 10
#slider2 properties
slider2_color = WHITE
slider2_x, slider2_y = 400, 25
slider2_radius = 10
#slider3 properties
slider3_color = WHITE
slider3_x, slider3_y = 400, 525
slider3_radius = 10

# Dragging variables
is_dragging = False
is_dragging2 = False
is_dragging3 = False
is_dragging4 = False

offset_x = 0
offset_y = 0
MAX_X = 488
min_x = 399
MAX_X2 = 199
min_x2 = 100
MAX_X3 = 499
min_x3 = 400
MAX_X4 = 500
min_x4 = 400
Massess2 = 300
def rotate_point(cx, cy, x, y, angle):
        # Translate point back to origin
        x -= cx
        y -= cy

        # Rotate point
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)

        # Translate point back
        new_x += cx
        new_y += cy -50 - math.cos(angle_value+2*9999)-5#+ angle_value*(180/pi)+(200+Yval-200)/2
        

        return new_x, new_y

box_width, box_height = 50, 50
box_x, box_y = 50, 150  # Initial position
iscliked = False
isreset = False
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the mouse is over the rectangle
                if rect_x-slider_radius < mouse_x < rect_x + slider_radius and rect_y-slider_radius < mouse_y < rect_y + slider_radius:
                    is_dragging = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - rect_x
                    offset_y = mouse_y - rect_y
                elif slider_x-slider_radius < mouse_x < slider_x + slider_radius and slider_y-slider_radius < mouse_y < slider_y + slider_radius:
                    is_dragging2 = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - slider_x
                    offset_y = mouse_y - slider_y
                elif slider2_x-slider_radius < mouse_x < slider2_x + slider_radius and slider2_y-slider_radius < mouse_y < slider2_y + slider_radius:
                    is_dragging3 = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - slider2_x
                    offset_y = mouse_y - slider2_y
                elif slider3_x-slider_radius < mouse_x < slider3_x + slider_radius and slider3_y-slider_radius < mouse_y < slider3_y + slider_radius:
                    is_dragging4 = True
                    # Calculate offset for smooth dragging
                    offset_x = mouse_x - slider3_x
                    offset_y = mouse_y - slider3_y
                elif 400 < mouse_x < 520 and 300 < mouse_y < 350:
                    iscliked = True
                elif 400 < mouse_x < 520 and 400 < mouse_y < 450:
                    iscliked = False
                    isreset = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                is_dragging = False
                is_dragging2 = False
                is_dragging3 = False
                is_dragging4 = False
                #iscliked = False
                #iscliked = False
        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                # Update rectangle position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                rect_x = mouse_x - offset_x
                if rect_x > MAX_X:
                    rect_x = MAX_X
                elif rect_x < min_x:
                    rect_x = min_x
            elif is_dragging2:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                slider_x = mouse_x - offset_x
                if slider_x > MAX_X2:
                    slider_x = MAX_X2
                elif slider_x < min_x2:
                    slider_x = min_x2
            elif is_dragging3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                slider2_x = mouse_x - offset_x
                if slider2_x > MAX_X3:
                    slider2_x = MAX_X3
                elif slider2_x < min_x3:
                    slider2_x = min_x3
            elif is_dragging4:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                slider3_x = mouse_x - offset_x
                if slider3_x > MAX_X4:
                    slider3_x = MAX_X4
                elif slider3_x < min_x4:
                    slider3_x = min_x4

    # Drawing

    Mass1 = (slider_x - 99) # Slider_x = Mass1
    Mass2 = (slider2_x - 399) # Slider2_x = Mass2
    Angle = (rect_x - 399) # Rect_x = Angle
    Friction = (slider3_x - 400)/100 # Slider3_x = Friction
    Mass1_Scaler = (Mass1)/10/5
    Mass2_Scaler = Mass2+1/100
    screen.fill("black")  # Clear the screen
    #pygame.draw.arc(screen, WHITE, [350, 100, 110, 20], pi/10, pi, 2)
    pygame.draw.line(screen, WHITE, (330, Massess2), (330,175), 2)  # Line connecting box2 to pulley
    Masses1 = 50
    Yval =200
    pygame.draw.circle(screen, WHITE, (330, 175), 30)  # Pulley
    #pygame.draw.rect(screen, "blue", [Masses1, 150+Angle, 50, 50]) # Box 1
    #pygame.draw.polygon(screen, WHITE, [[50+Angle, 200+Angle], [100-Angle, 200-Angle], [100-Angle, 150-Angle], [50-Angle, 150-Angle]])  # Static polygon
    # Sliders
    pygame.draw.rect(screen, BLUE, (100, 15, 110, 20))  # Mass 1 rectangle
    pygame.draw.rect(screen, RED, (400, 15, 110, 20))  # Mass 2 rectangle
    pygame.draw.rect(screen, "grey", (400, 615, 100, 20))  # Angle rectangle
    pygame.draw.rect(screen, "grey", (400, 515, 110, 20))  # Friction rectangle
    pygame.draw.circle(screen, WHITE, (slider_x, slider_y), slider_radius)  # Slider circle for m1
    pygame.draw.circle(screen, WHITE, (rect_x, rect_y), slider_radius) # Slider for m2
    pygame.draw.circle(screen, WHITE, (slider2_x, slider2_y), slider_radius)  # Slider circle for angle
    pygame.draw.circle(screen, WHITE, (slider3_x, slider3_y), slider_radius)  # Slider circle for angle

    # Draw text
    text_surface = font.render(str(Mass1), True, WHITE)  # Render text
    screen.blit(text_surface, (slider_x-6, 50))  # Draw text at position (50, 50) Mass1
    text_surface2 = font.render(str(Angle), True, WHITE)  # Render text
    screen.blit(text_surface2, (rect_x-6, rect_y+25))  # Draw text at position (50, 50)
    text_surface3 = font.render(str(Mass2), True, WHITE)  # Render text
    screen.blit(text_surface3, (slider2_x-6, slider2_y+25))  # Draw text at position (50, 50)
    text_surface4 = font.render(str(Friction), True, WHITE)  # Render text
    screen.blit(text_surface4, (slider3_x-6, slider3_y+25))  # Draw text at position (50, 50)
    #Slider names
    Mass1 = font.render("Mass 1", True, WHITE)  # Render text
    screen.blit(Mass1, (120, 0))  # Draw text at position (50, 50)
    Mass2 = font.render("Mass 2", True, WHITE)  # Render text
    screen.blit(Mass2, (420, 0))  # Draw text at position (50, 50)
    Angle = font.render("Angle", True, WHITE)  # Render text
    screen.blit(Angle, (415, 575))  # Draw text at position (50, 50)
    Friction = font.render("Friction", True, WHITE)  # Render text
    screen.blit(Friction, (400, 475))  # Draw text at position (50, 50)
    # Math
    # Math
    angle_value = (rect_x - 399) * (pi / 180)  # Convert the slider value to radians
    mass1_value = (slider_x - 99)
    mass2_value = (slider2_x - 399)
    friction_value = (slider3_x - 400) / 100
    if angle_value != 0:
        zz = math.tan(angle_value)
        newthingy = 305*zz
        Yval=Yval+newthingy
    else:
        Yval=200
    pygame.draw.polygon(screen, WHITE, [[0, 700], [305, 700], [305, 200], [0, Yval]])  # Static polygon

    if Angle != 0:
        g = 9.81
        sins = math.sin(angle_value)
        coss = math.cos(angle_value)
        fric = (friction_value * mass1_value * g) * coss
        othersin = (mass1_value * g) * sins
        top = mass2_value * g - fric - othersin
        a = top / (mass1_value + mass2_value)
    if Angle == 0:
        a = (g(mass2_value - friction_value*mass1_value))/(mass1_value+mass2_value)
    
    

    #Mass Hanging distance

        #Time
    if a<0:
        t=0
        a=0
    elif a>0:
        ax=(2*350)/a
        t=math.sqrt(ax)
        Velocity = a*t
    time_text = f"Time: {t:.5f}"
    Time = font.render(time_text, True, WHITE)  # Render text
    screen.blit(Time, (400, 150))  # Draw text at position (50, 50)
    acceleration_text = f"Acceleration: {a:.5f}"
    velocity_text = f"Velocity: {Velocity:.5f}"

    Acceleration = font.render(acceleration_text, True, WHITE)  # Render text
    screen.blit(Acceleration, (400, 100))  # Draw text at position (50, 50)
    Velocitys = font.render(velocity_text, True, WHITE)  # Render text
    screen.blit(Velocitys, (400, 200))  # Draw text at position (50, 50)
    Distances = font.render("Distance: 350", True, WHITE)  # Render text
    screen.blit(Distances, (400, 250))  # Draw text at position (50, 50)
    # Calc velocity
    pygame.draw.rect(screen, "red", (400, 400, 110, 50))  # Mass 1 rectangle
    end = font.render(" End", True, "black")  # Render text
    screen.blit(end, (425, 415))  # Draw text at position (50, 50)

    pygame.draw.rect(screen, "yellow", (400, 300, 110, 50))  # Mass 1 rectangle
    start = font.render("Start", True, "black")  # Render text
    screen.blit(start, (425, 315))  # Draw text at position (50, 50)
    dt = clock.tick(60) /10  # Time in seconds since last tick
    if iscliked:  # Use if statement instead of while loop
        if Massess2 < 650:  # Only increment if Massess2 has not reached 650
            Massess2 += a * dt
    pygame.draw.rect(screen, "red", [305, Massess2, 50, 50])  # Box 2
    if isreset:
        Massess2 = 300
        isreset = False
    ground_start = (305, 200)
    ground_end = (0, Yval)
    
    slope_angle = math.atan2(ground_end[1] - ground_start[1], ground_end[0] - ground_start[0])

    # Calculate the center of the box
    box_center_x = box_x + box_width / 2
    box_center_y = box_y + box_height / 2

    # Calculate the four corners of the box
    top_left = (box_x, box_y)
    top_right = (box_x + box_width, box_y)
    bottom_left = (box_x, box_y + box_height)
    bottom_right = (box_x + box_width, box_y + box_height)

    # Rotate each corner of the box to align with the slope
    rotated_top_left = rotate_point(box_center_x, box_center_y, *top_left, slope_angle)
    rotated_top_right = rotate_point(box_center_x, box_center_y, *top_right, slope_angle)
    rotated_bottom_left = rotate_point(box_center_x, box_center_y, *bottom_left, slope_angle)
    rotated_bottom_right = rotate_point(box_center_x, box_center_y, *bottom_right, slope_angle)


    pygame.draw.line(screen, WHITE, (rotated_bottom_left[0],rotated_bottom_left[1]+25), (350,175), 2)  # Line connecting box to pulley

    y2 = ground_end[1]
    y1 = ground_start[1]
    x1 = ground_start[0]
    x2 = ground_end[0]
    helps = math.cos(slope_angle)
    m = (y2 - y1) / (x2 - x1)  # Slope of the line
    b = y1 - m * x1  # y-intercept
    box_y = m * box_x + b
    pygame.draw.polygon(screen, BLUE, [rotated_top_left, rotated_top_right, rotated_bottom_right, rotated_bottom_left])



    # Update the display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()




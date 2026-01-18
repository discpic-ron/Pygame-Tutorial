import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Mouse Events Demo")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Variables to store mouse state
mouse_pos = (0, 0)
left_button_pressed = False
right_button_pressed = False

# Font for displaying text
font = pygame.font.Font(None, 36)

def draw_text(text, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Main game loop
running = True
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse button pressed down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left button
                left_button_pressed = True
                print(f"Left button down at {event.pos}")
            elif event.button == 3: # Right button
                right_button_pressed = True
                print(f"Right button down at {event.pos}")
            elif event.button == 4: # Mouse wheel up
                print(f"Mouse wheel up at {event.pos}")
            elif event.button == 5: # Mouse wheel down
                print(f"Mouse wheel down at {event.pos}")

        # Mouse button released
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Left button
                left_button_pressed = False
                print(f"Left button up at {event.pos}")
            elif event.button == 3: # Right button
                right_button_pressed = False
                print(f"Right button up at {event.pos}")

        # Mouse moved
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            # print(f"Mouse moved to {event.pos}") # Uncomment for lots of output

    # Alternative way to get current mouse state without event loop
    # mouse_pos = pygame.mouse.get_pos()
    # mouse_pressed = pygame.mouse.get_pressed()
    # if mouse_pressed[0]: # Check if left button is held down
    #     left_button_pressed = True # Note: get_pressed() state persists across frames

    # Drawing
    screen.fill(BLACK) # Fill the screen with black

    # Display current mouse position
    draw_text(f"Mouse Pos: {mouse_pos}", WHITE, screen, 10, 10)
    
    # Display button status
    left_status = "Pressed" if left_button_pressed else "Released"
    right_status = "Pressed" if right_button_pressed else "Released"
    draw_text(f"Left Button: {left_status}", GREEN if left_button_pressed else RED, screen, 10, 50)
    draw_text(f"Right Button: {right_status}", GREEN if right_button_pressed else RED, screen, 10, 90)

    # Draw a circle at the mouse position
    pygame.draw.circle(screen, BLUE, mouse_pos, 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

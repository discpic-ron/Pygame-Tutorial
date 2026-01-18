import pygame
import sys

# 1. SETUP
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    # 2. INPUT (The Event Loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. UPDATE (Game Logic)
    # This is where physics and math go

    # 4. DRAW (Rendering)
    screen.fill((30, 30, 30)) # Clear screen with dark grey
    pygame.display.flip()     # Update the monitor
    
    clock.tick(60) # Maintain 60 Frames Per Second

pygame.quit()
sys.exit()

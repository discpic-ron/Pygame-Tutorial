import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lesson 2: Drawing module")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")

    # 1. DRAW A RECTANGLE (Filled)
    # pygame.draw.rect(surface, color, (x, y, width, height))
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # 2. DRAW A CIRCLE (Outline only)
    # pygame.draw.circle(surface, color, (center_x, center_y), radius, width)
    pygame.draw.circle(screen, "blue", (400, 300), 50, 5)

    # 3. DRAW A LINE
    # pygame.draw.line(surface, color, start_pos, end_pos, width)
    pygame.draw.line(screen, "green", (0, 0), (800, 600), 10)

    # 4. DRAW A POLYGON (Triangle)
    # Takes a list of points
    points = [(600, 100), (700, 200), (500, 200)]
    pygame.draw.polygon(screen, "purple", points)

    pygame.display.flip()

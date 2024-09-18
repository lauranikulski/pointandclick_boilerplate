# pipenv install pygame (to install pygame with pipenv functionality)
# pipenv shell (to activate virtual environment)

import pygame
import sys
from pygame.locals import *

pygame.init()

# Set the size of the game window full screen to play
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

DISPLAYSURF = pygame.display.set_mode((600,600))

pygame.display.set_caption("Haunted House on the beach")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Clear the screen
    screen.fill((0, 0, 0)) # burgundy red colour 
    
    # Update the game state
    
    # Draw the screen
    pygame.display.update()
    pygame.display.flip()


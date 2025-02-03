import pygame
import json
import objects
import os

# Intilaize Pygame
pygame.init()
running = True

# Set The Screen Size
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen_size = (1920, 1080) 
offset = screen_width / screen_size[0]
print(offset)

default_screen_size = (int((screen_size[0] * .9 * offset) - (screen_size[0] * .9 * offset) % (40 * offset)), int(screen_size[1] * .9 * offset))
screen = pygame.display.set_mode(default_screen_size)
print(default_screen_size)

# Main Loop
while running:
    # Check for Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Set The Background
    base_Path = base_path = os.path.dirname(__file__)
    image = pygame.image.load(os.path.join(base_path, r"menu_Images\menu_Background.png"))
    image = pygame.transform.scale(image, (default_screen_size[0], default_screen_size[1]))
    screen.blit(image, (0, 0)) 

    for x in range(30,39):
        image = pygame.image.load(os.path.join(base_path, fr"menu_Images\Group {x}.png"))
        screen.blit(image, (0, 0)) 
        pygame.display.flip() 
        pygame.time.delay(50)



pygame.quit()
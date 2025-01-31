import pygame
import json
import objects

# Initialize Pygame and Screen
pygame.init()
clock = pygame.time.Clock()

screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen_size = (1920, 1080) 
offset = screen_width / screen_size[0]
print(offset)

default_screen_size = (screen_size[0] * .9 * offset, screen_size[1] * .9 * offset)
screen = pygame.display.set_mode(default_screen_size)

#1728, 972
running = True
fullscreen = False

# Grid Size
tilesWide = 300
tilesHeight = 20

#Creates An Empty Grid
def create_Empty_Grid():
    grid = []
    for x in range(tilesHeight):
        current = []
        for y in range(tilesWide):
            current.append("empty")
        grid.append(current)  
    return grid  

#Saves A Grid To A Json File
def Saved_Grid(grid, filename):
    with open(f"{filename}.json", "w") as file:
        json.dump(grid, file)

# Loads A Grid From A Json File
def load_grid(filename):
    with open(f"{filename}.json", "r") as file:
        return json.load(file)

current_Grid = create_Empty_Grid()

#Turn The Grid Into Objects
grid_Blocks = []
current_Row = 0
current_Column = 0
grid_Size = 40 * offset
for x in current_Grid:
    current_Column = 0
    row_Add = []
    for y in x:
        current_Object = objects.block(y, grid_Size, current_Column*grid_Size, current_Row*grid_Size)
        row_Add.append([current_Object[0], current_Object[1]])
        current_Column += 1
    grid_Blocks.append(row_Add)
    current_Row += 1

# Sets Up The Camera
camera_x = 0
camera_speed = int(20 * offset)
keys = {"left": False, "right":False}

# Main Loop
while running:
    
    screen.fill((255, 255, 255))

    # Check For Inputs
    for event in pygame.event.get():
        
        # Check for Quit
        if event.type == pygame.QUIT:
            running = False

        # Check for Fullscreen 
        """if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN | pygame.NOFRAME)
            else:
                screen = pygame.display.set_mode(default_screen_size, pygame.RESIZABLE)"""
        
        # Check To See If User Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_Scalling = int(grid_Size)
                mouse_Column, mouse_Row = event.pos  
                mouse_Column += camera_x
                print(f"Mouse clicked at: ({mouse_Column//mouse_Scalling}, {mouse_Row//mouse_Scalling})")
                grid_Blocks[mouse_Row//mouse_Scalling][mouse_Column//mouse_Scalling] = objects.block("brick", mouse_Scalling, mouse_Column//mouse_Scalling*mouse_Scalling, mouse_Row//mouse_Scalling*mouse_Scalling)

        # Ajust the camera
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys["left"] = True
            elif event.key == pygame.K_RIGHT:
                keys["right"] = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            elif event.key == pygame.K_RIGHT:
                keys["right"] = False

    # Create Grid
    for row in range(tilesHeight):
        for col in range(tilesWide):
            screen.blit(grid_Blocks[row][col][0], 
            (grid_Blocks[row][col][1].x - camera_x, grid_Blocks[row][col][1].y))

    # Moves The Camera
    if keys["left"] and keys["right"]:
        continue
    elif keys["left"]:
        if camera_x >= camera_speed:
            camera_x -= camera_speed
        elif camera_x < camera_speed and camera_x > 0:
            camera_x = 0
    elif keys["right"]:
        camera_x += camera_speed

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
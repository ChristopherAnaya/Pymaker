import pygame
import json
import objects

# Initialize Pygame and Screen
pygame.init()
clock = pygame.time.Clock()

screen_size = (1920, 1080) 
default_screen_size = (screen_size[0] * .9, screen_size[1] * .9)
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
current_Grid[0][0] = "brick"
current_Grid[9][29] = "brick"
current_Grid[9][9] = "brick"
current_Grid[5][19] = "brick"

#turn the grid into objects
grid_Blocks = []
current_Row = 0
current_Column = 0
grid_Size = 40
for x in current_Grid:
    current_Column = 0
    row_Add = []
    for y in x:
        current_Object = objects.block(y, grid_Size, current_Column*grid_Size, current_Row*grid_Size)
        row_Add.append([current_Object[0], current_Object[1]])
        current_Column += 1
    grid_Blocks.append(row_Add)
    current_Row += 1

# Main Loop
while running:
    
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_Column, mouse_Row = event.pos  
                print(f"Mouse clicked at: ({mouse_Column//40}, {mouse_Row//40})")
                grid_Blocks[mouse_Row//40][mouse_Column//40] = objects.block("brick", 40, mouse_Column//40*40, mouse_Row//40*40)


    screen.fill((255, 255, 255))

    
    



    # Create Grid
    for row in range(tilesHeight):
        for col in range(tilesWide):
            screen.blit(grid_Blocks[row][col][0], grid_Blocks[row][col][1])

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
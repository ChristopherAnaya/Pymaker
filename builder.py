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

# Set The Grid Size
grid_Size = int(40 * offset)

default_screen_size = (int((screen_size[0] * .9 * offset) - (screen_size[0] * .9 * offset)%40), int(screen_size[1] * .9 * offset))
screen = pygame.display.set_mode(default_screen_size)
print(default_screen_size)
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
current_Grid[0][299] = "red"

#Turn The Grid Into Objects
grid_Blocks = []
current_Row = 0
current_Column = 0
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
camera_speed = int(40 * offset)
keys = {"left": False, "right":False}

# Sets Up The Hotbar
hotbar = objects.hotbar(offset, default_screen_size[0], default_screen_size[1])
current_Block = "red"

# Main Loop
while running:
    
    screen.fill((255, 255, 255))

    # Check For Inputs
    for event in pygame.event.get():
        
        # Check for Quit
        if event.type == pygame.QUIT:
            running = False
        
        # Check To See If User Clicked
    mouse_buttons = pygame.mouse.get_pressed()
    
    if mouse_buttons[0]:
        if event.button == 1: 
            mouse_Column, mouse_Row = pygame.mouse.get_pos()  
            mouse_Column += camera_x
            if mouse_Row < grid_Size * tilesHeight:
                print(f"Mouse clicked at: ({mouse_Column//grid_Size}, {mouse_Row//grid_Size})")
                grid_Blocks[mouse_Row//grid_Size][mouse_Column//grid_Size] = objects.block(current_Block, grid_Size, mouse_Column//grid_Size*grid_Size, mouse_Row//grid_Size*grid_Size)
            else:
                for item in hotbar:
                    if mouse_Column > item[1].x and mouse_Column < item[1].x + item[1].width and mouse_Row > item[1].y and mouse_Row < item[1].y + item[1].height:
                        print(f"color now {item[2][:-4]}")
                        current_Block = item[2][:-4]
                        break
  
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

    # Creates The Hotbar
    for item in hotbar:
        screen.blit(item[0], item[1])
        if item[2][:-4] == current_Block:
            pygame.draw.rect(screen, (140, 140, 140), item[1], 10)
        else:
            pygame.draw.rect(screen, (60, 60, 60), item[1], 10)

    # Moves The Camera
    if keys["left"] and keys["right"]:
        continue
    elif keys["left"]:
        if camera_x >= camera_speed:
            camera_x -= camera_speed
        elif camera_x < camera_speed and camera_x > 0:
            camera_x = 0
    elif keys["right"]:
        if camera_x <= (tilesWide * grid_Size) -  default_screen_size[0] - camera_speed:
            camera_x += camera_speed
        elif camera_x > (tilesWide * grid_Size) - default_screen_size[0] - camera_speed and camera_x < (tilesWide * grid_Size) -  default_screen_size[0]:
            camera_x = (tilesWide * grid_Size) -  default_screen_size[0]

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
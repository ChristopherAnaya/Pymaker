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
            current.append("brick")
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

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y  
        self.width = 50
        self.height = 50
        self.color = (0, 0, 255)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

player_obj = player(375, 275)


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

    screen.fill((0, 0, 0))

    # Player Logic
    keys = pygame.key.get_pressed()
    player_obj.move(keys)
    player_obj.draw(screen)

    # Create Grid
    current_Row = 0
    current_Column = 0
    grid_Size = 40
    for x in current_Grid:
        current_Column = 0
        for y in x:
            if y == "brick":
                current_Object = objects.block(y, grid_Size, current_Column*grid_Size, current_Row*grid_Size)
                screen.blit(current_Object[0], current_Object[1])
            current_Column += 1
        current_Row += 1

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
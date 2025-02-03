import pygame
import json
import objects
before = False
running = True
pygame.init()
clock = pygame.time.Clock()

screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen_size = (1920, 1080) 
offset = screen_width / screen_size[0]
print(offset)

# Set The Grid Size
grid_Size = int(40 * offset)

default_screen_size = (int((screen_size[0] * .9 * offset) - (screen_size[0] * .9 * offset) % grid_Size), int(screen_size[1] * .9 * offset))
screen = pygame.display.set_mode(default_screen_size)
print(default_screen_size)

# Load The World
def load_grid(filename):
    with open(f"{filename}.json", "r") as file:
        return json.load(file)
    
world_Current = load_grid("test")

grid_Blocks = []
current_Row = 0
current_Column = 0
for x in world_Current:
    current_Column = 0
    row_Add = []
    for y in x:
        current_Object = objects.block(y, grid_Size, current_Column*grid_Size, current_Row*grid_Size)
        row_Add.append([current_Object[0], current_Object[1]])
        current_Column += 1
    grid_Blocks.append(row_Add)
    current_Row += 1

tilesWide = 300
tilesHeight = 20

gravity = .1

player_Speed_X = 2

player_Speed_Y = 0

# Player Spawn
spawn_y = -5
for x in world_Current:
    if x[0] != "empty":
        break
    spawn_y += 1

player = objects.player("idle", grid_Size, 0, spawn_y * grid_Size)

keys = {"left": False, "right": False}

# Main Loop
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create Grid
    for row in range(tilesHeight):
        for col in range(tilesWide):
            screen.blit(grid_Blocks[row][col][0], grid_Blocks[row][col][1])

    keys_pressed = pygame.key.get_pressed()
    keys["left"] = keys_pressed[pygame.K_a]
    keys["right"] = keys_pressed[pygame.K_d]
    if keys_pressed[pygame.K_SPACE]:
        if before == False:
            player_Speed_Y -= 4.5
            before = True


    if keys["left"] and keys["right"]:
        pass
    elif keys["left"]:
        if world_Current[player[1].y // grid_Size][int(player[1].x - player_Speed_X) // grid_Size] == "empty":
            player[1].x -= player_Speed_X
    elif keys["right"]:
        if world_Current[player[1].y // grid_Size][int(player[1].x + player_Speed_X + grid_Size) // grid_Size] == "empty":
            player[1].x += player_Speed_X

    player[1].y += player_Speed_Y

    if world_Current[int(player[1].y + grid_Size + player_Speed_Y) // grid_Size][player[1].x // grid_Size] == "empty":
        player_Speed_Y += gravity
    else:
        player_Speed_Y = 0
        before = False
    print(world_Current[int(player[1].y + grid_Size + player_Speed_Y) // grid_Size][player[1].x // grid_Size], [int(player[1].y + grid_Size + player_Speed_Y) // grid_Size],[player[1].x // grid_Size])


    screen.blit(player[0], player[1])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
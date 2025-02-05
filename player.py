import pygame
import json
import objects
import animations
pygame.font.init()
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

gravity = 2 * offset

player_Speed_Y = 0

walking_Frames = 0
walking = False
direction = "right"
frame_Speed = 10

# Player Spawn
spawn_y = -1
for x in world_Current:
    if x[0] != "empty":
        break
    spawn_y += 1

player = objects.player("idle", grid_Size, 0, spawn_y * grid_Size)

keys = {"left": False, "right": False, "shift":False, "space":False}
jumping = False
font = pygame.font.SysFont("Arial", 30)

space_held = True
able_Jump = True
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
    keys["shift"] = keys_pressed[pygame.K_LSHIFT]
    keys["space"] = keys_pressed[pygame.K_SPACE]
    if keys_pressed[pygame.K_SPACE]:
        if jumping == False and space_held == False:
            player_Speed_Y -= 12 * offset
            jumping = True
            space_held = True
            gained_height = 0
    else:
        space_held = False
    if space_held == False and jumping == True or jumping == True and gained_height >= 3.5 * grid_Size:
        player_Speed_Y += gravity
        if player_Speed_Y > 12 * offset:
            player_Speed_Y = 12 * offset

    if keys["shift"]:
        player_Speed_X = 8 * offset
    else:
        player_Speed_X = 4 * offset
    
    if keys["left"] and keys["right"]:
        pass
    elif keys["left"]:
        if world_Current[player[1].y // grid_Size][int(player[1].x - player_Speed_X) // grid_Size] == "empty" and world_Current[(player[1].y + grid_Size - 1) // grid_Size][int(player[1].x - player_Speed_X) // grid_Size] == "empty":
            player[1].x -= player_Speed_X
            walking = True
            direction = "left"
        elif player[1].x % grid_Size != 0:
            player[1].x -= player[1].x % grid_Size
            walking = True
            direction = "left"
        else:
            walking = False
            walking_Frames = 0
            direction = "left"
    elif keys["right"]:
        if world_Current[player[1].y // grid_Size][int(player[1].x + player_Speed_X + grid_Size - 1) // grid_Size] == "empty" and world_Current[(player[1].y + grid_Size - 1) // grid_Size][int(player[1].x + player_Speed_X + grid_Size - 1) // grid_Size] == "empty":
            player[1].x += player_Speed_X
            walking = True
            direction = "right"
        elif player[1].x % grid_Size != 0:
            player[1].x += grid_Size - player[1].x % grid_Size
            walking = True
            direction = "right"
        else:
            walking = False
            walking_Frames = 0
            direction = "right"
    else:
        walking = False
        walking_Frames = 0

    if walking == True:
        walking_Frames = (walking_Frames + 1) % (frame_Speed * 3)
        player = animations.walking(f"walking_{walking_Frames//frame_Speed + 1}", grid_Size, player[1].x, player[1].y)
    else:
        player = objects.player("idle", grid_Size, player[1].x, player[1].y)
    screen.blit(pygame.transform.flip(player[0], (True if direction == "left" else False) ,False), player[1])
    
    if jumping:
        if world_Current[int((player[1].y + player_Speed_Y)//grid_Size + 1)][player[1].x//grid_Size] == "empty" and world_Current[int((player[1].y + player_Speed_Y)//grid_Size + 1)][(player[1].x + grid_Size - 1)//grid_Size] == "empty":
            player[1].y += player_Speed_Y
            if gained_height < 3.5 * grid_Size:
                gained_height -= player_Speed_Y
        elif player[1].y % grid_Size != 0:
            player_Speed_Y = 0
            jumping = False
            able_Jump = True
            player[1].y += grid_Size - player[1].y % grid_Size
        else:
            player_Speed_Y = 0
            jumping = False
            able_Jump = True
    else:
        if world_Current[int((player[1].y + player_Speed_Y)//grid_Size + 1)][player[1].x//grid_Size] == "empty" and world_Current[int((player[1].y + player_Speed_Y)//grid_Size + 1)][(player[1].x + grid_Size - 1)//grid_Size] == "empty":
            player[1].y += player_Speed_Y
            player_Speed_Y += gravity
            able_Jump = False
        else:
            player_Speed_Y = 0
            able_Jump = True
        
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (0, 0, 0))  
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
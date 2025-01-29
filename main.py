import pygame

# Initialize Pygame and Screen
pygame.init()
clock = pygame.time.Clock()

screen_size = (1920, 1080) 
default_screen_size = (screen_size[0] * .9, screen_size[1] * .9)
screen = pygame.display.set_mode(default_screen_size)
#1728, 972
running = True
fullscreen = False

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN | pygame.NOFRAME)
            else:
                screen = pygame.display.set_mode(default_screen_size, pygame.RESIZABLE)

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    
    player_obj.move(keys)
    
    player_obj.draw(screen)

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
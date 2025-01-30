import pygame
def block(type, length, x, y):
    sprite = pygame.image.load(fr"C:\Users\canay353\Documents\GitHub\Pymaker\object_Images\{type}.png")
    sprite = pygame.transform.scale(sprite, (length, length))
    block_rect = sprite.get_rect()
    block_rect.topleft = (x, y)
    return sprite, block_rect
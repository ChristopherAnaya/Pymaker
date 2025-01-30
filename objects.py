import pygame
import os
print(os.path.dirname(__file__))
def block(type, length, x, y):
    base_path = os.path.dirname(__file__)  
    image_path = os.path.join(base_path, "object_Images", f"{type}.png")
    sprite = pygame.image.load(image_path)
    sprite = pygame.transform.scale(sprite, (length, length))
    block_rect = sprite.get_rect()
    block_rect.topleft = (x, y)
    return sprite, block_rect
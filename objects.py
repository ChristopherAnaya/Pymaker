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

def hotbar(offset, width, height):
    base_path = os.path.dirname(__file__)  
    image_path = os.path.join(base_path, "object_Images")
    images = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
    for_Range = 12 if len(images) > 12 else len(images)
    final = []
    print(height, offset)
    for i in range(for_Range):
        image = pygame.image.load(os.path.join(image_path, images[i]))
        image = pygame.transform.scale(image, (100*offset, 100*offset))
        image_rect = image.get_rect()
        image_rect.topleft = ((width - 1200 * offset)/2 + i * 100 * offset, 20 * 40 * offset + (height - (20 * 40 * offset) - 100 * offset)/2)
        final.append([image, image_rect, images[i]])
    return final
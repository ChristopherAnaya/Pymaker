import os
import pygame

base_path = os.path.dirname(__file__)

def walking(type, length, x, y): 
    image_path = os.path.join(base_path, "animation_Images", f"{type}.png")
    sprite = pygame.image.load(image_path)
    sprite = pygame.transform.scale(sprite, (length, length))
    block_rect = sprite.get_rect()
    block_rect.topleft = (x, y)
    return sprite, block_rect

def question_block_static(frame, x, y, length):
    if frame < 18:
        image_path = os.path.join(base_path, r"animation_Images", "question_1.png")
    elif frame < 28:
        image_path = os.path.join(base_path, r"animation_Images", "question_2.png")
    elif frame < 36:
        image_path = os.path.join(base_path, r"animation_Images", "question_3.png")
    else:
        image_path = os.path.join(base_path, r"animation_Images", "question_2.png")
    sprite = pygame.image.load(image_path)
    sprite = pygame.transform.scale(sprite, (length, length))
    block_rect = sprite.get_rect()
    block_rect.topleft = (x, y)
    return sprite, block_rect
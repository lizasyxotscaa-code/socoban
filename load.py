import pygame
from script import load_image
player_images = {'right': load_image('assets/images/player/right'),
                 'left': load_image('assets/images/player/left'),
                 'up': load_image('assets/images/player/up'),
                 'down': load_image('assets/images/player/down')}

wall_image = pygame.image.load('assets/images/blocks/block.png').convert_alpha()
wall_2_image = pygame.image.load('assets/images/blocks/block_2.png').convert_alpha()

crate_image = pygame.image.load('assets/images/blocks/crate.png').convert_alpha()
crate_green_image = pygame.image.load('assets/images/blocks/crate (2).png').convert_alpha()

monetka_image = pygame.image.load('assets/images/blocks/environment.png').convert_alpha()

ground_image = pygame.image.load('assets/images/blocks/ground.png').convert_alpha()
ground_2_image = pygame.image.load('assets/images/blocks/ground_1.png').convert_alpha()

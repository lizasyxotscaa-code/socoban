import pygame
import sys
from sprites.sprite_classes import *


BLACK = (0, 0, 0)
WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Socoban")
clock = pygame.time.Clock()


from load import *

def restart():
    global block_group, gravel_group, gr_crate_group, ye_crate_group, \
        monetka_group, goal_group, player_group, collision_sprites, all_sprites, \
        player

    block_group = pygame.sprite.Group()
    gravel_group = pygame.sprite.Group()
    gr_crate_group = pygame.sprite.Group()
    ye_crate_group = pygame.sprite.Group()
    monetka_group = pygame.sprite.Group()
    goal_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()


def lvlGame():
    global block_group, gravel_group, gr_crate_group, ye_crate_group, \
        monetka_group, goal_group, player_group, all_sprites, player

    block_group.draw(sc)
    gravel_group.draw(sc)
    gr_crate_group.draw(sc)
    ye_crate_group.draw(sc)
    monetka_group.draw(sc)
    goal_group.draw(sc)
    player_group.draw(sc)

    block_group.update()
    gravel_group.update()
    gr_crate_group.update()
    ye_crate_group.update()
    monetka_group.update()
    goal_group.update()
    player_group.update(dt, FPS, player_images)

    player = Player(player_images['down'][0], (180, 300), collision_sprites)
    player_group.add(player)

    pygame.display.update()

def drawMap(mapFile):
    global block_group, gravel_group, gr_crate_group, ye_crate_group, \
        monetka_group, goal_group, player_group, collision_sprites, all_sprites, \
        player
    game_map = []

    with open(mapFile, 'r') as file:
        for i in range(10):
            game_map.append(file.readline().replace('\n', '').split(','))

        pos = [0, 0]
        for i in range(10):
            pos[1] = i * 60
            for j in range(10):
                pos[0] = j * 60
                if game_map[i][j] == '7':
                    block = Block(wall_2_image, pos)
                    block_group.add(block)
                    all_sprites.add(block)
                elif game_map[i][j] == '8':
                    ye_crate = Ye_crate(crate_image, pos)
                    ye_crate_group.add(ye_crate)
                    all_sprites.add(ye_crate)
                elif game_map[i][j] == '9':
                    gr_crate = Gr_crate(crate_green_image, pos)
                    gr_crate_group.add(gr_crate)
                    all_sprites.add(gr_crate)
                elif game_map[i][j] == '10':
                    monetka = Monetka(monetka_image, pos)
                    monetka_group.add(monetka)
                    all_sprites.add(monetka)
                elif game_map[i][j] == '11':
                    gravel = Gravel(ground_image, pos)
                    gravel_group.add(gravel)
                    all_sprites.add(gravel)
                elif game_map[i][j] == '12':
                    goal = Goal(ground_2_image, pos)
                    goal_group.add(goal)
                    all_sprites.add(goal)

restart()
drawMap('game_lvl/socoban0_Слой_тайлов_2.csv')
drawMap('game_lvl/socoban0_Слой_тайлов_1.csv')



# all_sprites.add(player)


while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    sc.fill(BLACK)
    lvlGame()




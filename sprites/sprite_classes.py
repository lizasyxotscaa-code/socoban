import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]




class Gravel(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]




class Gr_crate(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Ye_crate(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Goal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



# class Player(pygame.sprite.Sprite):
#     def __init__(self, images, pos):
#         super().__init__()
#         self.images = images
#         self.frame = 0
#         self.image = self.images[self.frame][0]
#         self.rect = self.image.get_rect(topleft=pos)
#         self.speed = 5
#         self.velocity_y = 0
#         self.on_ground = True
#         self.timer_anime = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, collision_sprites):
        super().__init__()
        image1 = image
        self.image = pygame.transform.scale(image1, (60, 60))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2()
        self.speed = 300
        self.im_dir = 'right'
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.collision_sprites = collision_sprites
        self.health = 100


    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.im_dir = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.im_dir = 'left'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.im_dir = 'down'
        elif keys[pygame.K_UP]:
            self.direction.y = -1
            self.im_dir = 'up'


        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
            self.anime = True
        else:
            self.anime = False

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):

                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.centerx

                if direction == 'vertical':
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.centery

    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.collision('horizontal')

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        self.collision('vertical')

    def animation(self, FPS, player_images):
        if self.anime:
            self.timer_anime += 1
            image1 = player_images[self.im_dir][self.frame]
            self.image = pygame.transform.scale(image1,(40,60))
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_images[self.im_dir]) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self, dt, FPS, player_images):
        self.input()
        self.move(dt)
        self.animation(FPS, player_images)




    # def animation(self, FPS, player_images):
    #     if self.anime:
    #         self.timer_anime += 1
    #         image1 = player_images[self.im_dir][self.frame]
    #         self.image = pygame.transform.scale(image1,(40,60))
    #         if self.timer_anime / FPS > 0.1:
    #             if self.frame == len(player_images[self.im_dir]) - 1:
    #                 self.frame = 0
    #             else:
    #                 self.frame += 1
    #             self.timer_anime = 0
    #
    #
    #
    #

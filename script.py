import os
import pygame

def load_image(directory):
    # directory путь к папке с картинками, например: 'image/player'
    image_list = [] # список для загруженных картинок
    files = os.listdir(directory) # узнаем названия всех файлов в указанной папке
    for i in files:
        # загружаем картинку и помещаем в конечный список
        image = pygame.image.load(f'{directory}/{i}').convert_alpha()
        image_list.append(image)
    return image_list
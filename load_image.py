import os
import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    if not os.path.isfile(fullname):
        sys.exit(f"Файл {fullname} не найден.")
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
    else:
        image = image.convert_alpha()
    return image

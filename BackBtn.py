import pygame.sprite
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


# class BackButton(pygame.sprite.Sprite):
#     def __init__(self, width, top):
#         super().__init__()
#         self.width = width
#         self.top = top
#         self.image = load_image("back-btn.jpg", -1)
#         self.image = pygame.transform.scale(self.image, (50, 20))
#         self.rect = self.image.get_rect()
#
#         self.rect.x = width - self.rect.w - 20
#         self.rect.y = top
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
#             return True
#         return False

class BackButton(pygame.sprite.Sprite):
    def __init__(self, width, top):
        super().__init__()
        self.width = width
        self.top = top
        self.image = load_image("back-btn.jpg", -1)
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()

        self.rect.x = width - self.rect.w - 20
        self.rect.y = top

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False
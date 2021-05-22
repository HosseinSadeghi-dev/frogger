import time

import pygame
import random
import main
from shared.functions import rotate


class Frog:
    image = pygame.image.load('assets/images/frog.png')

    def __init__(self):
        self.x = main.Game.width / 2
        self.y = main.Game.height - 50
        self.speed = 50
        self.image = Frog.image
        self.rect = pygame.Rect(self.x + self.image.get_width() / 2, self.y + self.image.get_height() / 2,
                                self.image.get_width(), self.image.get_height())

        self.car_hit = False
        self.drowned = False

    def move(self, dir_x, dir_y):

        if (0 < self.x + self.speed * dir_x < main.Game.width - self.image.get_width()) and (
                0 <= self.y + self.speed * -dir_y < main.Game.height):
            if dir_x == 1:
                self.x += self.speed * dir_x
                self.image = rotate('right', Frog.image)
            elif dir_x == -1:
                self.x += self.speed * dir_x
                self.image = rotate('left', Frog.image)
            elif dir_y == 1:
                self.y += self.speed * -dir_y
                self.image = rotate('up', Frog.image)
            elif dir_y == -1:
                self.y += self.speed * -dir_y
                self.image = rotate('down', Frog.image)
            self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
            pygame.mixer.Sound('assets/sounds/jump.mp3').play()

    def show(self):
        main.Game.screen.blit(self.image, [self.x, self.y])
        if self.car_hit:
            main.Game.screen.blit(pygame.image.load('assets/images/blood.png'), [self.x, self.y])

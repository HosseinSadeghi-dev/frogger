import random
import pygame
import main
from shared.functions import rotate


class Obstacle:
    images = ['black', 'blue', 'purple', 'red']

    def __init__(self):
        self.speed = self.speed
        self.rect = pygame.Rect(self.x + self.image.get_width() / 2, self.y + self.image.get_height() / 2,
                                self.image.get_width(), self.image.get_height())

        self.image = self.image
        self.x = self.x
        self.y = self.y
        self.d_x = self.d_x
        self.in_water = self.in_water

    def show(self):
        main.Game.screen.blit(self.image, [self.x, self.y])

    def move(self, frog, obstacles):
        if -self.image.get_width() <= self.x <= (main.Game.width + self.image.get_width()):
            if self.in_water:
                self.x += self.speed * self.d_x
                self.rect = pygame.Rect(self.x, self.y, self.image.get_width() - 2, self.image.get_height() - 2)
                if self.rect.colliderect(frog.rect):
                    frog.x += self.speed * self.d_x
                    frog.rect = pygame.Rect(frog.x, frog.y, frog.image.get_width(), frog.image.get_height())
                elif not any(tree.rect.colliderect(frog.rect) for tree in obstacles) and 50 <= frog.y <= 250:
                    pygame.mixer.Sound('assets/sounds/water_drop.mp3').play()
                    frog.drowned = True
            else:
                if self.y > 250:
                    if any(c.rect.colliderect(frog.rect) for c in obstacles):
                        pygame.mixer.Sound('assets/sounds/crush.mp3').play()
                        frog.car_hit = True
                    else:
                        self.x += self.speed * self.d_x
                        self.rect = pygame.Rect(self.x, self.y, self.image.get_width() - 2, self.image.get_height() - 2)
        else:
            return False

    def change_position(self, obstacles):
        i = 0
        while i < len(obstacles) - 1:
            if any(self.rect.colliderect(obs.rect) and obs is not self for obs in obstacles):
                if self.y % 100 == 0:
                    # right to left
                    self.x += self.image.get_width() + 10
                else:
                    # left to right
                    self.x += -self.image.get_width() - 10
                i = 0
            else:
                i += 1


class Car(Obstacle):
    def __init__(self, cars):
        self.image = pygame.image.load(f'assets/images/{random.choice(Obstacle.images)} car.png')
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.in_water = False
        self.speed = 4

        self.y = random.choice([350, 400, 450, 500, 550])
        if self.y % 100 == 0:
            # right to left
            self.x = main.Game.width + self.image.get_width()
            self.d_x = -1
            self.image = rotate('left', self.image)
        else:
            # left to right
            self.x = -self.image.get_width()
            self.d_x = 1
            self.image = rotate('right', self.image)

        i = 0
        while i < len(cars) - 1:
            if (cars[i].x <= self.x <= cars[i].x + self.image.get_width()) and (cars[i].y == self.y) or (
                    cars[i].x >= self.x >= cars[i].x - self.image.get_width()) and (cars[i].y == self.y):
                if self.y % 100 == 0:
                    # right to left
                    self.x += self.image.get_width()
                else:
                    # left to right
                    self.x += -self.image.get_width()
                i = 0
            else:
                i += 1

        Obstacle.__init__(self)


class Tree(Obstacle):
    def __init__(self, trees):
        self.speed = 2
        self.image = pygame.image.load('assets/images/tree branch.png')
        self.in_water = True

        self.y = random.choice([50, 100, 150, 200, 250])
        if self.y % 100 == 0:
            # right to left
            self.x = main.Game.width + self.image.get_width()
            self.d_x = -1
        else:
            # left to right
            self.x = -self.image.get_width()
            self.d_x = 1

        i = 0
        while i < len(trees) - 1:
            if (trees[i].x <= self.x <= trees[i].x + self.image.get_width()) and (trees[i].y == self.y) or (
                    trees[i].x >= self.x >= trees[i].x - self.image.get_width()) and (trees[i].y == self.y):
                if self.y % 100 == 0:
                    # right to left
                    self.x += self.image.get_width()
                else:
                    # left to right
                    self.x += -self.image.get_width()
                i = 0
            else:
                i += 1
        Obstacle.__init__(self)

import random

import pygame
import time

import frog
import obstacle
from shared.color import Color
from shared.functions import draw_text


class Game:
    pygame.init()
    # accord to picture ratio
    height = 650
    width = 550
    background = pygame.image.load('assets/Images/background.png')
    water_background = pygame.image.load('assets/Images/water.png')
    water_position_1 = 0
    water_position_2 = -background.get_width()
    bg_speed = 4
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Frogger')
    # pygame.display.set_icon(pygame.image.load('assets/Images/lamborghini.png'))
    clock = pygame.time.Clock()
    fps = 60
    font_size = 20

    @staticmethod
    def play():
        pygame.init()

        frogs = []
        for i in range(5):
            frogs.append(frog.Frog())
        current_frog = frogs[0]
        current_frog_index = 0

        cars = []
        trees = []

        while len(frogs) > current_frog_index:

            for event in pygame.event.get():
                # move with keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        current_frog.move(1, 0)
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        current_frog.move(-1, 0)
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        current_frog.move(0, 1)
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        current_frog.move(0, -1)
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    Game.gameover()

            Game.water_position_1 += Game.bg_speed
            Game.water_position_2 += Game.bg_speed

            if Game.water_position_1 > Game.background.get_width():
                Game.water_position_1 = -Game.background.get_width()

            if Game.water_position_2 > Game.background.get_width():
                Game.water_position_2 = -Game.background.get_width()

            Game.screen.blit(Game.background, (0, 0))
            Game.screen.blit(Game.water_background, [Game.water_position_1, 50])
            Game.screen.blit(Game.water_background, [Game.water_position_2, 50])

            if current_frog.y < 50:
                current_frog_index += 1
                if current_frog_index < len(frogs):
                    current_frog = frogs[current_frog_index]
            elif current_frog.car_hit:
                current_frog.show()
                current_frog.car_hit = False
                current_frog_index += 1
                time.sleep(1.5)
                if current_frog_index < len(frogs):
                    current_frog = frogs[current_frog_index]
            elif current_frog.drowned:
                current_frog.show()
                current_frog.drowned = False
                current_frog_index += 1
                time.sleep(1.5)
                if current_frog_index < len(frogs):
                    current_frog = frogs[current_frog_index]

            if len(cars) <= 10:
                if random.random() <= 0.2:
                    cars.append(obstacle.Car(cars))
            if len(trees) <= 20:
                if random.random() <= 0.4:
                    trees.append(obstacle.Tree(trees))

            for car in cars:
                # car.change_position(cars)
                if car.move(current_frog, cars) == False:
                    cars.remove(car)
                car.show()
            for tree in trees:
                # tree.change_position(trees)
                tree.show()
                if tree.move(current_frog, trees) == False:
                    trees.remove(tree)

            current_frog.show()
            for f in range(len(frogs)):
                if f != current_frog_index and frogs[f].y < 50:
                    frogs[f].show()

            draw_text(Game.screen, f'Remaining Frogs: {len(frogs) - current_frog_index}', Color.black, Game.font_size,
                      Game.width - 90, Game.height - 30)

            pygame.display.update()
            Game.clock.tick(Game.fps)

        Game.gameover()

    @staticmethod
    def gameover():
        end_time = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == 13:
                        main()
                if event.type == pygame.QUIT:
                    exit()
            Game.screen.fill(Color.black)

            draw_text(Game.screen, "Gameover !!!", Color.red, Game.font_size,
                      Game.width / 2, Game.height / 2 - 70)

            draw_text(Game.screen, 'Press Enter To PLAY AGAIN', Color.white, Game.font_size,
                      Game.width / 2, Game.height / 2 + 30)

            draw_text(Game.screen, "Press Esc To Exit", Color.white, Game.font_size,
                      Game.width / 2, Game.height / 2 + 70)

            pygame.display.update()


def main():
    Game.play()


if __name__ == "__main__":
    main()

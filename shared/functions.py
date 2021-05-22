import pygame


def rotate(direction, image):
    rotated_image = image
    if direction == "right":
        rotated_image = pygame.transform.rotate(image, 270)
    elif direction == "left":
        rotated_image = pygame.transform.rotate(image, 90)
    elif direction == "up":
        rotated_image = pygame.transform.rotate(image, 0)
    elif direction == "down":
        rotated_image = pygame.transform.rotate(image, 180)
    return rotated_image


def draw_text(screen, text, color, size, x, y):
    font = pygame.font.Font('assets/fonts/arial.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

import pygame
import os
from pygame.locals import *
from sys import exit

# **== CONSTANTS ==**
WIDTH, HEIGHT = 900, 600
BACKGROUND_COLOR = (171, 167, 167)
FPS = 60
DOOR_WIDTH, DOOR_HEIGHT = 130, 180

# **== CONFIG ==**
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monty Hall Problem")

# **== IMAGES ==**
DOOR = pygame.image.load(os.path.join('Assets', 'door.png'))
DOOR = pygame.transform.scale(DOOR, ((DOOR_WIDTH, DOOR_HEIGHT)))
DOOR_OPENED = pygame.image.load(os.path.join('Assets', 'door_opened.png'))
DOOR_OPENED = pygame.transform.scale(DOOR_OPENED, ((DOOR_WIDTH, DOOR_HEIGHT)))
CAR = pygame.image.load(os.path.join('Assets', 'car.png'))
CAR = pygame.transform.scale(CAR, (DOOR_HEIGHT, DOOR_WIDTH))
GOAT = pygame.image.load(os.path.join('Assets', 'goat.png'))
GOAT = pygame.transform.scale(GOAT, (DOOR_HEIGHT, DOOR_WIDTH))

def render():
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(GOAT, (300, 100))
        # pygame.draw.rect(WIN, (255, 0, 0), button)

        pygame.display.flip() #flip melhor que o update em processamento
        # pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()

import pygame
import os
from pygame.locals import *
from sys import exit

# **== CONSTANTS ==**
WIDTH, HEIGHT, MARGIN_LEFT, MARGIN_RIGHT = 900, 600, 80, 80
BACKGROUND_COLOR = (66, 66, 66)
FPS = 60
DOOR_WIDTH, DOOR_HEIGHT = 130, 180

# **== CONFIG ==**
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monty Hall Problem")

# **== IMAGES ==**
DOOR_1 = pygame.image.load(os.path.join('Assets', 'door.png'))
DOOR_1 = pygame.transform.scale(DOOR_1, ((DOOR_WIDTH, DOOR_HEIGHT)))
DOOR_2 = pygame.image.load(os.path.join('Assets', 'door.png'))
DOOR_2 = pygame.transform.scale(DOOR_2, ((DOOR_WIDTH, DOOR_HEIGHT)))
DOOR_3 = pygame.image.load(os.path.join('Assets', 'door.png'))
DOOR_3 = pygame.transform.scale(DOOR_3, ((DOOR_WIDTH, DOOR_HEIGHT)))
DOOR_OPENED_2 = pygame.image.load(os.path.join('Assets', 'door_opened.png'))
DOOR_OPENED_2 = pygame.transform.scale(DOOR_OPENED_2, ((DOOR_WIDTH * 1.8, DOOR_HEIGHT)))
CAR = pygame.image.load(os.path.join('Assets', 'car.png'))
CAR = pygame.transform.scale(CAR, (DOOR_HEIGHT*1.5, DOOR_WIDTH*2))
GOAT = pygame.image.load(os.path.join('Assets', 'goat.png'))
GOAT = pygame.transform.scale(GOAT, (DOOR_HEIGHT, DOOR_WIDTH))

def render():
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(DOOR_1, ((WIDTH - DOOR_WIDTH)/2 - 250, 100))
        WIN.blit(DOOR_2, ((WIDTH - DOOR_WIDTH)/2, 100))
        WIN.blit(DOOR_3, ((WIDTH - DOOR_WIDTH)/2 + 250, 100))

        # **== DOOR_OPENED, CAR AND GOAT POSITION ==**
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 - 350, 100))
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 - 100, 100))
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 + 150, 100))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 - 350, 50))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 - 100, 50))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 + 150, 50))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 - 300, 130))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 - 50, 130))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 + 200, 130))


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

import pygame
import os


WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
FPS = 60
DOOR_WIDTH, DOOR_HEIGHT = 130, 180
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monty Hall Problem")

DOOR = pygame.image.load(os.path.join('Assets', 'door.png'))
DOOR = pygame.transform.scale(DOOR, ((DOOR_WIDTH, DOOR_HEIGHT)))
DOOR_OPENED = pygame.image.load(os.path.join('Assets', 'door_opened.png'))
DOOR_OPENED = pygame.transform.scale(DOOR_OPENED, ((DOOR_WIDTH, DOOR_HEIGHT)))
CAR = pygame.image.load(os.path.join('Assets', 'car.png'))
CAR = pygame.transform.scale(CAR, (DOOR_HEIGHT, DOOR_WIDTH))
GOAT = pygame.image.load(os.path.join('Assets', 'goat.png'))
GOAT = pygame.transform.scale(GOAT, (DOOR_HEIGHT, DOOR_WIDTH))


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(GOAT, (300, 100))
    WIN.blit(CAR, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()


    pygame.quit()


if __name__ == "__main__":
    main()

    

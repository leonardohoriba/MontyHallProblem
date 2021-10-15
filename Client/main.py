import pygame
import os
from pygame.locals import *
from sys import exit
pygame.font.init()

# **== CONSTANTS ==**
WIDTH, HEIGHT, MARGIN_LEFT, MARGIN_RIGHT = 900, 600, 80, 80
BACKGROUND_COLOR = (66, 66, 66)
FPS = 60
DOOR_WIDTH, DOOR_HEIGHT = 130, 180
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 30

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
# BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.jpg'))
# BACKGROUND = pygame.transform.scale(BACKGROUND, ((WIDTH, HEIGHT)))

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def main():
    clock = pygame.time.Clock()
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    title = main_font.render("Monty Hall Problem", 1, (0,0,0))
    reset_button = Button((102, 61, 16), 200, 300, BUTTON_WIDTH, BUTTON_HEIGHT, 'RESET')
    


    # **== Renderização das figuras, em ordem de profundidade ==**
    def render():
        WIN.fill(BACKGROUND_COLOR)
        # WIN.blit(BACKGROUND, (0,0))
        WIN.blit(title, (10, 10))
        WIN.blit(DOOR_1, ((WIDTH - DOOR_WIDTH)/2 - 250, 100))
        WIN.blit(DOOR_2, ((WIDTH - DOOR_WIDTH)/2, 100))
        WIN.blit(DOOR_3, ((WIDTH - DOOR_WIDTH)/2 + 250, 100))
        reset_button.draw(WIN)
        # **== FIGURES IN THE CORRECT POSITION ==**
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 - 350, 100))
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 - 100, 100))
        # WIN.blit(DOOR_OPENED_2, ((WIDTH - DOOR_WIDTH)/2 + 150, 100))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 - 350, 50))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 - 100, 50))
        # WIN.blit(CAR, ((WIDTH - DOOR_WIDTH)/2 + 150, 50))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 - 300, 130))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 - 50, 130))
        # WIN.blit(GOAT, ((WIDTH - DOOR_WIDTH)/2 + 200, 130))


        pygame.display.flip() 
        # pygame.display.update() #flip melhor que o update em processamento

    while run:
        clock.tick(FPS)
        render()

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # Button Clicks
                if reset_button.isOver(mouse_pos): 
                    print('clicked!!!')
            if event.type == pygame.MOUSEMOTION:
                # Button Motion
                if reset_button.isOver(mouse_pos):
                    reset_button.color = (89, 66, 42)
                else:
                    reset_button.color = (102, 61, 16)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()

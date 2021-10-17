import pygame
import os
from pygame.locals import *
from sys import exit
pygame.font.init()

# **== CONSTANTS ==**
WIDTH, HEIGHT, MARGIN_LEFT, MARGIN_RIGHT = 900, 600, 80, 80
BACKGROUND_COLOR = (66, 66, 66)
FPS = 60

# **== DIMENSIONS ==**
DOOR_WIDTH, DOOR_HEIGHT = 130, 180
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 30
DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT = (DOOR_WIDTH * 1.8, DOOR_HEIGHT)
CAR_WIDTH, CAR_HEIGHT =  (DOOR_HEIGHT*1.5, DOOR_WIDTH*2)
GOAT_WIDTH, GOAT_HEIGHT = (DOOR_HEIGHT, DOOR_WIDTH)

# **== POSITIONS ==**
POS_TITLE = (10, 10)
POS_DOOR_1 = ((WIDTH - DOOR_WIDTH)/2 - 250, 100)
POS_DOOR_2 = ((WIDTH - DOOR_WIDTH)/2, 100)
POS_DOOR_3 = ((WIDTH - DOOR_WIDTH)/2 + 250, 100)
POS_DOOR_OPENED_1 = ((WIDTH - DOOR_WIDTH)/2 - 350, 100)
POS_DOOR_OPENED_2 = ((WIDTH - DOOR_WIDTH)/2 - 100, 100)
POS_DOOR_OPENED_3 = ((WIDTH - DOOR_WIDTH)/2 + 150, 100)
POS_CAR_1 = ((WIDTH - DOOR_WIDTH)/2 - 350, 50)
POS_CAR_2 = ((WIDTH - DOOR_WIDTH)/2 - 100, 50)
POS_CAR_3 = ((WIDTH - DOOR_WIDTH)/2 + 150, 50)
POS_GOAT_1 = ((WIDTH - DOOR_WIDTH)/2 - 300, 130)
POS_GOAT_2 = ((WIDTH - DOOR_WIDTH)/2 - 50, 130)
POS_GOAT_3 = ((WIDTH - DOOR_WIDTH)/2 + 200, 130)

# **== CONFIG ==**
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monty Hall Problem")

class Image():
    def __init__(self, path, name, x, y, width, height):
        self.path = path
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        #Call this method to draw the image on the screen
        self.image = pygame.image.load(os.path.join(self.path, self.name))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        WIN.blit(self.image, (self.x, self.y))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
        
class Button():
    def __init__(self, color, x, y, width, height, text=''):
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

    reset_button = Button((102, 61, 16), 300, 400, BUTTON_WIDTH, BUTTON_HEIGHT, 'RESET')
    door_1 = Image('Assets', 'door.png', POS_DOOR_1[0], POS_DOOR_1[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_2 = Image('Assets', 'door.png', POS_DOOR_2[0], POS_DOOR_2[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_3 = Image('Assets', 'door.png', POS_DOOR_3[0], POS_DOOR_3[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_opened_1 = Image('Assets', 'door_opened.png', POS_DOOR_OPENED_1[0], POS_DOOR_OPENED_1[1], DOOR_OPENED_WIDTH, DOOR_OPENED_WIDTH)
    door_opened_2 = Image('Assets', 'door_opened.png', POS_DOOR_OPENED_2[0], POS_DOOR_OPENED_2[1], DOOR_OPENED_WIDTH, DOOR_OPENED_WIDTH)
    door_opened_3 = Image('Assets', 'door_opened.png', POS_DOOR_OPENED_3[0], POS_DOOR_OPENED_3[1], DOOR_OPENED_WIDTH, DOOR_OPENED_WIDTH)
    car_1 = Image('Assets', 'car.png', POS_CAR_1[0], POS_CAR_1[1], CAR_WIDTH, CAR_WIDTH)
    car_2 = Image('Assets', 'car.png', POS_CAR_2[0], POS_CAR_2[1], CAR_WIDTH, CAR_WIDTH)
    car_3 = Image('Assets', 'car.png', POS_CAR_3[0], POS_CAR_3[1], CAR_WIDTH, CAR_WIDTH)
    goat_1 = Image('Assets', 'goat.png', POS_GOAT_1[0], POS_GOAT_1[1], GOAT_WIDTH, GOAT_WIDTH)
    goat_2 = Image('Assets', 'goat.png', POS_GOAT_2[0], POS_GOAT_2[1], GOAT_WIDTH, GOAT_WIDTH)
    goat_3 = Image('Assets', 'goat.png', POS_GOAT_3[0], POS_GOAT_3[1], GOAT_WIDTH, GOAT_WIDTH)


    # **== Renderização das figuras, em ordem de profundidade ==**
    def render():
        WIN.fill(BACKGROUND_COLOR)
        # WIN.blit(BACKGROUND, (0,0))
        WIN.blit(title, (10, 10))
        door_1.draw()
        door_2.draw()
        door_3.draw()
        door_opened_1.draw()
        door_opened_2.draw()
        door_opened_3.draw()
        car_1.draw()
        car_2.draw()
        car_3.draw()
        goat_1.draw()
        goat_2.draw()
        goat_3.draw()
        reset_button.draw(WIN, (0,0,0))
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
                    print(mouse_pos)
                
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

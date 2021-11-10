import pygame
import os
from pygame import mouse
from pygame.locals import *
from sys import exit
import socket
import time
import ast
import json
pygame.font.init()

# **== CONSTANTS ==**
WIDTH, HEIGHT, MARGIN_LEFT, MARGIN_RIGHT = 900, 600, 80, 80
BACKGROUND_COLOR = (66, 66, 66)
FPS = 60
INFO_TEXT_0 = 'I have hidden a car behind one of these three doors.'
INFO_TEXT_1 = 'Behind the other two doors there are goats. If you choose the door with the car, you win the car!'
INFO_TEXT_2 = 'If you choose a door with a goat, you get a goat. Click on a door to choose it.'
INFO_TEXT_3 = 'I will display one goat and allow to stay with your choice or switch doors.'
INFO_TEXT_4 = 'Click on your door to stay with it, or click on the other door to switch.'
INFO_TEXT_5 = 'I will then reveal the location of the car. Click on play again to restart the game.' 
INFO_TEXT_6 = 'Should you stay with your first choice, or switch?'

# **== DIMENSIONS ==**
DOOR_WIDTH, DOOR_HEIGHT = 130, 180
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 30
DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT = (DOOR_WIDTH * 1.8, DOOR_HEIGHT)
CAR_WIDTH, CAR_HEIGHT =  (DOOR_HEIGHT*1.5, DOOR_WIDTH*2)
GOAT_WIDTH, GOAT_HEIGHT = (DOOR_HEIGHT, DOOR_WIDTH)
WIN_WIDTH, WIN_HEIGHT = 200, 100

# **== POSITIONS ==**
POS_TITLE = (10, 10)
POS_DOOR_1 = ((WIDTH - DOOR_WIDTH)/2 - 250, 130)
POS_DOOR_2 = ((WIDTH - DOOR_WIDTH)/2, 130)
POS_DOOR_3 = ((WIDTH - DOOR_WIDTH)/2 + 250, 130)
POS_DOOR_OPENED_1 = ((WIDTH - DOOR_WIDTH)/2 - 350, 130)
POS_DOOR_OPENED_2 = ((WIDTH - DOOR_WIDTH)/2 - 100, 130)
POS_DOOR_OPENED_3 = ((WIDTH - DOOR_WIDTH)/2 + 150, 130)
POS_CAR_1 = ((WIDTH - DOOR_WIDTH)/2 - 350, 120)
POS_CAR_2 = ((WIDTH - DOOR_WIDTH)/2 - 100, 120)
POS_CAR_3 = ((WIDTH - DOOR_WIDTH)/2 + 150, 120)
POS_GOAT_1 = ((WIDTH - DOOR_WIDTH)/2 - 270, 120)
POS_GOAT_2 = ((WIDTH - DOOR_WIDTH)/2 - 20, 120)
POS_GOAT_3 = ((WIDTH - DOOR_WIDTH)/2 + 230, 120)
POS_STAY_1 = (POS_DOOR_1[0] + DOOR_WIDTH/2 - 25, POS_DOOR_1[1] + DOOR_HEIGHT/2)
POS_STAY_2 = (POS_DOOR_2[0] + DOOR_WIDTH/2 - 25, POS_DOOR_2[1] + DOOR_HEIGHT/2)
POS_STAY_3 = (POS_DOOR_3[0] + DOOR_WIDTH/2 - 25, POS_DOOR_3[1] + DOOR_HEIGHT/2)
POS_SWITCH_1 = (POS_DOOR_1[0] + DOOR_WIDTH/2 - 40, POS_DOOR_1[1] + DOOR_HEIGHT/2)
POS_SWITCH_2 = (POS_DOOR_2[0] + DOOR_WIDTH/2 - 40, POS_DOOR_2[1] + DOOR_HEIGHT/2)
POS_SWITCH_3 = (POS_DOOR_3[0] + DOOR_WIDTH/2 - 40, POS_DOOR_3[1] + DOOR_HEIGHT/2)
POS_STAYS = [POS_STAY_1, POS_STAY_2, POS_STAY_3]
POS_SWITCHES = [POS_SWITCH_1, POS_SWITCH_2, POS_SWITCH_3]
POS_X_1 = ((WIDTH - DOOR_WIDTH)/2 - 270, 135)
POS_X_2 = ((WIDTH - DOOR_WIDTH)/2 - 20, 135)
POS_X_3 = ((WIDTH - DOOR_WIDTH)/2 + 230, 135)

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

class Client():
    PORT = 5050
    FORMATO = 'utf-8'
    SERVER = "127.0.3.4"
    ADDR = (SERVER, PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
    


    def jogar(self,mensagem):
        self.client.send(str(mensagem).encode(self.FORMATO))
        msg = None
        while msg is None:
            msg = self.client.recv(1024).decode()
        return msg

def main():
    
    cliente1 = Client()
        
    clock = pygame.time.Clock()
    run = True
    info = False
    request = 0
    default_res = {
                    'doors' : "['d', 'd', 'd']",
                    'stay': 'None',
                    'switch': 'None',
                    'status': 'None',
                    }
    response = default_res

    main_font = pygame.font.SysFont("comicsans", 50)
    secondary_font = pygame.font.SysFont("comicsans", 30)
    info_font = pygame.font.SysFont("comicsans", 20)
    mario_font = pygame.font.Font(os.path.join(r'./Assets', r'Mario-Kart-DS.ttf'), 55)

    title = mario_font.render("MONTY HALL PROBLEM", 1, (0,0,0))
    stay = secondary_font.render("Stay", 1, (0,0,0))
    switch = secondary_font.render("Switch", 1, (0,0,0))
    text_info_0 = info_font.render(INFO_TEXT_0, 1, (0,0,0))
    text_info_1 = info_font.render(INFO_TEXT_1, 1, (0,0,0))
    text_info_2 = info_font.render(INFO_TEXT_2, 1, (0,0,0))
    text_info_3 = info_font.render(INFO_TEXT_3, 1, (0,0,0))
    text_info_4 = info_font.render(INFO_TEXT_4, 1, (0,0,0))
    text_info_5 = info_font.render(INFO_TEXT_5, 1, (0,0,0))
    text_info_6 = info_font.render(INFO_TEXT_6, 1, (0,0,0))

    # **== OBJECTS ==**
    reset_button = Button((102, 61, 16), WIDTH*0.83, HEIGHT*0.82, BUTTON_WIDTH, BUTTON_HEIGHT, 'RESET')
    info_button = Button((102, 61, 16), WIDTH*0.80, HEIGHT*0.90, BUTTON_WIDTH+55, BUTTON_HEIGHT, 'INSTRUCTIONS')
    again_button = Button((102, 61, 16), WIDTH*0.76, HEIGHT*0.55, BUTTON_WIDTH+35, BUTTON_HEIGHT, 'PLAY AGAIN')
    door_1 = Image(r'./Assets', 'door.png', POS_DOOR_1[0], POS_DOOR_1[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_2 = Image(r'./Assets', 'door.png', POS_DOOR_2[0], POS_DOOR_2[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_3 = Image(r'./Assets', 'door.png', POS_DOOR_3[0], POS_DOOR_3[1], DOOR_WIDTH, DOOR_HEIGHT)
    door_opened_1 = Image(r'./Assets', 'door_opened.png', POS_DOOR_OPENED_1[0], POS_DOOR_OPENED_1[1], DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT)
    door_opened_2 = Image(r'./Assets', 'door_opened.png', POS_DOOR_OPENED_2[0], POS_DOOR_OPENED_2[1], DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT)
    door_opened_3 = Image(r'./Assets', 'door_opened.png', POS_DOOR_OPENED_3[0], POS_DOOR_OPENED_3[1], DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT)
    car_1 = Image(r'./Assets', 'car.png', POS_CAR_1[0], POS_CAR_1[1], CAR_WIDTH, CAR_WIDTH)
    car_2 = Image(r'./Assets', 'car.png', POS_CAR_2[0], POS_CAR_2[1], CAR_WIDTH, CAR_WIDTH)
    car_3 = Image(r'./Assets', 'car.png', POS_CAR_3[0], POS_CAR_3[1], CAR_WIDTH, CAR_WIDTH)
    goat_1 = Image(r'./Assets', 'goat.png', POS_GOAT_1[0], POS_GOAT_1[1], GOAT_WIDTH, GOAT_WIDTH)
    goat_2 = Image(r'./Assets', 'goat.png', POS_GOAT_2[0], POS_GOAT_2[1], GOAT_WIDTH, GOAT_WIDTH)
    goat_3 = Image(r'./Assets', 'goat.png', POS_GOAT_3[0], POS_GOAT_3[1], GOAT_WIDTH, GOAT_WIDTH)
    you_win_1 = Image(r'./Assets', 'win.png', WIDTH*0.09, HEIGHT*0.18, WIN_WIDTH, WIN_HEIGHT)
    you_win_2 = Image(r'./Assets', 'win.png', WIDTH*0.37, HEIGHT*0.18, WIN_WIDTH, WIN_HEIGHT)
    you_win_3 = Image(r'./Assets', 'win.png', WIDTH*0.65, HEIGHT*0.18, WIN_WIDTH, WIN_HEIGHT)
    you_lose_1 = Image(r'./Assets', 'x.png', POS_X_1[0], POS_X_1[1], WIN_WIDTH, WIN_HEIGHT+50)
    you_lose_2 = Image(r'./Assets', 'x.png', POS_X_2[0], POS_X_2[1], WIN_WIDTH, WIN_HEIGHT+50)
    you_lose_3 = Image(r'./Assets', 'x.png', POS_X_3[0], POS_X_3[1], WIN_WIDTH, WIN_HEIGHT+50)

    doors = [door_1, door_2, door_3]
    doors_opened = [door_opened_1, door_opened_2, door_opened_3]
    cars = [car_1, car_2, car_3]
    goats = [goat_1, goat_2, goat_3]
    wins = [you_win_1, you_win_2, you_win_3]
    loses = [you_lose_1, you_lose_2, you_lose_3]
    # **== Renderização das figuras, em ordem de profundidade ==**
    def render(response=default_res):
        WIN.fill(BACKGROUND_COLOR)
        # WIN.blit(BACKGROUND, (0,0))
        WIN.blit(title, (WIDTH/7, 30))

        door_list = list(response['doors'])
        filtered = filter(lambda elem: elem not in [',', "'", ' ', ']', '[', '"'], door_list)
        for idx, elem in enumerate(list(filtered)):
            if elem == 'd':
                doors[idx].draw()
            elif elem == 'g':
                doors_opened[idx].draw()
                goats[idx].draw()
            elif elem == 'c':
                doors_opened[idx].draw()
                cars[idx].draw()
            if response['stay'] != 'None':
                WIN.blit(stay, POS_STAYS[int(response['stay'])])
            if response['stay'] != 'None':
                WIN.blit(switch, POS_SWITCHES[int(response['switch'])])
            if response['status'] == 'lose':
                loses[int(request)].draw()
            if response['status'] == 'win':
                wins[int(request)].draw() 
        

        info_button.draw(WIN, (0,0,0))

        if info: #print text with game instructions
            WIN.blit(text_info_0, (WIDTH*0.1, HEIGHT*0.8))
            WIN.blit(text_info_1, (WIDTH*0.1, HEIGHT*0.825))
            WIN.blit(text_info_2, (WIDTH*0.1, HEIGHT*0.85))
            WIN.blit(text_info_3, (WIDTH*0.1, HEIGHT*0.875))
            WIN.blit(text_info_4, (WIDTH*0.1, HEIGHT*0.9))
            WIN.blit(text_info_5, (WIDTH*0.1, HEIGHT*0.925))
            WIN.blit(text_info_6, (WIDTH*0.1, HEIGHT*0.95))


        pygame.display.flip() 

    render(default_res)

    while run:
        clock.tick(FPS)
        render(response)
        
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                cliente1.jogar("exit")
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: 


                if door_1.isOver(mouse_pos): 
                    request = '0'
                    response = cliente1.jogar("msg=" + request)
                    response = ast.literal_eval(response)
                    time.sleep(0.2)
                    
                if door_2.isOver(mouse_pos): 
                    request = '1'
                    response = cliente1.jogar("msg=" + request)
                    response = ast.literal_eval(response)
                    time.sleep(0.2)

                if door_3.isOver(mouse_pos): 
                    request = '2'
                    response = cliente1.jogar("msg=" + request)
                    response = ast.literal_eval(response)
                    time.sleep(0.2)

                if info_button.isOver(mouse_pos):
                    info = not(info)

                
 
            if event.type == pygame.MOUSEMOTION:


                if info_button.isOver(mouse_pos):
                    info_button.color = (89, 66, 42)
                else:
                    info_button.color = (102, 61, 16)
                

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()

import socket
import threading
import time



class Client():
    PORT = 5050
    FORMATO = 'utf-8'
    SERVER = "127.0.3.1"
    ADDR = (SERVER, PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        thread1 = threading.Thread(target=self.handle_mensagens)
        thread2 = threading.Thread(target=self.iniciar_envio)
        thread1.start()
        thread2.start()
            
    
    def handle_mensagens(self):
        #while(True):
            msg = self.client.recv(1024).decode()
            print('\n'+msg)
    
    def enviar_mensagem(self):
        mensagem = input("digite sua jogada\n")
        self.enviar("msg=" + mensagem)

    def enviar(self,mensagem):
        print("enviado")
        self.client.send(str(mensagem).encode(self.FORMATO))
        msg = None
        while msg is None:
            msg = self.client.recv(1024).decode()
        return msg


    def iniciar_envio(self):
        while(True):
            self.enviar_mensagem()






Client()
while(True):
    msg = input("digite sua mensagem:")
    resposta = Client.enviar(msg)
    print("essa é a resposta:" + msg)

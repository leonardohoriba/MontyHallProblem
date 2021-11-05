import socket
import time



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
        print("enviado")
        msg = None
        while msg is None:
            msg = self.client.recv(1024).decode()
        return msg









cliente1 = Client()
while(True):
    msg = input("digite sua mensagem:")
    time.sleep(0.2)
    resposta = cliente1.jogar("msg=" + msg)
    time.sleep(0.2)
    print("essa é a resposta:" + resposta)

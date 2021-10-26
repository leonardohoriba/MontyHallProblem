import socket
import time
from random import randrange



class Server():
    conexoes = {}
    mensagens = []
    
    SERVER_IP = '127.0.3.1'
    #socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (SERVER_IP, PORT)
    FORMATO = 'utf-8'
    #socket do tipo TCP socket.SOCK_STREAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    conn,addr=False,False
    run=True
    nome=False

    def __init__(self):
        print(f"[INICIO] Socket iniciado no ip {self.SERVER_IP}")
        self.server.listen()
        while (self.run):
            self.conn, self.addr = self.server.accept()
            self.handle_clientes(self.conn, self.addr)

    def handle_clientes(self,conn,addr):
        print(f'[NOVA CONEXÃO] Endereço: {addr}')
        self.nome = False
        vencedor=str(randrange(0,2))
        doors=['door1','door2','door3']
        print('vencedor = ' + vencedor)
        reposta = {}
        status = None
        while(True):
            msg= conn.recv(1024).decode()
            if(msg):
                if(msg=='msg=exit'):
                    self.conn.close()
                print(msg)
                
                mensagem_separada= msg.split("=")
                self.nome = mensagem_separada[1]
                   
                mensagem=mensagem_separada[1]
                retorno = mensagem
                if (mensagem == '1'):
                    print(1)
                    if vencedor == '1':
                        retorno = str('{ door1 :O,door2:C,door3:C,status:win}')
                    else:
                        retorno = str('{ door1 :O,door2:C,door3:C,status:None}')
                elif(mensagem == '2'):
                    print(2)
                    if vencedor == '2':
                        retorno = str('{ door1:C,door2:O,door3:C,status:win}')
                    else:
                        retorno = str('{door1:C,door2:O,door3:C,status:None}')
                elif(mensagem == '3'):
                    print(3)
                    if vencedor == '3':
                        retorno = str('{door1:C,door2:C,door3:O,status:win}')
                    else:
                        retorno = str('{door1:C,door2:C,door3:O,status:None}')
                #JOGO
                self.enviar_mensagem(retorno)

    def enviar_mensagem(self,mensagem):
        mensagem_envio=mensagem
        self.conn.send(mensagem_envio.encode(self.FORMATO))
        time.sleep(0.2)

        


Server()
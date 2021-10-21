import socket
import threading
import time



class Server():
    conexoes = {}
    mensagens = []
    #socket do tipo TCP socket.SOCK_STREAM
    SERVER_IP = '127.0.14.1'
    #socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (SERVER_IP, PORT)
    FORMATO = 'utf-8'
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
            thread = threading.Thread(target=self.handle_clientes, args=(self.conn,self.addr))
            thread.start()

    def handle_clientes(self,conn,addr):
        print(f'[NOVA CONEXÃO] Endereço: {addr}')
        self.nome = False

        while(True):
            msg= conn.recv(1024).decode()
            if(msg):
                if(msg=='msg=exit'):
                    self.conn.close()
                print(msg)
                
                mensagem_separada= msg.split("=")
                self.nome = mensagem_separada[1]
                   
                mensagem=mensagem_separada[1]
                self.mensagens.append(mensagem)
                self.enviar_mensagem(mensagem)

    def enviar_mensagem(self,mensagem):
        mensagem_envio=mensagem
        self.conn.send(mensagem_envio.encode(self.FORMATO))
        time.sleep(0.2)

        


Server()
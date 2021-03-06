import socket
import time
from random import randrange

#### Lógica do Jogo
class game():
    doors=[0,1,2]
    retorno = None
    vencedor = None
    nr_jogada = 1
    def __init__(self):
        self.vencedor=int(randrange(0,3))
        self.vector=["d","d","d"]
        self.retorno = { 'doors':'["d","d","d"]','status':'None','switch':'None','stay':'None'}
    def jogada(self,selecionada):
        if selecionada not in self.doors:
            return 'ERROR'
        if self.nr_jogada == 1:
            win=self.vencedor
            self.nr_jogada=2
            self.retorno['stay']=str(selecionada)
            for i in self.doors:
                if (i is not selecionada) and (i is not win):
                    self.vector[i]='g'
                    h=i
                    break
            for i in self.doors:
                if (i is not selecionada) and (i is not h):
                    self.retorno['switch']=str(i)
            self.retorno['doors']=str(self.vector)
            return str(self.retorno)
        if self.nr_jogada == 2:
            win=self.vencedor
            self.nr_jogada=3
            self.retorno['stay']='None'
            self.retorno['switch']='None'
            self.vector[win]='c'
            if selecionada == win:
                self.retorno['status']='win'
                for i in self.doors:
                    if i is not win:
                        self.vector[i]='g'
                self.retorno['doors']=str(self.vector)
            else:           
                self.retorno['status']='lose'
                for i in self.doors:
                    if i is not win:
                        self.vector[i]='g'
                self.retorno['doors']=str(self.vector)
            return str(self.retorno)
        if self.nr_jogada == 3:
            self.nr_jogada=1
            self.retorno = { 'doors':'["d","d","d"]','status':'None','switch':'None','stay':'None'}
            self.vector=["d","d","d"]
            self.vencedor=int(randrange(0,3))
            return str(self.retorno)
            


class Server():
   
    SERVER_IP = "127.0.3.4"
    PORT = 5050
    ADDR = (SERVER_IP, PORT)
    FORMATO = 'utf-8'
    #Socket do tipo TCP socket.SOCK_STREAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    conn,addr=False,False
    run=True
    nome=False
    game1=game()

    def __init__(self):
        print(f"[INICIO] Socket iniciado no ip {self.SERVER_IP}")
        self.server.listen()
        game1 = game()
        while (self.run):
            self.conn, self.addr = self.server.accept()
            self.handle_clientes(self.conn, self.addr)

    def handle_clientes(self,conn,addr):
        print(f'[NOVA CONEXÃO] Endereço: {addr}')
        self.nome = False
        while(self.run ==True):
            msg= conn.recv(54).decode()
            if(msg):
                if(msg=='exit'):
                    print('[ENCERRANDO CONEXÃO DO SOCKET]')
                    self.conn.close()
                    self.run=False
                    break
                else:
                    mensagem_separada= msg.split("=")
                    self.nome = mensagem_separada[1]
                    
                    mensagem=int(mensagem_separada[1])
                    retorno = self.game1.jogada(mensagem)
                    self.enviar_mensagem(str(retorno))

    def enviar_mensagem(self,mensagem):
        mensagem_envio=mensagem
        self.conn.send(mensagem_envio.encode(self.FORMATO))
        time.sleep(0.2)
    

        


Server()
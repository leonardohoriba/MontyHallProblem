import socket 

class server():
    HOST = 'localhost'
    PORT = 50000

    def __init__(self):
        #Utilizaremos o protocolo tcp para maior confiabilidade da conexão 
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST,self.PORT))
        self.s.listen()
        print('Aguardando a conexão de um cliente')
        print('conectado em ', self.ender)
        

    def receber(self):
        self.conn,self.ender=self.s.accept()
        data=self.conn.recv(1024)
        self.conn.sendall(str.encode(str(data)))
        
    def abrir(self):
        self.s.listen()
        print('conectado em ', self.ender)

    def fechar (self):
        print('Fechando conexão')
        self.conn.close()


servidor= server()
servidor.receber()
servidor.fechar()
servidor.abrir()
#servidor.receber()
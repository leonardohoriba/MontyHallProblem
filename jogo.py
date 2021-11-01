from random import randrange
class game():
    doors=[0,1,2]
    retorno = None
    vencedor = None
    nr_jogada = 1
    def __init__(self):
        self.vencedor=int(randrange(0,2))
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
            self.vector[win]='car'
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
            self.vencedor=int(randrange(0,2))
            return str(self.retorno)

jogo = game()
jogo.jogada(1,1)
jogo.jogada(1,2)
jogo.jogada(1,3)
jogo.jogada(1,1)
jogo.jogada(0,2)
jogo.jogada(1,1)



            
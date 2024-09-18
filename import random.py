import random
class Pokemon:
    def __init__(self, bichinho, elemento,  alvo):
        self.bichinho = bichinho
        self.elemento = elemento
        self.alvo = alvo
    def ataquebasico(self,alvo): 
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print('O ataque foi crítico!')
            alvovida = alvo - 5
        elif 5<=x<=7:
            print('O ataque foi normal!')
            alvovida = alvo - 3
        else: 
            print('O ataque foi fraco!')
            alvovida = alvo -1
class Charmander(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, Charmander, 'Fogo', )
    def flameburst(self):
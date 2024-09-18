import random
class Pokemon:
    def __init__(self, bichinho, vida, evolucao ,  elemento,  alvo):
        self.bichinho = bichinho
        self.vida = vida
        self.evolucao = evolucao
        self.elemento = elemento
        self.alvo = alvo
    def ataquebasico(self,alvo): 
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print('O ataque foi crítico!')
            alvo.vida = alvo - 5
        elif 5<=x<=7:
            print('O ataque foi normal!')
            alvo.vida = alvo - 3
        else: 
            print('O ataque foi fraco!')
            alvo.vida = alvo -1
class Charmander(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmander', vida = 100 , elemento ='Fogo', alvo )
    def flameburst(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print(f'O {self.bichinho} utilizou o Flame Burst! Acerto em cheio!')
            alvo.vida = alvo - 15
        elif 5<=x<=7:
            print('O {self.bichinho} utilizou o Flame Burst! Acerto normal!')
            alvo.vida = alvo - 9
        else: 
            print('O {self.bichinho} utilizou o Flame Burst! O ataque foi fraco!')
            alvo.vida = alvo -3
    def dragonrage(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto em cheio!')
            alvo.vida = alvo - 20
        elif 5<=x<=7:
            print('O {self.bichinho} utilizou o Dragon Rage! Acerto normal!')
            alvo.vida = alvo - 12
        else: 
            print('O {self.bichinho} utilizou o Dragon Rage! O ataque foi fraco!')
            alvo.vida = alvo - 4
class Charmeleon(Pokemon, Charmander):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmeleon', vida = 200 , elemento ='Fogo', alvo )
    
    
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
        Pokemon.__init__(self, bichinho = 'Charmander', vida = 100, evolucao = 1 , elemento ='Fogo', alvo )
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
class Charmeleon (Charmander):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmeleon', vida = 200, evolucao = 2 , elemento ='Fogo', alvo )
    def firePunch(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print(f'O {self.bichinho} utilizou o Fire Punch! Acerto em cheio!')
            alvo.vida = alvo - 15
        elif 5<=x<=7:
            print(f'O {self.bichinho} utilizou o Fire Punch! Acerto normal!')
            alvo.vida = alvo - 9
        else: 
            print(f'O {self.bichinho} utilizou o Fire Punch! O ataque foi fraco!')
            alvo.vida = alvo -3
    def flamethrower(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto em cheio!')
            alvo.vida = alvo - 40
        elif 5<=x<=7:
            print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto normal!')
            alvo.vida = alvo - 20
        else: 
            print(f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi fraco!')
            alvo.vida = alvo - 10
class Charizard(Charmeleon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charizard', vida = 300, evolucao = 3 , elemento ='Fogo', alvo )
    def fireblast(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print(f'O {self.bichinho} utilizou o Fire Blast! Acerto em cheio!')
            alvo.vida = alvo - 60
        elif 5<=x<=7:
            print(f'O {self.bichinho} utilizou o Fire Blast! Acerto normal!')
            alvo.vida = alvo - 30
        else: 
            print(f'O {self.bichinho} utilizou o Fire Blast! O ataque foi fraco!')
            alvo.vida = alvo - 15
def computadorescolhas():
    evolucaocomputador = random.choice[1,2,3]
    alvonome = random.choice['Charmander', 'Bulbasaur', 'Squirtle']
    if alvonome == 'Charmander' and evolucaocomputador == 1:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')
    elif alvonome == 'Charmander' and evolucaocomputador == 2:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, flamethrower]
        print(f'O {alvonome} atacou com {Charmeleon.escolhaataque}') 
    elif alvonome == 'Charmander' and evolucaocomputador == 3:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, flamethrower, fireblast ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')      
















bichinho = input('Qual Pokemon você deseja entre Charmander, Bulbasaur ou Squirtle para lutar?')
evolucao = input('Qual a evolução do Pokemon inicial que você escolheu que deseja selecionar para a luta?')



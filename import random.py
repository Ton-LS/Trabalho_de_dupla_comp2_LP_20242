import random
class Pokemon:
    def __init__(self, bichinho, vida, evolucao ,  elemento, ):
        self.bichinho = bichinho
        self.vida = vida
        self.evolucao = evolucao
        self.elemento = elemento
    def ataquebasico(self): 
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print('O ataque foi crítico!')
            self.vida = self.vida - 5
        elif 5<=x<=7:
            print('O ataque foi normal!')
            self.vida = self.vida - 3
        else: 
            print('O ataque foi fraco!')
            self.vida = self.vida -1
class Charmander(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmander', vida = 100, evolucao = 1 , elemento ='Fogo')
    def flameburst(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto em cheio!')
            self.vida = self.vida - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto normal!')
            self.vida = self.vida - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Flame Burst! O ataque foi fraco!')
            self.vida = self.vida -3
    def dragonrage(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto em cheio!')
            self.vida = self.vida - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto normal!')
            self.vida = self.vida - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi fraco!')
            self.vida = self.vida - 4
class Charmeleon (Charmander):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmeleon', vida = 200, evolucao = 2 , elemento ='Fogo' )
    def firepunch(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto em cheio!')
            self.vida = self.vida - 25
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto normal!')
            self.vida = self.vida - 15
        else: 
            return print(f'O {self.bichinho} utilizou o Fire Punch! O ataque foi fraco!')
            self.vida = self.vida -10
    def flamethrower(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto em cheio!')
            self.vida = self.vida - 50
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto normal!')
            self.vida = self.vida - 25
        else: 
            return print(f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi fraco!')
            self.vida = self.vida - 15
class Charizard(Charmeleon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charizard', vida = 300, evolucao = 3 , elemento ='Fogo' )
    def fireblast(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto em cheio!')
            self.vida = self.vida - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto normal!')
            self.vida = self.vida - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Fire Blast! O ataque foi fraco!')
            self.vida = self.vida - 15
class Bulbasaur(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Bulbasaur', vida = 100, evolucao = 1 , elemento ='Planta')
    def vinewip(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto em cheio!')
            self.vida = self.vida - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto normal!')
            self.vida = self.vida - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Vine Wip! O ataque foi fraco!')
            self.vida = self.vida -3
    def seedbomb(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto em cheio!')
            self.vida = self.vida - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto normal!')
            self.vida = self.vida - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi fraco!')
            self.vida = self.vida - 4
class Ivysaur(Bulbasaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Ivysaur', vida = 200, evolucao = 2 , elemento ='Planta')
    def solarbeam(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto em cheio!')
            self.vida = self.vida - 25
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto normal!')
            self.vida = self.vida - 15
        else: 
            return print(f'O {self.bichinho} utilizou o Solar Beam! O ataque foi fraco!')
            self.vida = self.vida -10
    def powerwip(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto em cheio!')
            self.vida = self.vida - 50
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto normal!')
            self.vida = self.vida - 25
        else: 
            return print(f'O {self.bichinho} utilizou o Power Wip! O ataque foi fraco!')
            self.vida = self.vida - 15
class Venusaur(Bulbasaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Venusaur', vida = 300, evolucao = 3 , elemento ='Planta')
    def petalblizzard(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto em cheio!')
            self.vida = self.vida - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto normal!')
            self.vida = self.vida - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi fraco!')
            self.vida = self.vida - 15
class Squirtle(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Squirtle', vida = 100, evolucao = 1, elemento = 'Água')
    def bubble(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto em cheio!')
            self.vida = self.vida - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto normal!')
            self.vida = self.vida - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Bubble! O ataque foi fraco!')
            self.vida = self.vida -3
    def waterpulse(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto em cheio!')
            self.vida = self.vida - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto normal!')
            self.vida = self.vida - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Water Pulse! O ataque foi fraco!')
            self.vida = self.vida - 4
class Wartortle(Squirtle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Wartortle', vida = 200, evolucao = 2, elemento = 'Água')
    def watergun(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto em cheio!')
            self.vida = self.vida - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto normal!')
            self.vida = self.vida - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Water Gun! O ataque foi fraco!')
            self.vida = self.vida -3
    def aquajet(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto em cheio!')
            self.vida = self.vida - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto normal!')
            self.vida = self.vida - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi fraco!')
            self.vida = self.vida - 4
class Blastoise(Squirtle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Blastoise', vida = 300, evolucao = 3 , elemento ='Água')
    def hydropump(self):
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto em cheio!')
            self.vida = self.vida - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto normal!')
            self.vida = self.vida - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi fraco!')
            self.vida = self.vida - 15


def alvoescolhas(alvonome):
    if alvonome == Charmander:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')
    elif alvonome == Charmeleon:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, firepunch, flamethrower]
        print(f'O {alvonome} atacou com {Charmeleon.escolhaataque}') 
    elif alvonome == Charizard:
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, firepunch, flamethrower, fireblast ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')
    elif alvonome == Bulbasaur:
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb]
        print(f'O {alvonome} atacou com {Bulbasaur.escolhaataque}') 
    elif alvonome == Ivysaur:
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb, solarbeam, powerwip]
        print(f'O {alvonome} atacou com {Ivysaur.escolhaataque}') 
    elif alvonome == Venusaur:
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb, solarbeam, powerwip, petalblizzard]
        print(f'O {alvonome} atacou com {Venusaur.escolhaataque}')
    elif alvonome == Squirtle:
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse]
        print(f'O {alvonome} atacou com {Squirtle.escolhaataque}')
    elif alvonome == Wartortle:
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse, watergun, aquajet]  
        print(f'O {alvonome} atacou com {Wartortle.escolhaataque}') 
    elif alvonome == Blastoise:
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse, watergun, aquajet, hydropump]
        print(f'O {alvonome} atacou com {Blastoise.escolhaataque}')
def lutadepokemons(alvonome, alvoescolhas, bichinho):
    treinador01 =   bichinho()
    treinadorcomputador = alvonome()
    print('Opa! Um treinador adversário foi encontrado!')
    print(f'O treinador lançou o {alvonome}')
    while bichinho.vida != 0 or alvonome.vida != 0:
    #escrevendo comentario aqui pq ja sao 04 da manhã e to com preguiça de fazer mais coisa disso aqui
    #a parada q eu pensei foi em tirar a vida do bicho do cara que lançou o poder e não do adversario
    #pq ai fica mais facil tlgd? ai quando a vida do oponente chegar a 0 teoricamente a gnt perde e vice versa
    #pq nao achei um jeito de ficar mudando a vida do nosso personagem conforme o bicho inimigo lançar um ataque 
    #precisa fazer uns ifs pra poder mostrar pro usuario quais ataques ele pode usar e depois fazer esse loop até a batalha acabar
    #quando acabar diz que foi um prazer ter o jogador jogando o nosso jogo e acabou eu acho
       
    






bichinho = input('Qual Pokemon você deseja entre Charmander, Charmeleon, Charizard , Bulbasaur, Ivysaur, Venusaur, Squirtle, Wartotle ou Blastoise para lutar?').lower
if bichinho == 'charmander': bichinho = Charmander
elif bichinho == 'charmeleon': bichinho = Charmeleon
elif bichinho == 'charizard': bichinho = Charizard
elif bichinho == 'bulbasaur': bichinho = Bulbasaur
elif bichinho == 'ivysaur': bichinho = Ivysaur
elif bichinho == 'venusaur': bichinho = Venusaur
elif bichinho == 'squirtle': bichinho = Squirtle
elif bichinho == 'wartortle': bichinho = Wartortle
elif bichinho == 'blastoise': bichinho = Blastoise
else:
    print('O pokemon digitado não é valido :(')






alvonome = random.choice([Charmander, Bulbasaur, Squirtle, Charmeleon, Charizard, Wartortle, Blastoise, Ivysaur, Venusaur])




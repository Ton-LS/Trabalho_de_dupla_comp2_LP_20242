import random
class Pokemon:
    def __init__(self, bichinho, vida, evolucao ,  elemento, ):
        self.bichinho = bichinho
        self.vida = vida
        self.evolucao = evolucao
        self.elemento = elemento
    def ataquebasico(self,alvo): 
        x = random.randint(1,10)
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
        Pokemon.__init__(self, bichinho = 'Charmander', vida = 100, evolucao = 1 , elemento ='Fogo')
    def Ataque_rápido_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto em cheio!')
            #alvo.vida = alvo - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto normal!')
            #alvo.vida = alvo - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Flame Burst! O ataque foi fraco!')
            #alvo.vida = alvo -3
    def Ataque_carregado_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto em cheio!')
            #alvo.vida = alvo - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto normal!')
            #alvo.vida = alvo - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi fraco!')
            #alvo.vida = alvo - 4
class Charmeleon (Charmander):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmeleon', vida = 200, evolucao = 2 , elemento ='Fogo' )
    def Ataque_rápido_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto em cheio!')
            #alvo.vida = alvo - 25
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto normal!')
            #alvo.vida = alvo - 15
        else: 
            return print(f'O {self.bichinho} utilizou o Fire Punch! O ataque foi fraco!')
            #alvo.vida = alvo -10
    def Ataque_carregado_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto em cheio!')
            #alvo.vida = alvo - 50
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto normal!')
            #alvo.vida = alvo - 25
        else: 
            return print(f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi fraco!')
            #alvo.vida = alvo - 15
class Charizard(Charmeleon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charizard', vida = 300, evolucao = 3 , elemento ='Fogo' )
    def Ataque_especial(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto em cheio!')
            #alvo.vida = alvo - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto normal!')
            #alvo.vida = alvo - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Fire Blast! O ataque foi fraco!')
            #alvo.vida = alvo - 15
class Bulbasaur(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Bulbasaur', vida = 100, evolucao = 1 , elemento ='Planta')
    def Ataque_rápido_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto em cheio!')
            #alvo.vida = alvo - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto normal!')
            #alvo.vida = alvo - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Vine Wip! O ataque foi fraco!')
            #alvo.vida = alvo -3
    def Ataque_caregado_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto em cheio!')
            #alvo.vida = alvo - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto normal!')
            #alvo.vida = alvo - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi fraco!')
            #alvo.vida = alvo - 4
class Ivysaur(Bulbasaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Ivysaur', vida = 200, evolucao = 2 , elemento ='Planta')
    def Ataque_rápido_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto em cheio!')
            #alvo.vida = alvo - 25
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto normal!')
            #alvo.vida = alvo - 15
        else: 
            return print(f'O {self.bichinho} utilizou o Solar Beam! O ataque foi fraco!')
            #alvo.vida = alvo -10
    def Ataque_carregado_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto em cheio!')
            #alvo.vida = alvo - 50
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto normal!')
            #alvo.vida = alvo - 25
        else: 
            return print(f'O {self.bichinho} utilizou o Power Wip! O ataque foi fraco!')
            #alvo.vida = alvo - 15
class Venusaur(Ivysaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Venusaur', vida = 300, evolucao = 3 , elemento ='Planta')
    def Ataque_especial(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto em cheio!')
            #alvo.vida = alvo - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto normal!')
            #alvo.vida = alvo - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi fraco!')
            #alvo.vida = alvo - 15
class Squirtle(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Squirtle', vida = 100, evolucao = 1, elemento = 'Água')
    def Ataque_rápido_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto em cheio!')
            #alvo.vida = alvo - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto normal!')
            #alvo.vida = alvo - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Bubble! O ataque foi fraco!')
            #alvo.vida = alvo -3
    def Ataque_carregado_I(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto em cheio!')
            #alvo.vida = alvo - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto normal!')
            #alvo.vida = alvo - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Water Pulse! O ataque foi fraco!')
            #alvo.vida = alvo - 4
class Wartortle(Squirtle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Wartortle', vida = 200, evolucao = 2, elemento = 'Água')
    def Ataque_rápido_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto em cheio!')
            #alvo.vida = alvo - 15
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto normal!')
            #alvo.vida = alvo - 9
        else: 
            return print(f'O {self.bichinho} utilizou o Water Gun! O ataque foi fraco!')
            #alvo.vida = alvo -3
    def Ataque_carregado_II(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto em cheio!')
            #alvo.vida = alvo - 20
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto normal!')
            #alvo.vida = alvo - 12
        else: 
            return print(f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi fraco!')
            #alvo.vida = alvo - 4
class Blastoise(Wartortle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Blastoise', vida = 300, evolucao = 3 , elemento ='Água')
    def Ataque_especial(self):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto em cheio!')
            #alvo.vida = alvo - 60
        elif 5<=x<=7:
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto normal!')
            #alvo.vida = alvo - 30
        else: 
            return print(f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi fraco!')
            #alvo.vida = alvo - 15
#======================================================================================================================
'''''
def computadormovimentos(alvonome):
    if alvonome == 'Charmander':
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')
    elif alvonome == 'Charmeleon':
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, firepunch, flamethrower]
        print(f'O {alvonome} atacou com {Charmeleon.escolhaataque}') 
    elif alvonome == 'Charizard':
        escolhaataque = random.choice[ataquebasico, flameburst, dragonrage, flamethrower, fireblast ]
        print(f'O {alvonome} atacou com {Charmander.escolhaataque}')
    elif alvonome == 'Bulbasaur':
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb]
        print(f'O {alvonome} atacou com {Bulbasaur.escolhaataque}') 
    elif alvonome == 'Ivysaur':
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb, solarbeam, powerwip]
        print(f'O {alvonome} atacou com {Ivysaur.escolhaataque}') 
    elif alvonome == 'Venusaur':
        escolhaataque = random.choice[ataquebasico, vinewip, seedbomb, solarbeam, powerwip, petalblizzard]
        print(f'O {alvonome} atacou com {Venusaur.escolhaataque}')
    elif alvonome == 'Squirtle':
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse]
        print(f'O {alvonome} atacou com {Squirtle.escolhaataque}')
    elif alvonome == 'Wartotle':
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse, watergun, aquajet]  
        print(f'O {alvonome} atacou com {Wartortle.escolhaataque}') 
    elif alvonome == 'Blastoise':
        escolhaataque = random.choice[ataquebasico, bubble, waterpulse, watergun, aquajet, hydropump]
        print(f'O {alvonome} atacou com {Blastoise.escolhaataque}')  '''

def computadormovimentos(alvonome, evolucaoPC):
    if evolucaoPC == 1:
        escolhaataque = random.randint(1,3)
        if escolhaataque == 1:
            return alvonome.ataquebasico(pokemonusuario)
        elif escolhaataque == 2:
            return alvonome.Ataque_rápido_I(pokemonusuario)
        elif escolhaataque == 3:
            return alvonome.Ataque_carregado_II(pokemonusuario)
    elif evolucaoPC == 2:
        escolhaataque = random.randint(1,5)
        if escolhaataque == 1:
            return alvonome.ataquebasico(pokemonusuario)
        elif escolhaataque == 2:
            return alvonome.Ataque_rápido_I(pokemonusuario)
        elif escolhaataque == 3:
            return alvonome.Ataque_carregado_II(pokemonusuario)
        elif escolhaataque == 4:
            return alvonome.Ataque_rápido_II(pokemonusuario)
        elif escolhaataque == 5:
            return alvonome.Ataque_carregado_II(pokemonusuario)
    elif evolucaoPC == 3:
        escolhaataque = random.randint(1,6)
        if escolhaataque == 1:
            return alvonome.ataquebasico(pokemonusuario)
        elif escolhaataque == 2:
            return alvonome.Ataque_rápido_I(pokemonusuario)
        elif escolhaataque == 3:
            return alvonome.Ataque_carregado_II(pokemonusuario)
        elif escolhaataque == 4:
            return alvonome.Ataque_rápido_II(pokemonusuario)
        elif escolhaataque == 5:
            return alvonome.Ataque_carregado_II(pokemonusuario)
        elif escolhaataque == 6:
            return alvonome.Ataque_especial(pokemonusuario)

#Mecanismo para transformaar a escolha do usuário em uma classe de pokemon válida -----------------------------------------------------------------
bichinho = input('Qual Pokemon você deseja entre Charmander, Bulbasaur ou Squirtle para lutar?')
evolucao = int(input('Qual a evolução do Pokemon inicial que você escolheu que deseja selecionar para a luta?'))
if bichinho == "Charmander":
    if evolucao == 1:
        pokemonusuario = Charmander()
        ataquespossíveis=3
    elif evolucao == 2:
        pokemonusuario = Charmeleon()
        ataquespossíveis=5
    elif evolucao == 3:
        pokemonusuario = Charizard()
        ataquespossíveis=6
elif bichinho == "squirtle":
    if evolucao == 1:
        pokemonusuario = Squirtle()
    elif evolucao == 2:
        pokemonusuario = Wartortle()
    elif evolucao == 3:
        pokemonusuario = Blastoise()
elif bichinho== "bulbasaur":
    if evolucao == 1:
        pokemonusuario = Bulbasaur()
    elif evolucao == 2:
        pokemonusuario = Ivysaur()
    elif evolucao == 3:
        pokemonusuario = Venusaur()
else:
    print("Isso não é uma resposta válida, responda seriamente ou saia desse ginásio!")


#Mecanismo para tornar a escolha do computador em classes válidas ---------------------------------------------------------------------------------
bichinhoPC = random.choice(['Charmander', 'Bulbasaur', 'Squirtle'])
evolucaoPC = random.randint(1,3)
if bichinhoPC == "Charmander":
    if evolucaoPC == 1:
        alvonome = Charmander()
        ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Charmeleon()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Charizard()
        ataquespossíveisPC =6
elif bichinhoPC == "squirtle":
    if evolucaoPC == 1:
        alvonome = Squirtle()
        ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Wartortle()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Blastoise()
        ataquespossíveisPC =6
elif bichinhoPC== "bulbasaur":
    if evolucaoPC == 1:
        alvonome = Bulbasaur()
        ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Ivysaur()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Venusaur()
        ataquespossíveisPC =6

#batalha-------------------------------------------------------------------------------------------------------------------------------------------
print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS={pokemonusuario.vida} // Número de ataques {ataquespossíveis} // Elemento{pokemonusuario.elemento} ')
print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS={alvonome.vida} // Número de ataques {ataquespossíveisPC} // Elemento{alvonome.elemento} ')
print ('A batalha começa!')

if evolucao ==  1:
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("n/O que você faz")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        movimento = int(input(f"Movimento: "))
        if movimento == 1:
            pokemonusuario.ataquebasico(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        if pokemonusuario.vida > 0:
            print("Você venceu!")
        else: print("Você foi derrotado")

elif evolucao == 2:
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("n/O que você faz")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        movimento = int(input(f"Movimento: "))
        if movimento == 1:
            pokemonusuario.ataquebasico(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 4:
            pokemonusuario.Ataque_rápido_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 5:
            pokemonusuario.Ataque_carregado_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
    if pokemonusuario.vida > 0:
            print("Você venceu!")
    else: print("Você foi derrotado")

elif evolucao == 3:
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print(f"\nO que você faz")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        movimento = int(input(f"Movimento: "))
        if movimento == 1:
            pokemonusuario.ataquebasico(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 4:
            pokemonusuario.Ataque_rápido_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 5:
            pokemonusuario.Ataque_carregado_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
        elif movimento == 6:
            pokemonusuario.Ataque_especial(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
    if pokemonusuario.vida > 0:
            print("Você venceu!")
    else: print("Você foi derrotado")
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
            alvo.vida = alvo.vida - 5
        elif 5<=x<=7:
            print('O ataque foi normal!')
            alvo.vida = alvo.vida - 3
        else: 
            print('O ataque foi fraco!')
            alvo.vida = alvo.vida -1

class Charmander(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmander', vida = 100, evolucao = 1 , elemento ='Fogo')
    def Ataque_rápido_I(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return print(f'O {self.bichinho} utilizou o Flame Burst! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -3
            return print(f'O {self.bichinho} utilizou o Flame Burst! O ataque foi fraco!')
            
    def Ataque_carregado_I(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return print(f'O {self.bichinho} utilizou o Dragon Rage! Acerto normal!')
        
        else: 
            alvo.vida = alvo.vida - 4
            return print(f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi fraco!')
            
class Charmeleon (Charmander):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charmeleon', vida = 200, evolucao = 2 , elemento ='Fogo' )
    def Ataque_rápido_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 25
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Fire Punch! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -10
            return print(f'O {self.bichinho} utilizou o Fire Punch! O ataque foi fraco!')
            
    def Ataque_carregado_II(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 50
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 25
            return print(f'O {self.bichinho} utilizou o Flame Thrower! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi fraco!')
            
class Charizard(Charmeleon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Charizard', vida = 300, evolucao = 3 , elemento ='Fogo' )
    def Ataque_especial(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 60
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return print(f'O {self.bichinho} utilizou o Fire Blast! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Fire Blast! O ataque foi fraco!')
            
class Bulbasaur(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Bulbasaur', vida = 100, evolucao = 1 , elemento ='Planta')
    def Ataque_rápido_I(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return print(f'O {self.bichinho} utilizou o Vine Wip! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -3
            return print(f'O {self.bichinho} utilizou o Vine Wip! O ataque foi fraco!')
            
    def Ataque_carregado_I(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 4
            return print(f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi fraco!')
            
class Ivysaur(Bulbasaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Ivysaur', vida = 200, evolucao = 2 , elemento ='Planta')
    def Ataque_rápido_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 25
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Solar Beam! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -10
            return print(f'O {self.bichinho} utilizou o Solar Beam! O ataque foi fraco!')
            
    def Ataque_carregado_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 50
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto em cheio!')
           
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 25
            return print(f'O {self.bichinho} utilizou o Power Wip! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Power Wip! O ataque foi fraco!')
            
class Venusaur(Ivysaur):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Venusaur', vida = 300, evolucao = 3 , elemento ='Planta')
    def Ataque_especial(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 60
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi fraco!')
            
class Squirtle(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Squirtle', vida = 100, evolucao = 1, elemento = 'Água')
    def Ataque_rápido_I(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto em cheio!')
           
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return print(f'O {self.bichinho} utilizou o Bubble! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -3
            return print(f'O {self.bichinho} utilizou o Bubble! O ataque foi fraco!')
            
    def Ataque_carregado_I(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return print(f'O {self.bichinho} utilizou o Water Pulse! Acerto normal!')
           
        else: 
            alvo.vida = alvo.vida - 4
            return print(f'O {self.bichinho} utilizou o Water Pulse! O ataque foi fraco!')
            
class Wartortle(Squirtle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Wartortle', vida = 200, evolucao = 2, elemento = 'Água')
    def Ataque_rápido_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return print(f'O {self.bichinho} utilizou o Water Gun! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida -3
            return print(f'O {self.bichinho} utilizou o Water Gun! O ataque foi fraco!')
            
    def Ataque_carregado_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return print(f'O {self.bichinho} utilizou o Aqua Jet! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 4
            return print(f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi fraco!')
            
class Blastoise(Wartortle):
    def __init__(self):
        Pokemon.__init__(self, bichinho = 'Blastoise', vida = 300, evolucao = 3 , elemento ='Água')
    def Ataque_especial(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 60
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto em cheio!')
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return print(f'O {self.bichinho} utilizou o Hydro Pump! Acerto normal!')
            
        else: 
            alvo.vida = alvo.vida - 15
            return print(f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi fraco!')
            
#======================================================================================================================

def computadormovimentos(alvonome, evolucaoPC):
    if evolucaoPC == 1:
        escolhaataque = random.randint(1,3)
        if escolhaataque == 1:
            return alvonome.ataquebasico(pokemonusuario)
        elif escolhaataque == 2:
            return alvonome.Ataque_rápido_I(pokemonusuario)
        elif escolhaataque == 3:
            return alvonome.Ataque_carregado_I(pokemonusuario)
    elif evolucaoPC == 2:
        escolhaataque = random.randint(1,5)
        if escolhaataque == 1:
            return alvonome.ataquebasico(pokemonusuario)
        elif escolhaataque == 2:
            return alvonome.Ataque_rápido_I(pokemonusuario)
        elif escolhaataque == 3:
            return alvonome.Ataque_carregado_I(pokemonusuario)
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
            return alvonome.Ataque_carregado_I(pokemonusuario)
        elif escolhaataque == 4:
            return alvonome.Ataque_rápido_II(pokemonusuario)
        elif escolhaataque == 5:
            return alvonome.Ataque_carregado_II(pokemonusuario)
        elif escolhaataque == 6:
            return alvonome.Ataque_especial(pokemonusuario)

#Mecanismo para transformaar a escolha do usuário em uma classe de pokemon válida -----------------------------------------------------------------
bichinho = input('COm qual Pokemon você deseja jogar: Charmander, Bulbasaur ou Squirtle? ')
evolucao = int(input('Qual evolução desse Pokemon você deseja usar: 1, 2 ou 3? '))
if bichinho == "Charmander":
    if evolucao == 1:
        pokemonusuario = Charmander()
        ataquespossíveis=3
    elif evolucao == 2:
        pokemonusuario = Charmeleon()
        ataquespossíveis=5
        print("Charmander evoluiu para Charmeleon")
    elif evolucao == 3:
        pokemonusuario = Charizard()
        ataquespossíveis=6
elif bichinho == "Squirtle":
    if evolucao == 1:
        pokemonusuario = Squirtle()
        ataquespossíveis = 3
    elif evolucao == 2:
        pokemonusuario = Wartortle()
        ataquespossíveis = 5
    elif evolucao == 3:
        pokemonusuario = Blastoise()
        ataquespossíveis = 6
elif bichinho== "Bulbasaur":
    if evolucao == 1:
        pokemonusuario = Bulbasaur()
        ataquespossíveis = 3
    elif evolucao == 2:
        pokemonusuario = Ivysaur()
        ataquespossíveis = 5
    elif evolucao == 3:
        pokemonusuario = Venusaur()
        ataquespossíveis = 6
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
elif bichinhoPC == "Squirtle":
    if evolucaoPC == 1:
        alvonome = Squirtle()
        ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Wartortle()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Blastoise()
        ataquespossíveisPC =6
elif bichinhoPC== "Bulbasaur":
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
print('-'*20)
print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
print("x"*9)
print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')

if evolucao ==  1:
    print ('A batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        movimento = int(input(f"Movimento: "))
        if movimento == 1:
            pokemonusuario.ataquebasico(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
    if pokemonusuario.vida > 0:
        print(f"Você venceu! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho}")
    else: print(f"Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do líder deste ginásio.")

elif evolucao == 2:
    print ('A batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        movimento = int(input(f"Movimento: "))
        if movimento == 1:
            pokemonusuario.ataquebasico(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 4:
            pokemonusuario.Ataque_rápido_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 5:
            pokemonusuario.Ataque_carregado_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
    if pokemonusuario.vida > 0:
            print(f"Você venceu!{alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho}")
    else: print(f"Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do líder deste ginásio.")

elif evolucao == 3:
    print ('A batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print(f"\nO que você faz?")
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
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 2:
            pokemonusuario.Ataque_rápido_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 3:
            pokemonusuario.Ataque_carregado_I(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 4:
            pokemonusuario.Ataque_rápido_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 5:
            pokemonusuario.Ataque_carregado_II(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
        elif movimento == 6:
            pokemonusuario.Ataque_especial(alvonome)
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"Seu {alvonome.bichinho} tem PS = {alvonome.vida}")
            print("-"*60)
    if pokemonusuario.vida > 0:
            print(f"Você venceu! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho}")
    else: print(f"Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do líder deste ginásio.")
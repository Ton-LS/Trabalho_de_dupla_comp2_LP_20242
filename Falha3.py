import random
#primeiro definimos as classes, começando pela classe Pokemon que seria "mãe" de todas as outras
#definimos como bichinho sendo o nome do pokemon, a vida respectiva a cada evolução, o numero da evolução do pokemon e o seu elemento respectivamente
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
            alvo.vida = alvo.vida - 5
            return f'O {self.bichinho} utilizou o ataque básico, ataque foi crítico!'
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 3
            return f'O {self.bichinho} utilizou o ataque básico, ataque foi normal!'
        else: 
            alvo.vida = alvo.vida -1
            return f'O {self.bichinho} utilizou o ataque básico, ataque foi fraco!'
#agora fomos para a primeira classe filha para criar um charmander, embaixo de cada ataque, tem um guia para mostrar como funciona o d10 que criamos para saber de como será o ataque 
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
            return f'O {self.bichinho} utilizou o Flame Burst! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return f'O {self.bichinho} utilizou o Flame Burst! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -3
            return f'O {self.bichinho} utilizou o Flame Burst! O ataque foi fraco!'
            
    def Ataque_carregado_I(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi normal!'
        
        else: 
            alvo.vida = alvo.vida - 4
            return f'O {self.bichinho} utilizou o Dragon Rage! O ataque foi fraco!'
#a unica diferença de uma classe pra outra dentro das evoluções são que aumentamos o numero de ataques, a primeira evolução só consegue fazer ataques nivel 1, a segunda consegue fazer ataques nivel 2 e a ultima possui um ataque especial           
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
            return f'O {self.bichinho} utilizou o Fire Punch! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Fire Punch! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -10
            return f'O {self.bichinho} utilizou o Fire Punch! O ataque foi fraco!'
            
    def Ataque_carregado_II(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 50
            return f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 25
            return f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Flame Thrower! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Fire Blast! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return f'O {self.bichinho} utilizou o Fire Blast! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Fire Blast! O ataque foi fraco!'
#agora repetimos o processo para as outras duas familias de pokemons            
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
            return f'O {self.bichinho} utilizou o Vine Wip! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return f'O {self.bichinho} utilizou o Vine Wip! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -3
            return f'O {self.bichinho} utilizou o Vine Wip! O ataque foi fraco!'
            
    def Ataque_carregado_I(self, alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 4
            return f'O {self.bichinho} utilizou o Seed Bonmb! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Solar Beam! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Solar Beam! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -10
            return f'O {self.bichinho} utilizou o Solar Beam! O ataque foi fraco!'
            
    def Ataque_carregado_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 50
            return f'O {self.bichinho} utilizou o Power Wip! O ataque foi em cheio!'
           
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 25
            return f'O {self.bichinho} utilizou o Power Wip! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Power Wip! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Petal Blizzard! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Bubble! O ataque foi em cheio!'
           
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return f'O {self.bichinho} utilizou o Bubble! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -3
            return f'O {self.bichinho} utilizou o Bubble! O ataque foi fraco!'
            
    def Ataque_carregado_I(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return f'O {self.bichinho} utilizou o Water Pulse! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return f'O {self.bichinho} utilizou o Water Pulse! O ataque foi normal!'
           
        else: 
            alvo.vida = alvo.vida - 4
            return f'O {self.bichinho} utilizou o Water Pulse! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Water Gun! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 9
            return f'O {self.bichinho} utilizou o Water Gun! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida -3
            return f'O {self.bichinho} utilizou o Water Gun! O ataque foi fraco!'
            
    def Ataque_carregado_II(self,alvo):
        x = random.randint(1,10)
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            alvo.vida = alvo.vida - 20
            return f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 12
            return f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 4
            return f'O {self.bichinho} utilizou o Aqua Jet! O ataque foi fraco!'
            
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
            return f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi em cheio!'
            
        elif 5<=x<=7:
            alvo.vida = alvo.vida - 30
            return f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi normal!'
            
        else: 
            alvo.vida = alvo.vida - 15
            return f'O {self.bichinho} utilizou o Hydro Pump! O ataque foi fraco!'
            
#======================================================================================================================
#a seguir, criamos uma função para poder escolher qual ataque o computador(Dono do ginásio) ira usar para a batalha, utilizando como artificio a biblioteca random
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
        
#Função para colocar espaçamentos
def faixa():
    print ("-"*160)
    return "-"*160

#Mecanismo para transformar a escolha do usuário em uma classe de pokemon válida -----------------------------------------------------------------
print(faixa())
print( "x"*70 , "GINÁSIO POKÉMON" , "x"*70)
print(faixa())
print("Bem Vindo! Você está no ginásio Pokémon. Aqui você vai poder escolher seu Pokemon inicial, evolui-lo ou não e batalhar com ele contra um oponente de nossa escolha. Venha e descubra quais são os ataques dos nossos Pokémons. E quem sabe você não ganha nosso líder do ginásio...")
print(faixa())
bichinho = input('Com qual Pokemon você deseja jogar: Charmander, Bulbasaur ou Squirtle? ')
evolucao = int(input('Qual evolução desse Pokemon você deseja usar: 1, 2 ou 3? '))
if bichinho == "Charmander":
    if evolucao == 1:
        pokemonusuario = Charmander()
        ataquespossíveis=3
        vida_total = 100
    elif evolucao == 2:
        pokemonusuario = Charmeleon()
        ataquespossíveis=5
        vida_total = 200
        print("Charmander evoluiu para Charmeleon.")
    elif evolucao == 3:
        pokemonusuario = Charizard()
        ataquespossíveis=6
        vida_total = 300
        print("Charmander evoluiu para Charmeleon e Charmeleon evoluiu para Charizard.")
elif bichinho == "Squirtle":
    if evolucao == 1:
        pokemonusuario = Squirtle()
        ataquespossíveis = 3
        vida_total = 100
    elif evolucao == 2:
        pokemonusuario = Wartortle()
        ataquespossíveis = 5
        vida_total = 200
        print("Squirtle evoluiu para Wartortle.")
    elif evolucao == 3:
        pokemonusuario = Blastoise()
        ataquespossíveis = 6
        vida_total = 300
        print("Squirtle evoluiu para Wartortle e Wartortle evoluiu para Blastoise.")
elif bichinho== "Bulbasaur":
    if evolucao == 1:
        pokemonusuario = Bulbasaur()
        ataquespossíveis = 3
        vida_total = 100
    elif evolucao == 2:
        pokemonusuario = Ivysaur()
        ataquespossíveis = 5
        vida_total = 200
        print("Bulbasaur evoluiu para Ivysaur.")
    elif evolucao == 3:
        pokemonusuario = Venusaur()
        ataquespossíveis = 6
        vida_total = 300
        print("Bulbasaur evoluiu para Ivysaur e IvysaurBU evoluiu para Venusaur.")
else:
    print("Isso não é uma resposta válida, responda seriamente ou saia desse ginásio!")


#Mecanismo para tornar a escolha do computador em classes válidas ---------------------------------------------------------------------------------
bichinhoPC = random.choice(['Charmander', 'Bulbasaur', 'Squirtle'])

if bichinhoPC == "Charmander":
    '''if evolucaoPC == 1:'''
    alvonome = Charmander()
    '''ataquespossíveisPC =3'''
    '''elif evolucaoPC == 2:
        alvonome = Charmeleon()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Charizard()
        ataquespossíveisPC =6'''
elif bichinhoPC == "Squirtle":
    '''if evolucaoPC == 1:'''
    alvonome = Squirtle()
    ''' ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Wartortle()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Blastoise()
        ataquespossíveisPC =6'''
elif bichinhoPC== "Bulbasaur":
    '''if evolucaoPC == 1:'''
    alvonome = Bulbasaur()
    '''ataquespossíveisPC =3
    elif evolucaoPC == 2:
        alvonome = Ivysaur()
        ataquespossíveisPC =5
    elif evolucaoPC == 3:
        alvonome = Venusaur()
        ataquespossíveisPC =6'''

#batalha-------------------------------------------------------------------------------------------------------------------------------------------
print('-'*20)
print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
print("x"*9)
ataquespossíveisPC = 3
print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')

if evolucao ==  1:
    print ('A Primeira batalha começa!')
    evolucaoPC = 1
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f" *********************** Você venceu o Baixo líder deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
        print("Você deseja evoluir ? (1)Sim (2)Não")
        resposta_evolução = input("Resposta: ")
        if (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmander"):
            pokemonusuario = Charmeleon()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Squirtle"):
            pokemonusuario = Wartortle()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Bulbasaur"):
            pokemonusuario = Ivysaur
        else: pass
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Baixo líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    if alvonome.bichinho == "Charmander":
        alvonome=Charmeleon()
    elif alvonome.bichinho == "Bulbasaur":
        alvonome=Ivysaur()
    elif alvonome.bichinho == "Squirtle":
        alvonome=Wartortle()
    print('-'*20)
    print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
    print("x"*9)
    ataquespossíveisPC = 5
    print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')
    print ('A Segunda batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f" *********************** Você venceu o Vice Líder! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
        print("Você deseja evoluir ? (1)Sim (2)Não")
        resposta_evolução = input("Resposta: ")
        if (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmander"):
            pokemonusuario = Charmeleon()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Squirtle"):
            pokemonusuario = Wartortle()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Bulbasaur"):
            pokemonusuario = Ivysaur()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmeleon"):
            pokemonusuario = Charizard()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Wartortle"):
            pokemonusuario = Blastoise()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Ivysaur"):
            pokemonusuario = Venusaur()
        else: pass
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Vice líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    if alvonome.bichinho == "Charmeleon":
        alvonome=Charizard()
    elif alvonome.bichinho == "Ivysaur":
        alvonome=Venusaur()
    elif alvonome.bichinho == "Wartortle":
        alvonome=Blastoise()
    print('-'*20)
    print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
    print("x"*9)
    ataquespossíveisPC = 5
    print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')
    print ('A Terceira batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f" *********************** Você venceu o Grande lider deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
        '''print("Você deseja evoluir ? (1)Sim (2)Não")
        if pokemonusuario.bichinho in ["Charizard","Blastoise","Venusaur"]:
            pass
        elif pokemonusuario.bichinho in ["Charmander", "Squirtle", "Bulbasaur", "Charmeleon", "Wartortle", "Ivysaur"]:
            resposta_evolução = input("Resposta: ")
            if (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmander") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmander"):
                pokemonusuario = Charmeleon()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Squirtle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Squirtle"):
                pokemonusuario = Wartortle()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Bulbasaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Bulbasaur"):
                pokemonusuario = Ivysaur()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmeleon"):
                pokemonusuario = Charizard()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Wartortle"):
                pokemonusuario = Blastoise()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Ivysaur"):
                pokemonusuario = Venusaur()
            else: pass'''
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Grande líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)

elif evolucao == 2:
    print ('A Primeira batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu o Baixo líder deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
        print("Você deseja evoluir ? (1)Sim (2)Não")
        resposta_evolução = input("Resposta: ")
        if (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmeleon"):
            pokemonusuario = Charizard()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Wartortle"):
            pokemonusuario = Blastoise()
        elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Ivysaur"):
            pokemonusuario = Venusaur()
        else: pass
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Baixo líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    if alvonome.bichinho == "Charmander":
        alvonome=Charmeleon()
    elif alvonome.bichinho == "Bulbasaur":
        alvonome=Ivysaur()
    elif alvonome.bichinho == "Squirtle":
        alvonome=Wartortle()
    print('-'*20)
    print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
    print("x"*9)
    ataquespossíveisPC = 5
    print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')
    print ('A Segunda batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu o Médio líder deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
        if pokemonusuario.bichinho in ["Charizard","Blastoise","Venusaur"]:
            pass
        else:
            print("Você deseja evoluir ? (1)Sim (2)Não")
            resposta_evolução = input("Resposta: ")
            if (resposta_evolução == "1" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Charmeleon") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Charmeleon"):
                pokemonusuario = Charizard()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Wartortle") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Wartortle"):
                pokemonusuario = Blastoise()
            elif (resposta_evolução == "1" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "Sim" and pokemonusuario.bichinho == "Ivysaur") or (resposta_evolução == "S" and pokemonusuario.bichinho == "Ivysaur"):
                pokemonusuario = Venusaur()
            else: pass
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Médio líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    print ('A Terceira batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do líder baixo deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()

elif evolucao == 3:
    print ('A Primeira batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print(f"\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu o Baixo líder! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Baixo líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    if alvonome.bichinho == "Charmander":
        alvonome=Charmeleon()
    elif alvonome.bichinho == "Bulbasaur":
        alvonome=Ivysaur()
    elif alvonome.bichinho == "Squirtle":
        alvonome=Wartortle()
    print('-'*20)
    print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
    print("x"*9)
    ataquespossíveisPC = 5
    print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')
    print ('A Segunda batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print(f"\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu o Médio líder deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Médio líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()
    if alvonome.bichinho == "Charmander":
        alvonome=Charmeleon()
    elif alvonome.bichinho == "Bulbasaur":
        alvonome=Ivysaur()
    elif alvonome.bichinho == "Squirtle":
        alvonome=Wartortle()
    print('-'*20)
    print(f'Seu Pokemon é {pokemonusuario.bichinho} Dados: PS = {pokemonusuario.vida} // Número de ataques = {ataquespossíveis} // Elemento = {pokemonusuario.elemento} ')
    print("x"*9)
    ataquespossíveisPC = 5
    print(f'O Pokemon do adversário é {alvonome.bichinho} Dados: PS = {alvonome.vida} // Número de ataques = {ataquespossíveisPC} // Elemento = {alvonome.elemento} ')
    print ('A Terceira batalha começa!')
    while pokemonusuario.vida > 0 and alvonome.vida > 0:
        print(f"\nO que você faz?")
        print("1. Ataque básico I")
        print("2. Ataque Rápido I")
        print("3. Ataque carregado I")
        print("4. Ataque Rápido II")
        print("5. Ataque carregado II")
        print("6. Golpe especial")
        print("---")
        movimento = int(input(f"Movimento: "))
        print("---")
        if movimento == 1:
            print(pokemonusuario.ataquebasico(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 2:
            print(pokemonusuario.Ataque_rápido_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 3:
            print(pokemonusuario.Ataque_carregado_I(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 4:
            print(pokemonusuario.Ataque_rápido_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 5:
            print(pokemonusuario.Ataque_carregado_II(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        elif movimento == 6:
            print(pokemonusuario.Ataque_especial(alvonome))
            print(computadormovimentos(alvonome, evolucaoPC))
            print(f"Seu {pokemonusuario.bichinho} tem PS = {pokemonusuario.vida}")
            print(f"O {alvonome.bichinho} adversário tem PS = {alvonome.vida}")
            print("-"*160)
        else: pass
    if pokemonusuario.vida > 0:
        pokemonusuario.vida = vida_total
        print("-"*160)
        print(f"*********************** Você venceu o Grande Líder deste ginásio! {alvonome.bichinho} foi derrotado por seu {pokemonusuario.bichinho} ***********************")
        print("-"*160)
        print("-"*160)
    else: 
        print("-"*160)
        print(f"*********************** Você foi derrotado! Seu {pokemonusuario.bichinho} foi derrotado pelo {alvonome.bichinho} do Grande líder deste ginásio. ***********************")
        print("Saia do ginásio")
        print("-"*160)
        print("-"*160)
        exit()

#Torneio pokemon do CT#
import random

class pokemon:
    def __init__ (self, PS):
        self.PS = 60       

#Abaixo temos as relações de vantagens entre os tipos de pokemon---------------------------------------------------------------------------------------------------------
class normal(pokemon):
    def __init__(self, PS, super_efetivo_contra=[], pouco_efetivo_contra = ["pedra","aço" ], inefetivo_contra = ["fantasma"]):
        super().__init__(PS)

class lutador(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["normal","pedra","aço","gelo","sombrio"]
        self.pouco_efetivo_contra = ["voador","venenoso", "inseto", "psíquico", "fada" ]
        self.inefetivo_contra =["fantasma"]

class voador(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["lutador", "inseto", "planta"]
        self.pouco_efetivo_contra = ["pedra", "aço", "elétrico" ]
        self.inefetivo_contra =[]

class venenoso(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["planta", "fada"]
        self.pouco_efetivo_contra = ["venenoso","terrestre", "pedra", "fantasma" ]
        self.inefetivo_contra =["aço"]

class terrestre(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["venenoso", "pedra", "aço", "fogo"]
        self.pouco_efetivo_contra = ["inseto","planta"]
        self.inefetivo_contra =["voador"]

class pedra(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["voador", "inseto", "fogo", "gelo"]
        self.pouco_efetivo_contra = ["lutador", "terrestre", "aço"]
        self.inefetivo_contra =[]

class inseto(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["planta", "psíquico", "sombrio"]
        self.pouco_efetivo_contra = ["lutador", "voador", "venenoso", "fantasma", "aço", "fogo", "fada"]
        self.inefetivo_contra =[]

class fantasma(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["fantasma", "psíquico"]
        self.pouco_efetivo_contra = ["sombrio"]
        self.inefetivo_contra =["normal"]

class aço(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["pedra", "gelo", " fada"]
        self.pouco_efetivo_contra = ["aço", "fogo", "água", "elétrico"]
        self.inefetivo_contra =[]
 
class fogo(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["inseto", "aço", "planta", "gelo"]
        self.pouco_efetivo_contra = ["pedra", "fogo", "água", "dragão"]
        self.inefetivo_contra =[]

class água(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["terrestre","pedra", "fogo"]
        self.pouco_efetivo_contra = ["água", "planta", "dragão"]
        self.inefetivo_contra =[]
  
class planta(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["terrestre", "pedra", "água"]
        self.pouco_efetivo_contra = ["voador", "venenoso", "inseto", "aço", "fogo", "planta", "dragão"]
        self.inefetivo_contra =[]

class elétrico(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["voador", "água"]
        self.pouco_efetivo_contra = ["planta", "elétrico", "dragão"]
        self.inefetivo_contra =["terrestre"]

class psíquico(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["lutador", "venenoso"]
        self.pouco_efetivo_contra = ["aço", "psíquico"]
        self.inefetivo_contra =["sombrio"]

class gelo(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["voador", "terrestre", "planta", "dragão"]
        self.pouco_efetivo_contra = ["aço", "fogo", "água"]

class dragão(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["dragão"]
        self.pouco_efetivo_contra = ["aço"]
        self.inefetivo_contra =["fada"]

class sombrio(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["aço", "psíquico"]
        self.pouco_efetivo_contra = ["lutador", "sombrio", "fada"]

class fada(pokemon):
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra):
        super().__init__(PS)
        self.super_efetivo_contra = ["lutador", "dragão", "sombrio"]
        self.pouco_efetivo_contra = ["venenoso", "aço", "fogo"]
        self.inefetivo_contra =[]

#Abaixo começamos nossa pokedex -----------------------------------------------------------------------------------------------------------------------------------------

class bulbasaur(planta, venenoso):
    ataques_possíveis = ["bomba de lama", "bomba de lodo", "chicote de vinha"]
    def __init__(self, PS, ataque):
        self.PS=float(PS)
        self.ataque = self.verificador_de_ataque(ataque)
    def verificador_de_ataque(ataque, ataques_possíveis):
        if ataque in ataques_possíveis:
            return ataque
        else:
            return "esse ataque não é desse pokemon"
        
class charmander(fogo):
    ataques_possíveis = ["brasa", "lança chamas", "rajada de chamas"]
    def __init__(self, PS, ataque):
        self.PS=float(PS)
        self.ataque = self.verificador_de_ataque(ataque)
    def verificador_de_ataque(ataque, ataques_possíveis):
        if ataque in ataques_possíveis:
            return ataque
        else:
            return "esse ataque não é desse pokemon"

class squirtle(água):
    ataques_possíveis = ["bolha", "aqua cauda", "aqua jato"]
    def __init__(self, PS, ataque):
        self.PS=float(PS)
        self.ataque = self.verificador_de_ataque(ataque)
    def verificador_de_ataque(ataque, ataques_possíveis):
        if ataque in ataques_possíveis:
            return ataque
        else:
            return "esse ataque não é desse pokemon"

class pikachu(elétrico):
    ataques_possíveis = ["choque do trovão", "descarga elétrica", "relâmpago"]
    def __init__(self, PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra, ataque):
        super().__init__(PS, super_efetivo_contra, pouco_efetivo_contra, inefetivo_contra)
        self.PS=float(PS)
        self.ataque = self.verificador_de_ataque(ataque)
    def verificador_de_ataque(ataque, ataques_possíveis):
        if ataque in ataques_possíveis:
            return ataque
        else:
            return "esse ataque não é desse pokemon"



#Abaixo tipo como serão feitas as batalhas ------------------------------------------------------------------------------------------------------------------------------

# super efetivo multiplica por 2 o dano
# pouco efetivo multiplica por 1/2 o dano
# neutro multiplica por 1 o dano
# inefetivo multiplica por 0 o dano

bichinho1 = squirtle(50,"bolha")
bichinho2 = charmander(45, "brasa")
def blbalbla (pokemon1, pokemon2):
    if str(type(pokemon2)) in pokemon1


def dano_causado(desafiante, desafiado):
    return

def batalha(desafiante, desafiado):
    def ataquebasico(self,alvo): 
        x = random.choice[1,2,3,4,5,6,7,8,9,10]
        #ataquecritico 8-10
        #ataquenormal 5-7
        #ataqueerrado 1-4
        if 8<=x<=10:
            print('O ataque foi crítico!')
            desafiado.PS = desafiado.PS - 5
        elif 5<=x<=7:
            print('O ataque foi normal!')
            desafiado.PS = desafiado.PS - 3
        else: 
            print('O ataque foi fraco!')
            desafiado.PS = desafiado.PS -1

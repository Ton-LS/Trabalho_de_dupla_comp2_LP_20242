#Tornei pokemon do CT#
class pokemon:
    def __init__ (self, PS, PC):
        self.PS = float(PS)          #Tempo de duração de curso
        self.PC = float(PC)          #Capacidade de ter um bom emprego no mercado de trabalho

#Abaixo temos as relações de vantagens entre os tipos de pokemon---------------------------------------------------------------------------------------------------------
class normal(pokemon):
    super_efetivo_contra = []
    pouco_efetivo_contra = ["pedra","aço" ]
    inefetivo_contra =["fantasma"]

class lutador(pokemon):
    super_efetivo_contra = ["normal","pedra","aço","gelo","sombrio"]
    pouco_efetivo_contra = ["voador","venenoso", "inseto", "psíquico", "fada" ]
    inefetivo_contra =["fantasma"]

class voador(pokemon):
    super_efetivo_contra = ["lutador", "inseto", "planta"]
    pouco_efetivo_contra = ["pedra", "aço", "elétrico" ]
    inefetivo_contra =[]

class venenoso(pokemon):
    super_efetivo_contra = ["planta", "fada"]
    pouco_efetivo_contra = ["venenoso","terrestre", "pedra", "fantasma" ]
    inefetivo_contra =["aço"]

class terrestre(pokemon):
    super_efetivo_contra = ["venenoso", "pedra", "aço", "fogo"]
    pouco_efetivo_contra = ["inseto","planta"]
    inefetivo_contra =["voador"]

class pedra(pokemon):
    super_efetivo_contra = ["voador", "inseto", "fogo", "gelo"]
    pouco_efetivo_contra = ["lutador", "terrestre", "aço"]
    inefetivo_contra =[]

class inseto(pokemon):
    super_efetivo_contra = ["planta", "psíquico", "sombrio"]
    pouco_efetivo_contra = ["lutador", "voador", "venenoso", "fantasma", "aço", "fogo", "fada"]
    inefetivo_contra =[]

class fantasma(pokemon):
    super_efetivo_contra = ["fantasma", "psíquico"]
    pouco_efetivo_contra = ["sombrio"]
    inefetivo_contra =["normal"]

class aço(pokemon):
    super_efetivo_contra = ["pedra", "gelo", " fada"]
    pouco_efetivo_contra = ["aço", "fogo", "água", "elétrico"]
    inefetivo_contra =[]
 
class fogo(pokemon):
    super_efetivo_contra = ["inseto", "aço", "planta", "gelo"]
    pouco_efetivo_contra = ["pedra", "fogo", "água", "dragão"]
    inefetivo_contra =[]

class água(pokemon):
    super_efetivo_contra = ["terrestre","pedra", "fogo"]
    pouco_efetivo_contra = ["água", "planta", "dragão"]
    inefetivo_contra =[]
  
class planta(pokemon):
    super_efetivo_contra = ["terrestre", "pedra", "água"]
    pouco_efetivo_contra = ["voador", "venenoso", "inseto", "aço", "fogo", "planta", "dragão"]
    inefetivo_contra =[]

class elétrico(pokemon):
    super_efetivo_contra = ["voador", "água"]
    pouco_efetivo_contra = ["planta", "elétrico", "dragão"]
    inefetivo_contra =["terrestre"]

class psíquico(pokemon):
    super_efetivo_contra = ["lutador", "venenoso"]
    pouco_efetivo_contra = ["aço", "psíquico"]
    inefetivo_contra =["sombrio"]

class gelo(pokemon):
    super_efetivo_contra = ["voador", "terrestre", "planta", "dragão"]
    pouco_efetivo_contra = ["aço", "fogo", "água"]

class dragão(pokemon):
    super_efetivo_contra = ["dragão"]
    pouco_efetivo_contra = ["aço"]
    inefetivo_contra =["fada"]

class sombrio(pokemon):
    super_efetivo_contra = ["aço", "psíquico"]
    pouco_efetivo_contra = ["lutador", "sombrio", "fada"]

class fada(pokemon):
    super_efetivo_contra = ["lutador", "dragão", "sombrio"]
    pouco_efetivo_contra = ["venenoso", "aço", "fogo"]
    inefetivo_contra =[]

#Abaixo começamos nossa pokedex -----------------------------------------------------------------------------------------------------------------------------------------

class bulbasaur(planta, venenoso):
    ataque_básico = 
    ataque1 =
    ataque2 =
    ataque3 =

class charmander(fogo):
    ataque_básico = 
    ataque1 =
    ataque2 =
    ataque3 =

class squirtle(água):
    ataque_básico = 
    ataque1 =
    ataque2 =
    ataque3 =

class pikachu(elétrico):
    ataque_básico = 
    ataque1 =
    ataque2 =
    ataque3 =



#Abaixo tipo como serão feitas as batalhas ------------------------------------------------------------------------------------------------------------------------------

# super efetivo multiplica por 2 o dano
# pouco efetivo multiplica por 1/2 o dano
# neutro multiplica por 1 o dano
# inefetivo multiplica por 0 o dano

def dano_causado(desafiante, desafiado):
    return
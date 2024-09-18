#Tornei pokemon do CT#
class pokemon:
    def __init__ (self, PS, PC):
        self.PS = float(PS)          #Tempo de duração de curso
        self.PC = float(PC)          #Capacidade de ter um bom emprego no mercado de trabalho

#STAB = Same Type Attack Bonus
# super efetivo multiplica por 2 o dano
# pouco efetivo multiplica por 1/2 o dano
# neutro multiplica por 1 o dano
# iefetivo multiplica por 0 o dano

def dano_causado(desafiante, desafiado):
    return

class normal(pokemon):
    super_efetivo_contra = []
    pouco_efetivo_contra = ["pedra","aço" ]
    inefetivo_contra =["fantasma"]
    super_vulnerável_contra = ["lutador"]
    pouco_vulnerável_contra = []
    invulnerabilidade = ["fantasma"]

class lutador(pokemon):
    super_efetivo_contra = ["normal","pedra","aço","gelo","sombrio"]
    pouco_efetivo_contra = ["voador","venenoso", "inseto", "psíquico", "fada" ]
    inefetivo_contra =["fantasma"]
    super_vulnerável_contra = ["voador", "psíquico", "fada"]
    pouco_vulnerável_contra = ["pedra", "inseto", "sombrio"]
    invulnerabilidade = []

class voador:
    super_efetivo_contra = ["lutador", "inseto", "planta"]
    pouco_efetivo_contra = ["pedra", "aço", "elétrico" ]
    inefetivo_contra =[]
    super_vulnerável_contra = ["pedra", "elétrico", "gelo"]
    pouco_vulnerável_contra = ["lutador", "inseto", "planta"]
    invulnerabilidade = ["terrestre"]

class venenoso:
    super_efetivo_contra = ["planta", "fada"]
    pouco_efetivo_contra = ["venenoso","terrestre", "pedra", "fantasma" ]
    inefetivo_contra =["aço"]
    super_vulnerável_contra = ["terrestre", "psíquico"]
    pouco_vulnerável_contra = ["lutador", "venenoso", "inseto", "planta", "fada"]
    invulnerabilidade = []
class terrestre:

class pedra:

class inseto:

class fantasma:

class aço:

class fogo:

class água:

class planta:

class elétrico:

class psíquico:

class gelo:

class dragão:

class sombrio:

class fada

    
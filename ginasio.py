import random
def computadorescolha_de_pokemon():
    pokemon_pc = random.choice["charmander", "charminio", "charizard", "squirtle", "wartortle", "blastoise", "bulbasaur", "yvisaur", "venusaur"]

print('Bem Vindo a batalha Pokemon para iniciantes!')
print("Dispomos dos 9 pokemons iniciais da pokedex para essa experiência.")
print("Depois de escolher seu pokemon e apresentá-lo para batalha você poderá comparar seus atriutos com os atributos do pokemon do oponente do líder de ginásio e poderá decidir continuar ou abandonar a luta.")
print("Uma dica importante é que pokemons tipo fogo são mais fortes contra tipo planta, tipos planta são mais fortes contra tipo água e tipos água são mais fortes contra tipos fogo")
print("Os pokemons tipo fogo são: CHARMANDER,  CHARMINION e CHARIZARD")
print("Os pokemons tipo água são: SQUIRTLE,  WARTORTLE e BLASTOISE")
print("Os pokemons tipo fogo são: BULBASAUR,  YVISAUR e VENUSAUR")

pokemon_user = str(input("Qual é o seu pokemon? ")).lower

def definidor_de_classe (pokemon_user):
    if pokemon_user == "charmander":
        return pokemon_user = charmander()
    elif pokemon_user == "charminion":
        return pokemon_user = charminion()
    elif pokemon_user == "charizard":
        return pokemon_user = charizard()
    elif pokemon_user == "squirtle":
        return pokemon_user = squirtle()
    elif pokemon_user == "wartortle":
        return pokemon_user = wartortle()
    elif pokemon_user == "blastoise":
        return pokemon_user = blastoise()
    elif pokemon_user == "bulbasaur":
        return pokemon_user = bulbasaur()
    elif pokemon_user == "yvisaur":
        return pokemon_user = yvisaur()
    elif pokemon_user == "venusaur":
        return pokemon_user = venusaur()
    else:
        return "Isso não é uma resposta válida, responda seriamente ou saia desse ginásio!"
    
print(f"Você escolheu um {pokemon_user.bichinho}")
print(f"Atributos:")
print(f"Vida ....... {pokemon_user.vida}")
print(f"Elemento ... {pokemon_user.elemento}")
print(f"Golpes: {pokemon_user.golpes}")

print(".."*20)
print("Agora conheça seu adversário.")
print(" Líder do ginásio de AlgeLinetown o sr. Goldfish")
print(f"Pokemon: {}")


import random

class Personagem:
    def __init__(self,nome , vida):
        self.nome = nome
        self.__vida = vida

    def tomar_dano(self, dano):
        self.__vida -= dano
        
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}.", end="\n \n")

    @property
    def getVida(self):
        print(f"{self.nome} tem {self.__vida} de vida.", end="\n \n")

    def atacar(self, alvo, jogador):
        if jogador.usar_energia(10):
            dano = random.randint(5, 20)
            print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano.", end="\n \n")
            alvo.tomar_dano(dano)
        else:
            x = input("""
Você não tem energia suficiente para atacar. Se não descansar agora, não poderá atacar
e continuará sendo atingido pelo inimigo.
Quer descansar? digite 's' para sim ou 'n' para não: """)
            if x == "s":
                jogador.descansar(self)
                return
            else:
                return
            
class Pontuacao:
    
    def __init__(self):
        self.__pontos = 0

    # falta terminar o exercício de getters e setters
    @__pontos.setter
    def setPontos(self, valor):
        if valor >= 0:
            return valor
        else:
            print("Pontos não podem ser negativos.")
            return 0

    def adicionar_pontos(self, quantidade):
        self.__pontos += self.setPontos(quantidade)

    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}", end="\n \n")

pontos = Pontuacao()
pontos.adicionar_pontos(10)
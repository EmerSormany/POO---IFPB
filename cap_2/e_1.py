import random

class Personagem:
    def __init__(self,nome , vida):
        self.nome = nome
        self.__vida = vida

    def tomar_dano(self, dano):
        self.__vida -= dano
        
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}.", end="\n \n")

    def mostrar_vida(self):
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
    __pontos = 0

    def adicionar_pontos(self, quantidade):
        self.__pontos += quantidade

    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}", end="\n \n")

class Inimigo():

    def __init__(self, nome, vida=100, forca=6):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    def tomar_dano(self, dano):
        self.vida -= dano

    def atacar(self, alvo):
        dano = random.randint(self.__forca - 5, self.__forca + 5)
        print(f'{self.nome} tem {self.__forca} de força', end="\n \n")
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano.", end="\n \n")
        alvo.tomar_dano(dano) 


class Jogador():
    def __init__(self, energia=100, pontos=0):
        self.__energia = energia
        self.pontos = pontos

    def usar_energia(self, quantidade):
        if self.__energia - quantidade < 0:
            print("Sem energia suficiente!", end="\n \n")

            return False
        else:
            self.__energia -= quantidade
            return True
    
    def descansar(self, valor):
        if self.__energia + valor > 100:
            self.__energia = 100
        else:
            self.__energia += valor
        print(f"Energia recuperada em {valor} pontos. Energia total {self.__energia}", end="\n \n")

heroi = Personagem("Heroi", 100)
inimigo = Inimigo("Ogro", 120, 8)
pontuacao = Pontuacao()
jogador = Jogador()

heroi.mostrar_vida()
inimigo.atacar(heroi)
pontuacao.adicionar_pontos(10)
jogador.descansar(20)

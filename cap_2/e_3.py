
import random

class Personagem:
    def __init__(self, nome, vida, defesa=50):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    def tomar_dano(self, dano):
        self.__vida -= dano

    def dizer_nome(self):
        print(f"Meu nome é {self.nome}.", end="\n \n")

    @property
    def vida(self):
        return self.__vida

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Defesa deve estar entre 0 e 100.")

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

class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca

    def tomar_dano(self, dano):
        self.vida -= dano

    def atacar(self, alvo):
        dano = random.randint(self.__forca - 5, self.__forca + 5)
        print(f'{self.nome} tem {self.__forca} de força', end="\n \n")
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano.", end="\n \n")
        alvo.tomar_dano(dano)

class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = energia
        self.pontos = pontos

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if 0 <= valor <= 100:
            self.__energia = valor
        else:
            print("Energia deve estar entre 0 e 100.")

    def usar_energia(self, valor):
        if self.__energia - valor < 0:
            print("Sem energia suficiente!", end="\n \n")
            return False
        else:
            self.__energia -= valor
            return True

    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            self.__energia = 100
        else:
            self.__energia += valor
        print(f"Energia recuperada em {valor} pontos. Energia total {self.__energia}", end="\n \n")

    def descansar(self, personagem):
        print("Descansando...")
        self.recuperar_energia(20)
        personagem.defesa += 5
        print(f"A defesa de {personagem.nome} aumentou para {personagem.defesa}", end="\n \n")

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def iniciar_jogo(self):
        print(f"{self.titulo}")
        print("Bem-vindo ao jogo!")
        print("Iniciando o jogo...")

    def mostrar_opcoes(self):
        print("Mostrando opções...")

    def sair(self):
        print("Saindo do jogo...")


p = Personagem("Arthur", 100)
print(f"Nome: {p.nome}, Vida: {p.vida}, Defesa: {p.defesa}", end="\n \n")

i = Inimigo("Dragão", 150, 30)
print(f"Nome: {i.nome}, Vida: {i.vida}, Força: {i.forca}", end="\n \n")

j = Jogador("Jogador1", 80, 0)
print(f"Nome: {j.nome}, Energia: {j.energia}, Pontos: {j.pontos}", end="\n \n")

menu = Menu("=== Batalha Épica ===")
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()

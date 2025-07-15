
import os
import sys
import time
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cap_2.e_7 import Inimigo
from cap_2.e_5 import Pontuacao



class Jogador:
    total_jogadores = 0

    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = energia
        self.pontos = pontos
        self.inventario = []
        self.aliados = []
        Jogador.total_jogadores += 1

    @classmethod
    def exibir_total_jogadores(cls):
        return cls.total_jogadores

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

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"Item {item.nome} adicionado ao inventário.", end="\n \n")

j1 = Jogador("Jogador1", 100, 0)
j2 = Jogador("Jogador2", 80, 10)
j3 = Jogador("Jogador3", 90, 5)
print(f"Total de jogadores criados: {Jogador.exibir_total_jogadores()}", end="\n \n")

class Jogo:
    dificuldade_global = 1

    def __init__(self):
        self.personagem = Personagem("Sibito", 100)
        self.inimigos = ["Goblin", "Ogro", "Esqueleto"]
        self.jogador = Jogador('Sormany', 100, Pontuacao())
        self.__dificuldade = 1

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor
        else:
            print("Dificuldade deve ser 1 (fácil), 2 (médio) ou 3 (difícil).")

    def menu(self):
        print("Menu:")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        return escolha

    def mostrar_opcoes(self):
        print("Opções:")
        print("1. Ver Pontuação")
        print("2. Ver Energia")
        print("3. Voltar ao Menu Principal")

    def mostrar_pontuacao(self):
        print(f"Pontuação: {self.jogador.pontos.pontos}")

    def mostrar_energia(self):
        print(f"Energia: {self.jogador.energia}")

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def iniciar_jogo(self):
        for nome in self.inimigos:
            inimigo = Inimigo(nome, 80, 12)
            while self.personagem.vida > 0 and inimigo.vida > 0:
                self.personagem.atacar(inimigo, self.jogador)

                if inimigo.vida <= 0:
                    print(f"{inimigo.nome} foi derrotado.")
                    print(f"{self.personagem.nome} venceu a batalha! Parabéns!", end="\n \n")
                    self.jogador.pontos.adicionar_pontos(10)
                    print(f"Você derrotou {inimigo.nome} e ganhou 10 pontos!", end="\n \n")
                    break
                
                inimigo.atacar(self.personagem)

                if self.personagem.vida <= 0:
                    print(f"{self.personagem.nome} foi derrotado.")
                    print(f"{inimigo.nome} venceu a batalha! Game Over!", end="\n \n")
                    break
                time.sleep(1)

            if self.personagem.vida <= 0:
                print("Reiniciando jogo")
                for _ in range(3):
                    print('.', end='', flush=True)
                    time.sleep(1)
                print()
                break
            else:
                x = input("""
Quer descansar antes de enfrentar o próximo inimigo? digite 's' para sim ou 'n' para não: 
Você pode descansar quantas vezes quiser.
    """)
                while x == "s":
                    self.jogador.descansar(self.personagem)
                    x = input("Quer descansar novamente? digite 's' para sim ou 'n' para não: ") 

    def executar(self):
        while True:
            self.limpar_tela()
            escolha = self.menu()

            if escolha == "1":
                self.limpar_tela()
                self.personagem = Personagem("Sibito", 100)
                self.jogador.energia = 100
                self.jogador.pontos.pontos = 0
                self.iniciar_jogo()
            elif escolha == "2":
                self.limpar_tela()
                self.mostrar_opcoes()
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    self.mostrar_pontuacao()
                elif opcao == "2":
                    self.mostrar_energia()
                else:
                    print("Opção inválida.")
            elif escolha == "3":
                print("Saindo do jogo...")
                sys.exit()
            else:
                print("Opção inválida.")

class Personagem:
    def __init__(self, nome, vida, defesa=50, forca=10):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa
        self.missoes = []

    @staticmethod
    def calcular_dano_base(forca):
        return forca * 1.3

    def tomar_dano(self, dano):
        self.__vida -= dano

    def falar(self):
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

    def adicionar_missao(self, missao):
        self.missoes.append(missao)
        print(f"Missão '{missao.nome}' adicionada ao personagem {self.nome}.", end="\n \n")

print(Personagem.calcular_dano_base(10))

class Loja:
    itens = []

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item {item.nome} adicionado à loja {self.nome}.", end="\n \n")

    def listar_itens(self):
        print(f"Itens disponíveis na loja {self.nome}:")
        for item in self.itens:
            print(f"- {item.nome}: {item.descricao} no valor de {item.preco}.", end="\n \n")

    @classmethod
    def ajustar_preco_itens(cls, fator):
        for item in cls.itens:
            item.preco *= fator
            print(f"Preço do item {item.nome} ajustado para {item.preco}.", end="\n \n")

class Item:
    def __init__(self, nome, descricao, preco):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço não pode ser negativo.")

item_1 = Item("Espada", "Uma espada afiada.", 100)
item_2 = Item("Armadura", "Uma armadura resistente.", 200)
loja = Loja("Loja do Aventureiro")
loja.adicionar_item(item_1)
loja.adicionar_item(item_2)
loja.listar_itens()
Loja.ajustar_preco_itens(1.1)  

class Fase:

    tempo_maximo = 300

    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    
    def gerar_inimigos(self):
       inimigos = [
           Inimigo("Goblin Ladrão",  50, 15),
           Inimigo("Rato Gigante", 30, 10),
       ]
       return inimigos

print(f"Tempo máximo para completar a fase: {Fase.tempo_maximo} segundos", end="\n \n")
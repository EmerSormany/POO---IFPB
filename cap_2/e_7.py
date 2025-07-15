"""
2.7 Associação, Composição e Agregação
        46 Crie uma associação entre Jogador e Arma, onde um jogador
        pode equipar uma arma para usar em combate. === FEITO
        47 Crie uma associação entre Personagem e Missao, onde um
        personagem pode aceitar múltiplas missões. === FEITO
        48 Utilize composição para que a classe Jogo tenha um Menu,
        garantindo que o menu seja criado junto com o jogo e destruído
        junto com ele. === FEITO
        49 Utilize composição para que a classe Fase tenha um conjunto
        de Inimigos, garantindo que os inimigos sejam criados e
        destruídos junto com a fase. === FEITO
        50 Utilize composição para que a classe Inventario tenha uma lista
        de Itens, garantindo que os itens pertencem exclusivamente ao
        inventário e são destruídos com ele. === FEITO
        51 Utilize agregação para que a classe Guilda tenha vários
        Jogadores, permitindo que os jogadores existam
        independentemente da guilda. === FEITO
        52 Utilize agregação para que a classe Mapa tenha várias Fases,
        onde as fases podem existir separadamente do mapa. === FEITO
        53 Utilize agregação para que a classe Loja tenha uma lista de Itens,
        permitindo que os itens existam mesmo que a loja seja fechada. === FEITO
        54 Crie uma associação entre Aliado e Jogador, onde um aliado
        pode acompanhar um jogador durante a aventura. === FEITO
        55 Crie uma composição onde a classe SistemaCombate gerencia
        um Personagem e um Inimigo, garantindo que a batalha termine
        quando o sistema de combate for encerrado. === FEITO
""" 

from e_5 import Jogador, Personagem
from e_4 import Arma, Missao, Menu, Aliado

arma = Arma("Soco Inglês")
jogador = Jogador("Guerreiro", 100, 50)
jogador.adicionar_item(arma)

heroi = Personagem("Herói", 100, 50)
missao = Missao("Resgatar Gato", "Ajude Dona Maria a encontrar seu gatinho.")
heroi.adicionar_missao(missao)


import random

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

class Fase:
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

class FaseFloresta(Fase):
    def gerar_inimigos(self):
        inimigos = [
            Inimigo("Fada das Sombras", 30, 10),
            Inimigo("Orc", 50, 15)
        ]
        return inimigos

class FaseDeserto(Fase):
    def gerar_inimigos(self):
        inimigos = [
            Inimigo("Escorpião", 45, 10),
            Inimigo("Golem de Pedra", 50, 15)
        ]
        return inimigos

fase = Fase("Portal de Chegada", "Uma fase inicial onde os jogadores se preparam para a aventura.")
for inimigo in fase.gerar_inimigos():
    print(f"Inimigo: {inimigo.nome}, Vida: {inimigo.vida}, Força: {inimigo.forca}", end="\n \n")

class Item:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

class Inventario:
    def __init__(self):
        self.__inventario = [
            Item("Poção de Cura", "Restaura 20 pontos de vida."),
            Item("Elixir de Mana", "Restaura 15 pontos de mana.")
        ]

    @property
    def inventario(self):
        return self.__inventario


inventario = Inventario()
for item in inventario.inventario:
    print(f"Item: {item.nome}, Descrição: {item.descricao}", end="\n \n")

class Guilda:
    def __init__(self, nome, descricao="Nova guilda."):
        self.__nome = nome
        self.__descricao = descricao
        self.jogadores = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado à guilda {self.nome}.", end="\n \n")

g = Guilda("Pintinho Amarelinho")
g.adicionar_jogador(jogador)

class Mapa:
    def __init__(self, nome):
        self.nome = nome
        self.fases = []

    def adicionar_fase(self, fase):
        self.fases.append(fase)
        print(f"Fase {fase.nome} adicionada ao mapa {self.nome}.", end="\n \n")

cidade = Fase("Cidade Abandonada", "Uma cidade abanconada por seus moradores por conta de ladões misteriosos.")
floresta = FaseFloresta("Floresta Encantada", "Uma floresta cheia de criaturas mágicas.")
deserto = FaseDeserto("Deserto do Trovão", "Um deserto árido e cheio de tempestades.")
mapa = Mapa("Mundo Tortuoso")
mapa.adicionar_fase(fase)
mapa.adicionar_fase(cidade)
mapa.adicionar_fase(floresta)
mapa.adicionar_fase(deserto)

class Loja:
    def __init__(self, nome):
        self.__nome = nome
        self.itens = []

    @property
    def nome(self):
        return self.__nome
    
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item {item.nome} adicionado à loja {self.nome}.", end="\n \n")

    def listar_itens(self):
        print(f"Itens disponíveis na loja {self.nome}:")
        for item in self.itens:
            print(f"- {item.nome}: {item.descricao}", end="\n \n")

loja = Loja("Loja do Aventureiro")
item_1 = Item("Espada Longa", "Uma espada longa e afiada.")
item_2 = Item("Couraça de Combate", "Uma armadura leve de couro.")
item_3 = Item("Cartola", "Um chapéu elegante.")
loja.adicionar_item(item_1)
loja.adicionar_item(item_2)
loja.adicionar_item(item_3)
loja.listar_itens()

aliado = Aliado("Gato Preto")
jogador.aliados.append(aliado)

class SistemaCombate:
    def __init__(self):
        self.personagem = Personagem("Bernabeu", 100, 50)
        self.inimigo = Inimigo("Orc Gordo", 50, 15)

    def iniciar_batalha(self):
        print(f"Iniciando batalha entre {self.personagem.nome} e {self.inimigo.nome}.", end="\n \n")
        while self.personagem.vida > 0 and self.inimigo.vida > 0:
            self.personagem.atacar(self.inimigo, jogador)
            if self.inimigo.vida <= 0:
                print(f"{self.inimigo.nome} foi derrotado!", end="\n \n")
                break
            self.inimigo.atacar(self.personagem)
            if self.personagem.vida <= 0:
                print(f"{self.personagem.nome} foi derrotado!", end="\n \n")
                break

combate = SistemaCombate()
combate.iniciar_batalha()

# as linash abaixo estão comentadas para possbilitar os testes dos códigos acima.
# as linhas abaixo respondem a questão 48, da composição do Menu com a classe Jogo.
menu = Menu("Cavernas do Dragão")
menu.exibir_menu_principal()

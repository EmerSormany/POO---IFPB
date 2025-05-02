"""
    1.2 Criando atributos e métodos usando atributos
"""

class Personagem:
    """
        6 Crie uma classe Personagem com um atributo nome e um
        método dizer_nome() que imprime "Meu nome é {nome}".
        Instancie um personagem e teste o método.

        8 Crie uma classe Personagem com um atributo vida, inicializado
        em 100. Adicione um método tomar_dano(dano), que reduz a
        vida do personagem pelo valor passado como parâmetro. Se a
        vida chegar a 0, imprima "Game Over!".
    """

    def __init__(self,nome , vida=100):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print("Game Over!", end="\n \n")
        else:
            print(f"{self.nome} tem {self.vida} de vida restante.", end="\n \n")
        
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}.", end="\n \n")  


class Pontuacao:
    """
        7 Crie uma classe Pontuacao com um atributo pontos, inicializado
        em 0, e dois métodos: adicionar_pontos(quantidade), que soma
        quantidade ao total de pontos, e mostrar_pontos(), que imprime
        a pontuação atual.
    """
    pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}", end="\n \n")


class Jogador():
    """
        9 Crie uma classe Jogador com um atributo energia, inicializado
        em 50. Adicione métodos recuperar_energia(quantidade) e
        usar_energia(quantidade). Se a energia for menor que 0,
        imprima "Sem energia suficiente!".
    """
    def __init__(self, energia=50):
        self.energia = energia

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Energia recuperada em {quantidade}. Energia total {self.energia}", end="\n \n")

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia suficiente!", end="\n \n")
        else:
            self.energia -= quantidade


class Inimigo():
    """
        10 Crie uma classe Inimigo com atributos nome e vida (inicializada
        com 100). Adicione um método atacar(alvo), onde alvo é um
        objeto da classe Personagem. Esse método deve reduzir a vida
        do alvo em 10 pontos.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo, dano):
        alvo.vida -= 10 
        # incluídpa chamada do método tomar_dano para resolução do exercício 8 na classe personagem
        alvo.tomar_dano(dano)



personagem = Personagem("Sibito")
personagem.dizer_nome()

pontos = Pontuacao()
pontos.adicionar_pontos(10)
pontos.mostrar_pontos()

jogador = Jogador()
jogador.recuperar_energia(20)
jogador.usar_energia(30)
jogador.usar_energia(50)

heroi = Personagem("Sibito")
inimigo = Inimigo("Ogro")
dano = int(input('Digite o valor do dano: '))
inimigo.atacar(heroi, dano)


"""
    1.1 Criando classes sem atributos, apenas
    métodos
"""

class Jogo:
    """
        1 Crie uma classe chamada Jogo com um método iniciar() que
        imprime "O jogo começou!". Instancie a classe e chame o
        método.
    """
    def iniciar(self):
        print("O jogo começou!")

jogo = Jogo()
jogo.iniciar()

class Personagem:
    """
        2 Crie uma classe Personagem com um método pular() que
        imprime "O personagem pulou!". Instancie um objeto dessa
        classe e chame o método.
    """
    def pular(self):
        print("Personagem pulou!")
    
personagem = Personagem()
personagem.pular()

class Inimigo():
    """
        3 Crie uma classe Inimigo com um método atacar() que imprime
        "O inimigo atacou!". Instancie um objeto e chame o método. 
    """
    def atacar(self):
        print("O inimigo atacou!")
    
inimigo = Inimigo()
inimigo.atacar()

class Pontuacao:
    """
        4 Crie uma classe Pontuacao com um método zerar_pontos() que
        imprime "Pontuação zerada!". Instancie a classe e teste o
        método.
    """
    def zerar_pontos(self):
        print("Pontuação zerada!")
    
pontuacao = Pontuacao()
pontuacao.zerar_pontos()

class Menu:
    """
        5 Crie uma classe Menu com três métodos: iniciar_jogo(),
        mostrar_opcoes(), e sair(). Cada método deve imprimir uma
        mensagem correspondente. Instancie a classe e teste os
        métodos.
    """
    def iniciar_jogo(self):
        print("Iniciando o jogo...")
    
    def mostrar_opcoes(self):
        print("Mostrando opções...")
    
    def sair(self):
        print("Saindo do jogo...")

menu = Menu()
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()

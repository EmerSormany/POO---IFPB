"""
    1.3 Avançados
        11 Simulação de Combate entre Personagem e Inimigo
        Crie um sistema básico de combate onde um personagem e um
        inimigo possam atacar um ao outro até que um deles seja
        derotado.
    • Utilize as classes Personagem e Inimigo.
    • Cada um deve ter atributos nome e vida (inicializada com
    100).
    • Adicione um método atacar(alvo), onde alvo pode ser outro
    personagem ou inimigo. O ataque reduz a vida do alvo entre 5
    e 20 pontos (valor aleatório).
    • No loop do jogo, o personagem e o inimigo se atacam
    alternadamente até que a vida de um chegue a 0. Exiba
    mensagens indicando cada ataque e o vencedor da batalha.

    12 Sistema de Pontuação e Energia no Jogo
        Crie um sistema onde o jogador pode ganhar pontos ao derrotar
        inimigos, mas precisa gerenciar sua energia para continuar jogando.
    • Use as classes Jogador, Inimigo e Pontuacao.
    • O Jogador deve ter atributos energia (começa com 100) e
    pontos (começa com 0).
    • O jogador pode derrotar um inimigo chamando
    atacar(inimigo), reduzindo sua vida até 0. Cada inimigo
    derrotado adiciona 10 pontos.
    • Criar um método descansar() no jogador, que recupera 20 de
    energia, mas não pode passar de 100.
    • O jogador perde 10 de energia a cada ataque. Se a energia
    chegar a 0, ele não pode mais atacar até descansar.

    13 Criando um Sistema de Menu Interativo
        Crie um menu onde o jogador pode iniciar o jogo, ver opções ou
        sair. Se iniciar, o jogador enfrenta inimigos até que perca ou vença.
    • Utilize a classe Menu para oferecer as opções: "1. Iniciar
    Jogo", "2. Mostrar Opções" e "3. Sair".
    • Caso escolha iniciar o jogo, um jogador enfrentará inimigos
    sucessivamente.
    • Selecione aleatoriamente entre 1 e 3 inimigos para cada
    partida.
    • Exiba o progresso do jogo e, se o jogador vencer todos os
    inimigos, mostre uma mensagem de vitória.
"""
# Decidi por copiar e colar as classes usadas neste exercício, para não ter que realizar as alterações necessárias
# ao resolvê-lo e facilitar a correção, visto que ainda não passamos pelo conteúdo de herança.
# Mesmo não sendo o ideal, pois, com isso, haverá redundância de código, o que não é uma boa prática, mas facilitará a 
# correção por parte do professor.

import random
import time
import os
import sys

class Personagem:
    def __init__(self,nome , vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano
        
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}.", end="\n \n")

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
    pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}", end="\n \n")

class Jogador():
    def __init__(self, energia=100, pontos=0):
        self.energia = energia
        self.pontos = pontos

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia suficiente!", end="\n \n")

            return False
        else:
            self.energia -= quantidade
            return True
    
    def descansar(self, personagem):
        contador = 0
        print("Descansando")
        while contador < 3:
            print('.', end='', flush=True)
            contador += 1
            time.sleep(1)
        print()
        
        personagem.vida = 100

        if self.energia + 20 > 100:
            self.energia = 100
        else:
            self.energia += 20
        print(f"Energia recuperada em 20 pontos. Energia total {self.energia}", end="\n \n")

class Inimigo():
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano.", end="\n \n")
        alvo.tomar_dano(dano) 
    
jogo = Jogo()
jogo.executar()
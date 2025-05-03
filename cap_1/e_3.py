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
    
class Jogo:
    def __init__(self):
        self.personagem = Personagem("Sibito", 100)
        self.inimigos = ["Goblin", "Ogro", "Esqueleto"]
        self.jogador = Jogador()
        self.jogador.pontos = Pontuacao()

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
        for inimigo in self.inimigos:
            inimigo = Inimigo(inimigo)
            while self.personagem.vida > 0 and inimigo.vida > 0:
                self.personagem.atacar(inimigo, self.jogador)

                if inimigo.vida <= 0:
                    print(f"{inimigo.nome} foi derrotado.")
                    print(f"{self.personagem.nome} venceu a batalha! Parabéns!", end="\n \n")
                    self.jogador.pontos.adicionar_pontos(10)
                    print(f"Você derrotou {inimigo.nome} e ganhou 10 pontos!", end="\n \n")
                    self.jogador.pontos.mostrar_pontos()
                    break
                
                inimigo.atacar(self.personagem)

                if self.personagem.vida <= 0:
                    print(f"{self.personagem.nome} foi derrotado.")
                    print(f"{inimigo.nome} venceu a batalha! Game Over!", end="\n \n")
                    break
                time.sleep(1)

            if self.personagem.vida <= 0:
                print("Reiniciando jogo")
                contador = 0
                while contador < 3:
                    print('.', end='', flush=True)
                    contador += 1
                    time.sleep(1)
                print()
                break
            else:
                x = input("""
Quer descansar antes de enfrentar o próximo inimigo? digite 's' para sim ou 'n' para não: 
Você pode descansar quantas vezes quiser.
    """)
                while True:
                    if x == "s":
                        self.jogador.descansar(self.personagem)  
                        x = input("Quer descansar novamente? digite 's' para sim ou 'n' para não: ") 
                    else:
                        break 

    def executar(self):
        while True:
            self.limpar_tela()
            escolha = self.menu()

            if escolha == "1":
                self.limpar_tela()
                self.personagem.vida = 100
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

jogo = Jogo()
jogo.executar()
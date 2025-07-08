import random
import os
import sys
import time

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
                return
            else:
                return

class Pontuacao:
    def __init__(self, pontos=0):
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor
        else:
            print("Pontos não podem ser negativos.")

    def adicionar_pontos(self, quantidade):
        if quantidade < 0:
            print("Não é possível adicionar pontos negativos.")
            return
        self.__pontos += quantidade

class Inimigo:
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

class Jogador:
    def __init__(self, energia=100, pontos=0):
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

class Jogo:
    def __init__(self):
        self.personagem = Personagem("Sibito", 100)
        self.inimigos = ["Goblin", "Ogro", "Esqueleto"]
        self.jogador = Jogador()
        self.jogador.pontos = Pontuacao()
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
            inimigo = Inimigo(nome)
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

p = Personagem("Herói", 100)
print("Vida:", p.vida)
print("Defesa:", p.defesa, end="\n \n")
p.defesa = 120
p.defesa = 80
print("Nova defesa:", p.defesa  , end="\n \n")

pt = Pontuacao()
print("Pontos iniciais:", pt.pontos)
pt.pontos = -10
pt.pontos = 20
print("Pontos atualizados:", pt.pontos, end="\n \n")

j = Jogo()
print("Dificuldade atual:", j.dificuldade)
j.dificuldade = 4
j.dificuldade = 2 
print("Nova dificuldade:", j.dificuldade)
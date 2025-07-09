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

class Jogo:
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

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def iniciar_jogo(self, jogo):
        print(f"\n{self.titulo}")
        print("Bem-vindo ao jogo!")
        print("Iniciando o jogo...\n")
        jogo.executar()

    def mostrar_opcoes(self):
        print("Mostrando opções...")

    def sair(self):
        print("Saindo do jogo...")

    def exibir_menu_principal(self, jogo):
        while True:
            print("\n" + "="*40)
            print(f"{self.titulo}")
            print("="*40)
            print("1 - Iniciar Jogo")
            print("2 - Mostrar Opções")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.iniciar_jogo(jogo)
                break
            elif opcao == "2":
                self.mostrar_opcoes()
            elif opcao == "3":
                self.sair()
                break
            else:
                print("Opção inválida. Tente novamente.")

class NPC(Personagem):
    def __init__(self, nome, vida, defesa=50):
        super().__init__(nome, vida, defesa)

    def atacar(self, alvo, jogador=None):
        print(f"NPCs não podem atacar.", end="\n \n")


class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos, bonus=5):
        super().__init__(nome, energia, pontos)
        self.bonus = bonus

    def vencer_desafio(self, pontos):
        total = pontos + self.bonus
        self.pontos += total
        print(f"Jogador Premium ganhou {total} pontos (incluindo bônus de {self.bonus})!", end="\n \n")

class JogoMultiplayer(Jogo):
    def __init__(self):
        super().__init__()
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado ao jogo.", end="\n \n")

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {}

    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva como '{valor}'.", end="\n \n")

class Arma:
    def atacar(self):
        print("Ataque neutro.")

class Espada(Arma):
    def atacar(self):
        print("Ataque com espada: cortante!")

class Arco(Arma):
    def atacar(self):
        print("Ataque com arco: perfurante!")

class Missao:
    def recompensa(self):
        print("Você foi voluntário nessa missão, participar dela é a própria recompensa.")

class MissaoPrincipal(Missao):
    def recompensa(self):
        print("Recompensa: 100 moedas e 80 de experiência!")

class MissaoSecundaria(Missao):
    def recompensa(self):
        print("Recompensa: 20 moedas e 15 de experiência!.")

class Item:
    def efeito(self):
        pass

class Pocao(Item):
    def efeito(self):
        print("Efeito: Recupera 20 de vida!")

class Equipamento(Item):
    def efeito(self):
        print("Efeito: Aumenta 10 de defesa!")

class Fase:
    def caracteristicas(self):
        print("Ambiente neutro, sem características específicas.")
    
    def gerar_inimigos(self):
        print("Gerando inimigos padrão: Goblin, Orc.")

class FaseFloresta(Fase):
    def caracteristicas(self):
        print("Fase Floresta: muitos obstáculos naturais e inimigos camuflados.")

class FaseDeserto(Fase):
    def caracteristicas(self):
        print("Fase Deserto: calor intenso e pouca água.")

class Aliado:
    def habilidade(self):
        print("Possui uma adaga.")

class Mago(Aliado):
    def habilidade(self):
        print("Lança feitiço de fogo!", end="\n \n")

class Guerreiro(Aliado):
    def habilidade(self):
        print("Golpe devastador e atordoa o alvo!", end="\n \n")



from e_4 import Jogador, Jogo, Pontuacao, Personagem, Inimigo, Menu, Fase

class NPC(Personagem):
    def __init__(self, nome, vida, defesa=50):
        super().__init__(nome, vida, defesa)

    def atacar(self, alvo, jogador=None):
        print(f"NPCs não podem atacar.", end="\n \n")

    def falar(self):
        print("Está perdido, amigo?", end="\n \n")

class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

    def atacar(self, alvo):
        super().atacar(alvo)
        print("Causou 5 de dano por envenenamento!", end="\n \n")
        alvo.tomar_dano(5)

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos, bonus=5):
        super().__init__(nome, energia, pontos)
        self.pontos.adicionar_pontos(bonus)

class JogoMultiplayer(Jogo):
    def __init__(self):
        super().__init__()
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado ao jogo.", end="\n \n")

    def iniciar_jogo(self):
        print("=== MODO MULTIPLAYER ATIVADO ===")
        print("Conecte os jogadores antes de iniciar...\n")

        while True:
            nome = input("Digite o nome do jogador (ou 'fim' para continuar): ")
            if nome.lower() == 'fim':
                break
            jogador = Jogador(nome, 100, Pontuacao())
            self.adicionar_jogador(jogador)

        if not self.jogadores:
            print("Nenhum jogador foi adicionado. Encerrando...")
            return

        for jogador in self.jogadores:
            print(f"\n--- Iniciando jogo para {jogador.nome} ---")
            self.personagem = Personagem("Sibito", 100)
            jogador.energia = 100
            jogador.pontos.pontos = 0
            self.jogador = jogador
            super().iniciar_jogo()

        print("=== Todos os jogadores jogaram ===\n")

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {}

    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva como '{valor}'.", end="\n \n")

    def mostrar_opcoes(self):
        super().mostrar_opcoes()
        
        print("4. Alterar Configuração")
        print("5. Ver Configurações Atuais")
        print("6. Voltar ao Menu Principal")

        while True:
            opcao = input("Escolha uma opção avançada (ou pressione Enter para sair): ")

            if opcao == "4":
                chave = input("Nome da configuração: ")
                valor = input("Valor da configuração: ")
                self.salvar_configuracao(chave, valor)
            elif opcao == "5":
                if self.configuracoes:
                    print("\nConfigurações atuais:")
                    for k, v in self.configuracoes.items():
                        print(f"- {k}: {v}")
                else:
                    print("Nenhuma configuração salva.")
            elif opcao == "6" or opcao == "":
                break
            else:
                print("Opção inválida. Tente novamente.")

class FaseDeserto(Fase):
    def caracteristicas(self):
        print("Fase Deserto: calor intenso e pouca água.")
    
    def gerar_inimigos(self):
        print("Gerando inimigos do deserto: Escorpião, Cobra do Deserto.")
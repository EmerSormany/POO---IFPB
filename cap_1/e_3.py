"""
    1.3 Avançados

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

""" 
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
"""

from e_2 import Personagem, Inimigo

personagem = Personagem("Sibito")
inimigo = Inimigo("Ogro")

while personagem.vida > 0 and inimigo.vida > 0:
    personagem.atacar(inimigo)
    if inimigo.vida <= 0:
        break

    inimigo.atacar(personagem)
    if personagem.vida <= 0:
        break

"""
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
"""




"""
2.6 Herança Múltipla
        42 Crie uma classe Voador com um método voar() e faça uma nova
        classe Dragao herdar tanto de Inimigo quanto de Voador,
        permitindo que ele ataque e voe.
        43 Crie uma classe Curador com um método curar() e faça a classe
        Paladino herdar tanto de Guerreiro quanto de Curador,
        permitindo que ele ataque e cure aliados.
        44 Crie uma classe MagiaElemental com um método
        lançar_magia() e faça a classe MagoElemental herdar tanto de
        Mago quanto de MagiaElemental, permitindo que ele use
        magias específicas de fogo, água, terra ou ar.
        45 Crie uma classe AnimalMontaria com um método montar() e
        faça a classe Cavaleiro herdar tanto de Guerreiro quanto de
        AnimalMontaria, permitindo que ele lute montado em uma
        criatura.
"""

from e_5 import Inimigo, Personagem 
from e_4 import Guerreiro, Mago

class Voador:
    def voar(self):
        print("O ser voador está voando!", end="\n \n")

class Dragao(Inimigo, Voador):
    pass

p = Personagem("Guerreiro", 100, 50)

d = Dragao("Fogao", 100, 50)
d.atacar(p)
d.voar()

class Curador:
    def curar(self, alvo):
        print(f"{alvo.nome} foi curado!", end="\n \n")

class Paladino(Guerreiro, Curador):
    pass

p2 = Paladino()
p2.habilidade()
p2.curar(p)

class MagiaElemental:
    def lancar_magia(self, tipo):
        print(f"Lançando magia de {tipo}!", end="\n \n")

class MagoElemental(MagiaElemental, Mago):
    pass

m = MagoElemental()
m.lancar_magia("vento")
m.habilidade()

class AnimalMontaria:
    def montar(self):
        print("Montando a criatura!", end="\n \n")

class Cavaleiro(Guerreiro, AnimalMontaria):
    pass

c = Cavaleiro()
c.habilidade()
c.montar()
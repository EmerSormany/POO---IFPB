
class Balde:
    """
    Classe geral para balde de diferentes funcionalidades

    Primeiro argumento a marca em string.
    Segundo argumento é o volume em ml(inteiro).
    Terceiro argumento é o material de construção do balde em string.
    Quarto argumento é a cor do balde em string.
    """
    
    def __init__(self, marca, volume, feito_de, cor):
        self.marca = marca
        self.volume = volume
        self.feito_de = feito_de
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor


    

balde = Balde("Stanley", 8000, "Plástico", "Branca")

balde.cor = 'preto'

print(balde.cor)

#print(f"Balde da marca {balde.marca}, com volume {balde.volume/1000} litros, construído em {balde.feito_de} e na cor {balde.cor}")
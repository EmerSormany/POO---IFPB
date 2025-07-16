from matematica.basico.operacoes import somar, multiplicar
from matematica.avancado.calculos import potencia
from imc.calculo import calcular_imc as imc

print(multiplicar(2, somar(3, 5)))
print(potencia(2, 3))

peso = int(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

print(imc(peso, altura))
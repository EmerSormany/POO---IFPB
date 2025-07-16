from util_arquivos.escrita import escrever_no_final
from util_arquivos.leitura import ler_arquivo

escrever_no_final('mensagem.txt', 'Olá, mundo!\n')
conteudo = ler_arquivo('mensagem.txt')
print(conteudo)
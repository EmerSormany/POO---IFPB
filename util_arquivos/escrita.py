def escrever_no_final(arquivo, texto):
    with open(arquivo, 'a', encoding='utf-8') as f:
        f.write(texto)
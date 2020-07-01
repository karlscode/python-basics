#!/usr/bin/python3

# Faz stream do arquivo.
# Carrega o conteúdo sob demanda.
# Enquanto o arquivo está aberto.


with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!!')

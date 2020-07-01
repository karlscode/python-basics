#!/usr/bin/python3

# Faz stream do arquivo.
# Carrega o conteúdo sob demanda.
# Enquanto o arquivo está aberto.

arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, idade: {}'.format(*registro.split(',')))

arquivo.close()

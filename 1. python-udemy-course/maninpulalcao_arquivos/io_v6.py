#!/usr/bin/python3

# Faz stream do arquivo.
# Carrega o conteúdo sob demanda.
# Enquanto o arquivo está aberto.


import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, \tIdade: {}'.format(*pessoa))

if entrada.closed:
    print('Arquivo já foi fechado!!')

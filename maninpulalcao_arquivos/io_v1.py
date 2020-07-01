#!/usr/bin/python3

# Carrega todo arquivo na memória.

arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, idade: {}'.format(*registro.split(',')))

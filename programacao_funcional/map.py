#!/usr/bin/python3
from functools import reduce

print('# DESAFIO - 01 (MAP) #')

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes = map(lambda p: p['nome'], lista_2)
so_idades = map(lambda p: p['idade'], lista_2)

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))


pessoas_list = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26},
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Arthur', 'idade': 37},
    {'nome': 'Gabriela', 'idade': 6},
    {'nome': 'Thiago', 'idade': 31},
    {'nome': 'Mariana', 'idade': 17}
]

print('\n# DESAFIO - 02 (MAP) #')

menores = filter(lambda p: p['idade'] < 18, pessoas_list)
print(list(menores))

print('\n# DESAFIO - 03 (FILTER) #')
nomes_grandes = filter(lambda p: len(p['nome']) > 6, pessoas_list)
print(list(nomes_grandes))

print('\n# DESAFIO - 04 (REDUCE) #')
soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas_list, 0)
print(soma_idades)

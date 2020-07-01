#! /usr/bin/python3

from random import randint

palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('Muito legal'):
    print(letra)

produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)


PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política.',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            break
    else:
        print('Texto autorizado: ', texto)

# DESAFIO 01


def sortear_dado():
    return randint(1, 6)


numero_secreto = -1

for numero in range(1, 7):
    numero_secreto = sortear_dado()

    if numero % 2 == 1:
        continue

    if numero == numero_secreto:
        print('ACERTOU!', numero)
        break
else:
    print('Não acertou o número!')

print(numero_secreto)

# -*- coding: utf-8 -*-
print('Olá Python!')

# Resposta do desafio:
salario = 3450.45
despesas = 2456.2

percentaul_comprometido = despesas / salario * 100
print(percentaul_comprometido)

# Desafio: Operadores Lógicos
trabalho_terca = True
trabalho_quinta = True

'''
- Confirmando os 2: TV 50" + Sorvete
- Confirmando apenas 1: TV 32" + Sorvete
- Nenhum confirmado: Ficar em casa
'''
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("TV50={} TV32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))

# Operadores ternários
esta_chovendo = True
print('Hoje estou com as roupas ' +
      ('secas.', 'molhadas.')[esta_chovendo])

print('Hoje estou com as roupas ' +
      ('molhadas.' if esta_chovendo else 'secas.'))

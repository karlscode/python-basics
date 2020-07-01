# !/usr/bin/python3
# -*- coding: latin-1 -*-
# from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
# setlocale(LC_ALL, 'pt_BR')


# Listar todos os meses do ano com 31 dias.
def mes_31():
    meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
    mes_nomes = map(lambda mes: month_name[mes], meses_31)
    juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                          mes_nomes, 'Meses com 31 dias:')
    print(juntar_meses)


if __name__ == '__main__':
    mes_31()

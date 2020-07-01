#! /usr/bin/python3
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def printArea(raio):
    print('Área do círculo: {}'.format(circulo(raio)))


def circulo(raio):
    return pi * raio ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print("{}O raio deve ser um valor numérico inteiro! {}".format(
            TerminalColor.ERRO,
            TerminalColor.NORMAL))
        sys.exit(errno.EINVAL)
    else:
        raio = int(sys.argv[1])
        printArea(raio)

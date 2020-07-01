#! /usr/bin/python3
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar a nota do aluno.")
    print("Sintaxe: {} <nota>".format(sys.argv[0][2:]))


def helpArguments():
    help()
    print("{}A nota do aluno deve ser um valor numérico inteiro! {}"
          .format(TerminalColor.ERRO, TerminalColor.NORMAL))


def conceitos(nota):
    if nota > 10:
        print('Nota inválida')
        sys.exit(errno.EPERM)

    if nota >= 9.1:
        print('Conceito A.')
    elif nota >= 8.1:
        print('Conceito A-.')
    elif nota >= 7.1:
        print('Conceito B.')
    elif nota >= 6.1:
        print('Conceito B-.')
    elif nota >= 5.1:
        print('Conceito C.')
    elif nota >= 4.1:
        print('Conceito C-.')
    elif nota >= 3.1:
        print('Conceito D.')
    elif nota >= 2.1:
        print('Conceito D-.')
    elif nota >= 1.1:
        print('Conceito E.')
    else:
        print('Conceito E-.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        helpArguments()
        sys.exit(errno.EINVAL)
    else:
        nota = int(sys.argv[1])
        conceitos(nota)

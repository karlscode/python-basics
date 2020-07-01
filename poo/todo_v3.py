#!/usr/bin/python3
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        buscar_descricao = descricao.strip().lower()
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao.strip().lower() == buscar_descricao][0]

    def listar(self):
        print(self.nome)
        for tarefa in self:
            print(f'[{"x" if tarefa.feito else " "}] - {tarefa}')
        print(f'{self} \n')

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas(s) pendentes(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefa de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.listar()

    casa.procurar('lavar prato').concluir()
    casa.listar()

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Tomate')
    mercado.listar()


if __name__ == '__main__':
    main()

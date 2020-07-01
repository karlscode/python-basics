#!/usr/bin/python3
from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    def __iadd__(self, tarefa):
        tarefa.dono = tarefa
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        try:
            buscar_descricao = descricao.strip().lower()
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao.strip().lower() == buscar_descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self._dias = dias

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, dias):
        if dias < 0:
            raise ValueError('Número de dias deve ser um valor positivo!')
        self._dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefa de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 10)
    casa.add(casa.procurar('trocar Lençóis').concluir())
    casa.listar()

    casa.procurar('lavar prato').concluir()
    casa.listar()

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Tomate')
    mercado.listar()

    try:
        print('Testando método com excessão:')
        mercado.procurar('Frutas sec').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')
    else:
        mercado.listar()


if __name__ == '__main__':
    main()

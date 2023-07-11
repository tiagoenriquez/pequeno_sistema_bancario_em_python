from datetime import date

class ContaBancaria:

    def __init__(self) -> None:
        self.saldo = 0.0
        self.movimentacoes = []
        self.data_do_ultimo_saque = date.today()
        self.qtd_saques_hoje = 0
        
    def _validar_valor_positivo(self, valor: float) -> None:
        if valor <= 0:
            raise Exception("Valor negativo")
    
    def depositar(self, valor: float) -> None:
        self._validar_valor_positivo(valor)
        self.saldo += valor
        self.movimentacoes.append(valor)
    
    def sacar(self, valor: float) -> None:
        self._validar_valor_positivo(valor)
        if valor > 500:
            raise Exception("Valor maior do que permitido para saque.")
        if valor > self.saldo:
            raise Exception("Saldo insuficiente.")
        ultimo_saque_foi_hoje = self.data_do_ultimo_saque == date.today()
        if self.qtd_saques_hoje == 3 and ultimo_saque_foi_hoje:
            raise Exception("Número máximo de saques atingido")
        self.saldo -= valor
        self.movimentacoes.append(0 - valor)
        if ultimo_saque_foi_hoje:
            self.qtd_saques_hoje += 1
        else:
            self.data_do_ultimo_saque = date.today()
            self.qtd_saques_hoje = 0
    
    def extrato(self) -> str:
        titulo = "Extrato"
        extrato = f"\n{titulo.center(len(titulo) + 2, ' ').center(80, '#')}\n\n"
        for movimentacao in self.movimentacoes:
            if movimentacao > 0:
                extrato += f"Depósito de R${movimentacao:.2f}\n"
            else:
                extrato += f"Saque    de R${0 - movimentacao:.2f}\n"
        extrato += f"\nSaldo: R${self.saldo:.2f}\n\n"
        return extrato

conta_bancaria = ContaBancaria()

def depositar() -> None:
    valor = float(input("\nInforme o valor de depósito: "))
    try:
        conta_bancaria.depositar(valor)
    except Exception as e:
        print(e)

def sacar() -> None:
    valor = float(input("\nInforme o valor de saque: "))
    try:
        conta_bancaria.sacar(valor)
    except Exception as e:
        print(e)

def extrato() -> None:
    print(f"\n{conta_bancaria.extrato()}")
    
opcao = 'a'
titulo = "Sistema Bancário"
mensagem_menu = f"\n{titulo.center(len(titulo) + 2, ' ').center(80, '#')}"
mensagem_menu += """

Digite sua opção:
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

while opcao != 'q':
    opcao = input(mensagem_menu)
    if opcao == 'd':
        depositar()
    elif opcao == 's':
        sacar()
    elif opcao == 'e':
        extrato()
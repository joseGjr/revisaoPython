from requests import options


contas = []
deposito = []
saldo = 0

def main():
    options = bool(int(input("O QUE DESEJA? CRIAR CONTA? DIGITE (1) OU SAIR DO PROGRAMA(0)")))
    while options:
        criarConta()
        verSaldo()
        options = bool(int(input("O QUE DESEJA? CRIAR CONTA? DIGITE (1) OU SAIR DO PROGRAMA(0)")))

def criarConta():
    global contas,depositos, saldo
    num_conta = int(input("DIGITE O NÚMERO DA CONTA: "))

    while num_conta in contas:
        print("CONTE JÁ EXISTENTE, DIGITE NOVAMENTE. ")
        num_conta = int(input("DIGITE O NUMERO DA CONTA: "))

    contas.append(num_conta)
    depositos =float(input("DIGITE O VALOR DO PRIMEIRO DEPOSITO: "))
    while depositos <=0:
        print("VALOR DO DEPÓSITO INVALIDO")
        float(input("DIGITE O VALOR DO SEU PRIMEIRO DEPÓSITO: "))
        depositos.append(deposito)
    saldo += depositos
def verSaldo():
    global saldo
    options = bool(int(input("DESEJA VER SEU SALDO?? (1 - SIM OU 0 - NÃO: ")))
    if options:
        print(" O SALDO DA SUA CONTA É : R$: ",saldo)
main()
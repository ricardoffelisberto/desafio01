menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if (valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Depósito inválido digite outro valor.")
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if ((not valor > limite) and (not valor > saldo) and (not numero_saques >= LIMITE_SAQUES)):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
        else:
            print("Saque inválido. Digite outro valor.")
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione a operção desejada.")
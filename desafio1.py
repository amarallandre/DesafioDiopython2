menu = """    
  
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=>  """


saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:

    opcao = input(menu)


    if opcao == "d":
        depositar = int(input("Deposite o valor: "))
        if depositar <= 0:
            print("valor inválido")
        else:
            saldo =  saldo + depositar
            extrato += f"Depósito: R$ {depositar:.2f}\n"

    elif opcao == "s":
        saque = int(input("Digite um valor: "))

        if numero_saques < LIMITE_SAQUES:
            if saque > limite:
                print("Excedeu o valor limite por saque")
            elif saque <= 0:
                print("valor invalido")
            else:
                if saque > saldo:
                    print("Você não tem saldo suficiente")
                else:
                    numero_saques += 1
                    saldo = saldo - saque
                    extrato += f"Saque:    R$ {saque:.2f}\n"
        else:
            print("Você excedeu o limite de saques")

    elif opcao == "e":
        print("Extrato")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida")









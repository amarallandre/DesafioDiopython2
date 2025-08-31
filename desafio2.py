
def menu():
    return input("""    

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] criar conta
    [lc] Listar contas
    [q] Sair

=> """)

def sacar(numero_saques, LIMITE_SAQUES, saque, saldo, limite, extrato):
    if numero_saques < LIMITE_SAQUES:
        if saque > limite:
            print("Excedeu o valor limite por saque")
        elif saque <= 0:
            print("valor invalido")
        else:
            if saque > saldo:
                print("Você não tem saldo suficiente")
            else:
                saldo = saldo - saque
                extrato += f"Saque:    R$ {saque:.2f}\n"
                numero_saques += 1
            return saldo, extrato, numero_saques

def depositar(depositar, saldo, extrato):
    if depositar <= 0:
        print("valor inválido")
    else:
        saldo = saldo + depositar
        extrato += f"Depósito: R$ {depositar:.2f}\n"
    return saldo, extrato

def exibir_extrato(extrato, saldo):
    print("Extrato")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF!")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        print(f"""
        Nome: {usuario['nome']}
        CPF: {usuario['cpf']}
        Data de Nascimento: {usuario['data_nascimento']}
        Endereço: {usuario['endereco']}
        """)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "e":
            exibir_extrato(extrato, saldo)

        elif opcao == "c":
            usuarios = criar_usuario(usuarios)

        elif opcao == "lc":
            listar_usuarios(usuarios)c

        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Operação inválida.")

main()
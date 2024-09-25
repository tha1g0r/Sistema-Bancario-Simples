import datetime

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            print('Depósito realizado!')
            print(f'Novo saldo: R$ {saldo:.2f}')
            dia_hora = datetime.datetime.now()
            extrato += f'Depósito R$ {valor:.2f} | {dia_hora.strftime('%d/%m/%Y %H:%M')}\n'
    else:
        print('Não é possível depositar valores nulos ou negativos.')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, valor_limite, numero_saques, numero_limite):
    if numero_saques < numero_limite:
        if valor > 0:
            if valor <= saldo:
                if valor <= valor_limite:
                    saldo -= valor
                    print('Saque realizado!')
                    print(f'Novo saldo: R$ {saldo:.2f}')
                    numero_saques += 1
                    dia_hora = datetime.datetime.now()
                    extrato += f'Saque R$ {valor:.2f} | {dia_hora.strftime('%d/%m/%Y %H:%M')}\n'
                else:
                    print(f'Valor limite excedido. O limite é de R$ {valor_limite:.2f} por saque.')
            else:
                print('Não há saldo suficiente disponível.')
        else:
            print('Não é possível sacar valores nulos ou negativos.')
    else:
        print(f"Limite de saques diários excedido ({numero_limite}). Tente novamente amanhã.")
    
    return saldo, extrato, numero_saques

def ver_extrato(saldo, /, *, extrato):
    print('\nExtrato:')
    if extrato != '':
        print(extrato)
    else:
        print('Sem movimentações registradas até o momento.\n')
    print(f'Saldo atual: R$ {saldo:.2f}')

def criar_usuario(usuarios):
    nome = input('Informe seu nome completo: ')
    nascimento = input('Digite sua data de nascimento (dd-mm-aa): ')
    cpf = input('Insira seu CPF: ')
    endereco = input('Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Esse usuário já está cadastrado em nossa plataforma.')
        return
    else:
        usuarios.append({'Nome': nome, 'Data de nascimento': nascimento, 'CPF': cpf, 'Endereço': endereco})
        print('Usuário cadastrado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            return usuario
        else:
            return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Insira seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada!')
        conta = {'Agência': agencia, 'Número da conta': numero_conta, 'Usuário': usuario}
        return conta
    else:
        print('Usuário não encontrado.')
        return None

def listar_contas(contas):
    print('Lista de contas:')
    print('-'*50)
    if contas:
        for conta in contas:
            print('Agência:', conta['Agência'])
            print('Nro:', conta['Número da conta'])
            print('Titular:', conta['Usuário']['Nome'])
            print('-'*50)
    else:
        print('Não existem contas em nossos registros.')

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    menu = '''
Selecione uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Nova Conta
[l] Lista de Contas
[q] Sair

=> '''

    saldo = 0
    limite = 500
    extrato = ''
    n_saques = 0
    usuarios = list()
    contas = list()
    
    while True:
        opcao = input(menu).lower()

        if opcao == 'd':
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato, n_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, valor_limite=limite, numero_saques=n_saques, numero_limite=LIMITE_SAQUES)

        elif opcao == 'e':
            ver_extrato(saldo, extrato=extrato)

        elif opcao == 'u':
            criar_usuario(usuarios)

        elif opcao == 'c':
            n_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, n_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'l':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida. Por favor, selecione novamente a operação desejada.')

main()

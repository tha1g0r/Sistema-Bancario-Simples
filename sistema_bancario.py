menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
n_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        print('Depósito')
        deposito = float(input('Valor do depósito: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito R$ {deposito:.2f}\n'
            print('Depósito realizado!')
            print(f'Novo saldo: R$ {saldo:.2f}')
        else:
            print('Não é possível depositar valores nulos ou negativos.')
    
    elif opcao == 's':
        print('Saque')
        if n_saques < LIMITE_SAQUES:
            saque = float(input('Valor do saque: '))
            if saque > 0:
                if saque <= saldo:
                    if saque <= limite:
                        saldo -= saque
                        extrato += f'Saque R$ {saque:.2f}\n'
                        print('Saque realizado!')
                        print(f'Novo saldo: R$ {saldo:.2f}')
                        n_saques += 1
                    else:
                        print(f'Valor limite excedido. O limite é de R$ {limite:.2f} por saque.')
                else:
                    print('Não há saldo suficiente disponível.')
            else:
                print('Não é possível sacar valores nulos ou negativos.')
        else:
            print(f"Limite de saques diários excedido ({LIMITE_SAQUES}). Tente novamente amanhã.")

    elif opcao == 'e':
        print('\nExtrato:')
        if extrato != '':
            print(extrato)
        else:
            print('Sem movimentações registradas até o momento.\n')
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')
import os
extrato = []
saldo = 0
total_saques = 0

def deposito():
    try:
        valor_deposito = float(input('Valor do depósito R$: '))
        global saldo
        saldo += valor_deposito
        extrato.append(f'Deposito: R$ {valor_deposito:.2f}')
        os.system('cls')
        print(f'Depósito efetuado com sucesso no valor de: R${valor_deposito:.2f}')
    except:
        os.system('cls')
        print('Por favor, use o . como separador ao invés de ,')
def consulta_saldo():
    global saldo
    print(f'O seu saldo é: R$ {saldo}')

def saque():
    try:
        valor_saque = float(input('Valor do saque R$: '))
        global saldo, total_saques
        
        if valor_saque > saldo:
            print(f'Saldo insuficiente: você têm R${saldo} na sua conta')

        if valor_saque > 500:
            print('Limite de saque diário!!')

        elif total_saques + valor_saque > 500:
            print(f'Limite de saque diário')

        else:
            total_saques += valor_saque
            saldo -= valor_saque
            extrato.append(f'Saque: R$ {valor_saque:.2f}')
            print(f'Seu saque diário é {total_saques:.2f}')
    except:
        os.system('cls')
        print('Por favor, use o . como separador ao invés de ,')

def consultar_extrato():
    global extrato, saldo
    print('=====EXTRATO DETALHADO=====')
    for i in extrato:
        print(i)
    print(f'Saldo: R${saldo:.2f}')
    input('clique para ir ao menu: ')
    os.system('cls')

    

while True:

    menu = str(input("""
    Sistema online do seu banco:
    1 - Depósito
    2 - Saque
    3 - Saldo
    4 - Extrato
    5 - Sair
    >>>>> """))

    if menu == "1":
        os.system('cls')
        deposito()
    elif menu == "2":
        os.system('cls')
        saque()
    elif menu == "3":
        os.system('cls')
        consulta_saldo()
    elif menu == "4":
        os.system('cls')
        consultar_extrato()   
    elif menu == "5":
        os.system('cls')
        print('Finalizando . . .')
        break
    else:
        os.system('cls')
        print('Por favor, escolha somente o número desejado da opção!!')

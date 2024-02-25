menu = """"

[1] Deposito
[2] Saque
[3] Extrato
[4] Encerrar

=> """

saldo = 0
limite = 500
extrato = ""
num_saques_diario = 0
limite_saques_diario = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de: R$ {valor:.2f}\n"
        
        else: 
            print ("Operacao invalida. O valor depositado deve ser maior que zero.")
        
    elif opcao == "2":
        valor = float (input("Valor desejado: "))
    
        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_saques = num_saques_diario >= limite_saques_diario

        if excede_saldo:
            print("Falha na operacao. Saldo insuficiente.")

        elif excede_limite:
            print(f"Falha na operacao. Valor do saque excede o limite de R$ {limite:.2f}.")
        
        elif excede_saques:
            print(f"Falha na operacao. Voce já atingiu o limite de {limite_saques_diario} saques diarios.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            num_saques_diario += 1

        else:
            print("Valor informado inválido")
    
    elif opcao == "3":
        print("\n Extrato:\n")
        print("Sem movimentos."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n \n fim.")

    elif opcao == "4":
        break

    else:
        print("Operacao invalida.")


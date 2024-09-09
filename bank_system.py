'''
Sistema bancário simples:

Operações: Extrato, saque e deposito

deposito: perguntar qual valor deseja depositar

saque:    permitido realizar 3 saques diarios com limite max de 500 reais p saque, caso n tenha saldo em conta,
          o sistema deve exibir uma msg informando que n é possivel sacar o dinheiro p falta de saldo.

          todos os saques e depositos devem ser armazenados em suas variaveis e exibidos no extrato.

Extrato:  listar tds os dep e saques realizados na conta. no fim da listagem deve ser exibido o saldo atual da conta.
          Os valores devem ser exibidos utilizando formato R$ xxxx.xx

'''

menu_conta = """
   =========== MENU : CONTA CORRENTE =========

   1 - Depositar
   2 - Sacar
   3 - Extrato
   0 - Sair

   ============================================

   A seguir digite o Nº das opção do menu: => """
saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
limite_saques = 3



while True:
    opcao = int(input(menu_conta))

    if opcao == 1:        
      valor = float(input("\n   Entre com o valor a depositar: "))

      if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"   seu saldo é de R$ {saldo:.2f}")
      else:
        print("   Operação inválida! o valor informado não é permitido.")

    elif opcao == 2:
       valor_saque = float(input("\n   Entre com o valor a sacar: "))
       if numero_saques < 3:
        if valor_saque <= saldo:
          if valor_saque <= limite_por_saque:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"   seu saldo é de R$ {saldo:.2f}")
          else:
           print(f"   Operação não permitida! Seu limite de saque é {limite_por_saque}.")
        else:
         print("   Você não tem saldo suficiente para esta operação!")
         print(f"   seu saldo é de R$ {saldo:.2f}")
       else:
         print("   Operação não permitida! Você excedeu a quantidade de saques permitida!")
    elif opcao == 3:
        print("\n=====================  EXTRATO  ========================")
        print("\n   Não houve movimentação em sua conta!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n========================================================")

    elif opcao == 0:
        print("   Obrigado por acessar nosso sistema!")
        break
    else:
      print("   Operação inválida, por favor selecione outro valor do menu.")
tipo_conta = int(input("Digite (1) para Conta Normal\nDigite (2) para Conta Universitária\nDigite (3) para Conta Especial\nInsira o tipo de conta: "))

if tipo_conta == 1:
    
    conta_normal = True
    conta_universitaria = False
    conta_especial = False

elif tipo_conta == 2:
    
    conta_universitaria = True
    conta_especial = False
    conta_normal = False

elif tipo_conta == 3:

    conta_especial = True
    conta_normal = False
    conta_universitaria = False

else:
    
    print("O sistema não identificou o seu tipo de conta. Por favor entre em contato com o seu gerente.")

#conta_normal = True
#conta_universitaria = False
#conta_especial = False

valor_saque = int(input("Digite o valor que deseja sacar: "))
saque = valor_saque

saldo = 2000
chaque_especial = 450
    
if conta_normal:
    
    if saque <= saldo:
        imprime_saque = str(saque)
        print("Saque no valor de R$ " +imprime_saque+" realizado com sucesso.")
    
    elif saque <= (saldo + chaque_especial):
        print("Saque realizado com o uso do cheque especial.")
    
    else:
        print("Você não tem saldo suficiente.")

elif conta_universitaria:

    if saque <= saldo:
        print("Saque reaalizado com sucesso.")

    else:
        print("Você não tem saldo suficiente.")

elif conta_especial:
    print("Conta Especial Selecionada.")

else:
    print("O sistema não identificou o seu tipo de conta. Por favor entre em contato com o seu gerente.")

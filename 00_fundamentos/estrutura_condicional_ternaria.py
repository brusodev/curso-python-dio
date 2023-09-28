saldo = 2000
saque = 2200

status = "Sucesso" if saque <= saldo else "Falha"

print(f"{status} ao realizar o saque!")


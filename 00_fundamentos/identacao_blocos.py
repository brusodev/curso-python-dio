def sacar(valor):
    saldo = 800

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa")

    print("Obrigado por se nosso cliente, tenha um bom dia!")

sacar(1000)

def depositar(valor):
    saldo = 500
    saldo += valor

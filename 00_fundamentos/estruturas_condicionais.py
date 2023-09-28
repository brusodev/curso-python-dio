
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você já pode tirar a Carteira de Habilitação!")

if idade < MAIOR_IDADE:
    print("Você ainda não pode tirar a Carteira de Habilitação!")


if idade >= MAIOR_IDADE:
    print("Você já pode tirar a Carteira de Habilitação!")
else:
    print("Você ainda não pode tirar a Carteira de Habilitação!")


if idade >= MAIOR_IDADE:
    print("Você já pode tirar a Carteira de Habilitação!")
elif idade == IDADE_ESPECIAL:
    print("Você pode realizar aulas teórica, mas não pode realizar aulas práticas!")
else:
    print("Você ainda não pode tirar a Carteira de Habilitação!")


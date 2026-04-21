# EXERCÍCIO 4

print("=" * 40)
print("     MENU DE INVESTIMENTO   ")
print("=" * 40)
print("Escolha o tipo de investimento:")
print("1- CDB")
print("2- LCI")
print("3- LCA")
print("=" * 40)

# LOOP até digitar certo
while True:
    tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

    if tipo in [1, 2, 3]:
        break
    else:
        print("Tipo de investimento inválido! Tente novamente.\n")

# Continua o programa normal
valor = float(input("Digite o valor a ser resgatado: "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

imposto = 0

# Se for CDB
if tipo == 1:
    if dias <= 180:
        aliquota = 0.225
    elif dias <= 360:
        aliquota = 0.20
    elif dias <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15

    imposto = valor * aliquota

# LCI e LCA são isentos
else:
    imposto = 0

print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
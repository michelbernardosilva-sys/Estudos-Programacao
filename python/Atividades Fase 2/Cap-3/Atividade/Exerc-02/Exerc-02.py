# EXERCÍCIO 2
# valor do carro
valor = float(input("Digite o preço do carro: "))

# À vista 20% de desconto
preco_vista = valor * 0.8
print(f"O preço final à vista com desconto 20% é:R$ {preco_vista:.2f}")

# Parcelas e acréscimos
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
acrescimos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Loop
for i in range(len(parcelas)):
    qtd = parcelas[i]
    acrescimo = acrescimos[i]

    preco_final = valor * (1 + acrescimo / 100)
    valor_parcela = preco_final / qtd

    print(f"O preço final parcelado em {qtd} X é de R$ {preco_final:.2f} com parcelas de R$ {valor_parcela:.2f}")
# EXERCÍCIO 3

valor = float(input("Digite o valor da dívida: "))

# Tabela de parc. e juros

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

print()

# Loop para  tabela
for i in range(len(parcelas)):
    qtd = parcelas[i]
    taxa = juros[i]

    valor_juros = valor * taxa / 100
    total = valor + valor_juros
    valor_parcela = total / qtd

    print(f"Total: R$ {total:.2f} | Juros: R$ {valor_juros:.2f} | Número de parcelas: {qtd} | Valor da parcela: R$ {valor_parcela:.2f}")
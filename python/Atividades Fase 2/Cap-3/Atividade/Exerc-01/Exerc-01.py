# EXERCÍCIO 1
# Contador de votos

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

print("=" * 45)
print("BIDU — Votação: Qual o Melhor dia para a Live")
print("=" * 45)

# Quantidade de colaboradores
qtd = int(input(" # Informe quantos colaboradores vão votar? "))

# Loop de votação
for i in range(qtd):

    while True:  #  Repeti até digitar certo
        voto = input(f"Colaborador {i+1}, escolha um dia (segunda, terca, quarta, quinta, sexta): ").lower()

        if voto == "segunda":
            segunda += 1
            break
        elif voto == "terca":
            terca += 1
            break
        elif voto == "quarta":
            quarta += 1
            break
        elif voto == "quinta":
            quinta += 1
            break
        elif voto == "sexta":
            sexta += 1
            break
        else:
            print(" Voto inválido! Digite novamente.")

# Saber o maior número de votos
maior = max(segunda, terca, quarta, quinta, sexta)

# Quais dias tiveram esse maior valor
dias_vencedores = []

if segunda == maior:
    dias_vencedores.append("segunda-feira")
if terca == maior:
    dias_vencedores.append("terça-feira")
if quarta == maior:
    dias_vencedores.append("quarta-feira")
if quinta == maior:
    dias_vencedores.append("quinta-feira")
if sexta == maior:
    dias_vencedores.append("sexta-feira")

# Resultado
print("\nResultado da votação:")

if len(dias_vencedores) == 1:
    print(f" O dia escolhido foi: {dias_vencedores[0]}")
else:
    print("Teve empate entre os dias:", ", ".join(dias_vencedores))
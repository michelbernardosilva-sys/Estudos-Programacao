# Exercício 005 - Lista de Nomes
# Objetivo: Praticar listas, append e loops

nomes = []

print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"Nome {i+1}: ")
    nomes.append(nome)

print("\nNomes em ordem alfabética:")
for nome in sorted(nomes):
    print(f"  - {nome}")

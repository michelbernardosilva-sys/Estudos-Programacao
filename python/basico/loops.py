# ============================================
# Tema: Loops (for e while) em Python
# ============================================

# Loop for numa lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Loop for com range
for i in range(1, 6):   # de 1 até 5
    print(f"Número: {i}")

# Loop while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

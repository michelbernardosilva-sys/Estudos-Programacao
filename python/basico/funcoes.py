# ============================================
# Tema: Funções em Python
# ============================================

# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# Função com valor padrão
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(3))      # 9  → 3²
print(potencia(2, 3))   # 8  → 2³

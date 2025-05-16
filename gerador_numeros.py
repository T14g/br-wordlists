import random

# Padrões numéricos comuns no Brasil
padroes_comuns = [
    "123456789", "987654321", "111111111", "000000000", "222222222",
    "123123123", "456456456", "789789789", "147258369", "159753486",
    "123456780", "1234567890", "101010101", "202020202", "314159265",
    "123321123", "12344321", "321321321", "112233445", "121212121"
]

# Gerar senhas aleatórias numéricas entre 8 e 13 dígitos
def gerar_senhas_numericas(n):
    senhas = set(padroes_comuns)
    while len(senhas) < n:
        senha = ''.join(random.choices("0123456789", k=random.randint(8, 13)))
        senhas.add(senha)
    return list(senhas)

# Gerar 1000 senhas e salvar em arquivo
senhas = gerar_senhas_numericas(1000)
with open("senhas_numericas_brasil.txt", "w") as f:
    for senha in senhas:
        f.write(senha + "\n")

print("Arquivo gerado: senhas_numericas_brasil.txt")

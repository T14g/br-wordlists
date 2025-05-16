import random

# Palavras em português relacionadas a budismo, yoga e espiritualidade
bases_portugues = [
    "meditacao", "karma", "nirvana", "chakras", "yoga", "mantra",
    "samadhi", "dharma", "sutra", "bodhisattva", "buda", "moksha",
    "omnamah", "pranayama", "mudra", "vipassana", "mandala", "samsara",
    "atencao", "shanti", "bhakti", "ahimsa", "tantra",
    "lotus", "paz", "sangha", "ashtanga", "vajra",
    "yogini", "prana", "meditador", "buddhismo",
    "despertar", "pazinterior", "felicidade", "espiritual", "transcender",
    "serenidade", "iluminacao", "sagrado", "equilibrio", "liberdade",
    "consciencia", "harmonia", "alma", "universo", "gratidao", "amor",
    "verdade", "compaixao", "presenca", "fluxoenergia", "podermente",
]

def gerar_senhas_portugues(n):
    senhas = set()
    while len(senhas) < n:
        base = random.choice(bases_portugues)
        sufixo = str(random.randint(1000, 99999))
        senha = base + sufixo
        if len(senha) > 8:
            senhas.add(senha)
    return list(senhas)

senhas = gerar_senhas_portugues(1000)

with open("senhas_budismo_yoga_ptbr.txt", "w", encoding="utf-8") as f:
    for senha in senhas:
        f.write(senha + "\n")

print("Arquivo 'senhas_budismo_yoga_ptbr.txt' criado com sucesso!")

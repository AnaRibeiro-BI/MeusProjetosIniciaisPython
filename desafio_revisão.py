# Início do programa
print("--- Sistema de Análise de Candidatos para Emprego ---")
print("Por favor, insira as informações do candidato:")

# Pedir e armazenar o Nome (str)
nome_candidato = input("Nome do Candidato: ")

# edir a Idade e convertê-la para int (com validação)
while True:
    try:
        idade = int(input("Idade (em anos): "))
        if idade < 0:
            print("A idade não pode ser negativa. Por favor, digite novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro para a idade.")

# Pedir a Experiência em anos e convertê-la para float (com validação)
while True:
    try:
        experiencia = float(input("Experiência (em anos, ex: 3.5): "))
        if experiencia < 0:
            print("A experiência não pode ser negativa. Por favor, digite novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número decimal para a experiência.")

# Perguntar se o candidato Possui Habilidade-Chave (com validação de entrada)
while True:
    habilidade_chave = input("Possui Habilidade-Chave? (sim/não): ").strip().lower()
    if habilidade_chave in ["sim", "não"]:
        possui_habilidade = (habilidade_chave == "sim")  # Converte para True ou False
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

# Exibir as informações coletadas
print(f"\n--- Analisando Candidatura de {nome_candidato} ---")

# Lógica de Classificação usando if-elif-else para determinar o status
if idade >= 25 and experiencia >= 3.0 and possui_habilidade:
    status = "ACEITO"
elif idade >= 25 or experiencia >= 3.0:
    status = "PENDENTE"
else:
    status = "REJEITADO"

# Exibir o resultado final
print(f"Status da Candidatura para {nome_candidato}: {status}")
print("--------------------------------------------------")

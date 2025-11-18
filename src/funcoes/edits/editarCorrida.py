import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "corridas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        return []

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as file:
        return json.load(file)


# Função para guardar o JSON
def guardar_dados(dados):
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar uma corrida
def editar_corrida():
    dados = carregar_dados()

    if not dados:
        print("Nenhuma corrida encontrada.")
        return

    print("\n=== corridas Disponíveis ===")
    for corrida in dados:
        print(f"- {corrida['nome']}")

    nome = input("\nDigite o nome da corrida que deseja editar: ")

    # Procurar corrida pelo nome
    corrida_encontrada = None
    for corrida in dados:
        if corrida["nome"].lower() == nome.lower():
            corrida_encontrada = corrida
            break

    if not corrida_encontrada:
        print("corrida não encontrada!")
        return

    print("\n=== Campos editáveis ===")
    for chave in corrida_encontrada.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in corrida_encontrada:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {corrida_encontrada[campo]}): ")

    corrida_encontrada[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")


# editar_corrida()
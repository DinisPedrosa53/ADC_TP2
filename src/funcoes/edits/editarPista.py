import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "pistas.json"
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


# Função para editar uma pista
def editar_pista():
    dados = carregar_dados()

    if not dados:
        print("Nenhuma pista encontrada.")
        return

    print("\n=== Pistas Disponíveis ===")
    for pista in dados:
        print(f"- {pista['nome']}")

    nome = input("\nDigite o nome da pista que deseja editar: ")

    # Procurar pista pelo nome
    pista_encontrada = None
    for pista in dados:
        if pista["nome"].lower() == nome.lower():
            pista_encontrada = pista
            break

    if not pista_encontrada:
        print("Pista não encontrada!")
        return

    print("\n=== Campos editáveis ===")
    for chave in pista_encontrada.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in pista_encontrada:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {pista_encontrada[campo]}): ")

    pista_encontrada[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")


# editar_pista()
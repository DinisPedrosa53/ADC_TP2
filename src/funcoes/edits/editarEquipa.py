import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "equipas.json"
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


# Função para editar uma equipa
def editar_equipa():
    dados = carregar_dados()

    if not dados:
        print("Nenhuma equipa encontrada.")
        return

    print("\n=== Equipas Disponíveis ===")
    for equipa in dados:
        print(f"- {equipa['nome']}")

    nome = input("\nDigite o nome da equipa que deseja editar: ")

    # Procurar equipa pelo nome
    equipa_encontrada = None
    for equipa in dados:
        if equipa["nome"].lower() == nome.lower():
            equipa_encontrada = equipa
            break

    if not equipa_encontrada:
        print("Equipa não encontrada!")
        return

    print("\n=== Campos editáveis ===")
    for chave in equipa_encontrada.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in equipa_encontrada:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {equipa_encontrada[campo]}): ")

    equipa_encontrada[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")


# editar_equipa()
import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "membros_equipas.json"
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


# Função para editar um membro de equipa
def editar_membro_equipa():
    dados = carregar_dados()

    if not dados:
        print("Nenhum membro de equipa encontrado.")
        return

    print("\n=== CHEFES DE EQUIPAS Disponíveis ===")
    for membro_equipa in dados:
        print(f"- {membro_equipa['nome']}")

    nome = input("\nDigite o nome do membro de equipa que deseja editar: ")

    # Procurar membro de equipa pelo nome
    membro_equipa_encontrado = None
    for membro_equipa in dados:
        if membro_equipa["nome"].lower() == nome.lower():
            membro_equipa_encontrado = membro_equipa
            break

    if not membro_equipa_encontrado:
        print("membro de equipa não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in membro_equipa_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in membro_equipa_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {membro_equipa_encontrado[campo]}): ")

    membro_equipa_encontrado[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")

#editar_membro_equipa()
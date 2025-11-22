import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "membro_equipas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_membros():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        return []

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as file:
        return json.load(file)


# Função para guardar o JSON
def guardar_membros(dados):
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar membro da equipa
def editar_membro():
    dados = carregar_membros()

    if not dados:
        print("Nenhum membro de equipa encontrado.")
        return

    print("\n=== Membros Disponíveis ===")
    for membro in dados:
        print(f"- {membro['nome']}")

    nome = input("\nDigite o nome do membro que deseja editar: ")

    # Procurar membro pelo nome
    membro_encontrado = None
    for membro in dados:
        if membro["nome"].lower() == nome.lower():
            membro_encontrado = membro
            break

    if not membro_encontrado:
        print("Membro não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in membro_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ").strip()

    if campo not in membro_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {membro_encontrado[campo]}): ")

    membro_encontrado[campo] = novo_valor

    guardar_membros(dados)

    print("\nDados atualizados com sucesso!")

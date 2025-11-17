import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "pilotos.json"
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


# Função para editar um piloto
def editar_piloto():
    dados = carregar_dados()

    if not dados:
        print("Nenhum piloto encontrada.")
        return

    print("\n=== Pilotos Disponíveis ===")
    for piloto in dados:
        print(f"- {piloto['nome']}")

    nome = input("\nDigite o nome do piloto que deseja editar: ")

    # Procurar piloto pelo nome
    piloto_encontrado = None
    for piloto in dados:
        if piloto["nome"].lower() == nome.lower():
            piloto_encontrado = piloto
            break

    if not piloto_encontrado:
        print("Piloto não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in piloto_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in piloto_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {piloto_encontrado[campo]}): ")

    piloto_encontrado[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")

#editar_piloto()
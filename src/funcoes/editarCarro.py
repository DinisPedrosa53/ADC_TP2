import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "carros.json"
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


# Função para editar um carro
def editar_carro():
    dados = carregar_dados()

    if not dados:
        print("Nenhum carro encontrada.")
        return

    print("\n=== carros Disponíveis ===")
    for carro in dados:
        print(f"- {carro['nome']}")

    nome = input("\nDigite o nome do carro que deseja editar: ")

    # Procurar carro pelo nome
    carro_encontrado = None
    for carro in dados:
        if carro["nome"].lower() == nome.lower():
            carro_encontrado = carro
            break

    if not carro_encontrado:
        print("carro não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in carro_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in carro_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {carro_encontrado[campo]}): ")

    carro_encontrado[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")

#editar_carro()
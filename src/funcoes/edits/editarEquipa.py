import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "equipas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    """
    Carrega a lista de equipas do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `equipas.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando as equipas.
    """
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        return []

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as file:
        return json.load(file)


# Função para guardar o JSON
def guardar_dados(dados):
    """
    Guarda a lista de equipas no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando as equipas.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar uma equipa
def editar_equipa():
    """
    Permite editar os dados de uma equipa específica armazenada no ficheiro JSON.

    Esta função realiza os seguintes passos:
        1. Carrega a lista de equipas usando `carregar_dados()`.
        2. Exibe todas as equipas disponíveis.
        3. Solicita ao utilizador o nome da equipa que deseja editar.
        4. Procura a equipa pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo na equipa correspondente.
        9. Guarda a lista atualizada usando `guardar_dados()`.
       10. Exibe mensagem de confirmação de atualização.

    Se a equipa não for encontrada ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
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
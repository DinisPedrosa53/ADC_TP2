import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "pistas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    """
    Carrega a lista de pistas do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `pistas.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando as pistas.
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
    Guarda a lista de pistas no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando as pistas.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar uma pista
def editar_pista():
    """
    Permite editar os dados de uma pista específica armazenada no ficheiro JSON.

    A função realiza os seguintes passos:
        1. Carrega a lista de pistas usando `carregar_dados()`.
        2. Exibe todas as pistas disponíveis.
        3. Solicita ao utilizador o nome da pista que deseja editar.
        4. Procura a pista pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo na pista correspondente.
        9. Guarda a lista atualizada usando `guardar_dados()`.
       10. Exibe mensagem de confirmação de atualização.

    Se a pista não for encontrada ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
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
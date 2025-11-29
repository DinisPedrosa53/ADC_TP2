import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "corridas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    """
    Carrega a lista de corridas do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `corridas.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando as corridas.
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
    Guarda a lista de corridas no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando as corridas.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar uma corrida
def editar_corrida():
    """
    Permite editar os dados de uma corrida específica armazenada no ficheiro JSON.

    Esta função realiza os seguintes passos:
        1. Carrega a lista de corridas usando `carregar_dados()`.
        2. Exibe todas as corridas disponíveis.
        3. Solicita ao utilizador o nome da corrida que deseja editar.
        4. Procura a corrida pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo na corrida correspondente.
        9. Guarda a lista atualizada usando `guardar_dados()`.
       10. Exibe mensagem de confirmação de atualização.

    Se a corrida não for encontrada ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
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
import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "utilizadores.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_utilizadores():
    """
    Carrega a lista de utilizadores do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `utilizadores.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando os utilizadores.
    """
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        return []

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as file:
        return json.load(file)


# Função para guardar o JSON
def guardar_utilizadores(dados):
    """
    Guarda a lista de utilizadores no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando os utilizadores.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar um utilizador
def editar_utilizador():
    """
    Permite editar os dados de um utilizador específico armazenado no ficheiro JSON.

    A função realiza os seguintes passos:
        1. Carrega a lista de utilizadores usando `carregar_utilizadores()`.
        2. Exibe todos os utilizadores disponíveis.
        3. Solicita ao utilizador o nome do utilizador que deseja editar.
        4. Procura o utilizador pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo no utilizador correspondente.
        9. Guarda a lista atualizada usando `guardar_utilizadores()`.
       10. Exibe mensagem de confirmação de atualização.

    Se o utilizador não for encontrado ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
    dados = carregar_utilizadores()

    if not dados:
        print("Nenhum utilizador encontrado.")
        return

    print("\n=== Utilizadores Disponíveis ===")
    for user in dados:
        print(f"- {user['nome']}")

    nome = input("\nDigite o nome do utilizador que deseja editar: ")

    # Procurar utilizador pelo nome
    user_encontrado = None
    for user in dados:
        if user["nome"].lower() == nome.lower():
            user_encontrado = user
            break

    if not user_encontrado:
        print("Utilizador não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in user_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in user_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(
        f"Novo valor para '{campo}' (atual: {user_encontrado[campo]}): "
    )

    user_encontrado[campo] = novo_valor

    guardar_utilizadores(dados)

    print("\nDados atualizados com sucesso!")

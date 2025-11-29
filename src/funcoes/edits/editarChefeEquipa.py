import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "chefes_equipas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    """
    Carrega a lista de chefes de equipa do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `chefes_equipas.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando os chefes de equipa.
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
    Guarda a lista de chefes de equipa no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando os chefes de equipa.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar um chefe de equipa
def editar_chefe_equipa():
    """
    Permite editar os dados de um chefe de equipa específico armazenado no ficheiro JSON.

    Esta função realiza os seguintes passos:
        1. Carrega a lista de chefes de equipa usando `carregar_dados()`.
        2. Exibe todos os chefes de equipa disponíveis.
        3. Solicita ao utilizador o nome do chefe de equipa que deseja editar.
        4. Procura o chefe de equipa pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo no chefe de equipa correspondente.
        9. Guarda a lista atualizada usando `guardar_dados()`.
       10. Exibe mensagem de confirmação de atualização.

    Se o chefe de equipa não for encontrado ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
    dados = carregar_dados()

    if not dados:
        print("Nenhum chefe de equipa encontrado.")
        return

    print("\n=== CHEFES DE EQUIPAS Disponíveis ===")
    for chefe_equipa in dados:
        print(f"- {chefe_equipa['nome']}")

    nome = input("\nDigite o nome do chefe de equipa que deseja editar: ")

    # Procurar chefe de equipa pelo nome
    chefe_equipa_encontrado = None
    for chefe_equipa in dados:
        if chefe_equipa["nome"].lower() == nome.lower():
            chefe_equipa_encontrado = chefe_equipa
            break

    if not chefe_equipa_encontrado:
        print("chefe de equipa não encontrado!")
        return

    print("\n=== Campos editáveis ===")
    for chave in chefe_equipa_encontrado.keys():
        print(f"- {chave}")

    campo = input("\nDigite o nome do campo que deseja editar: ")

    if campo not in chefe_equipa_encontrado:
        print("Campo inválido!")
        return

    novo_valor = input(f"Novo valor para '{campo}' (atual: {chefe_equipa_encontrado[campo]}): ")

    chefe_equipa_encontrado[campo] = novo_valor

    guardar_dados(dados)

    print("\n Dados atualizados com sucesso!")

#editar_chefe_equipa()
import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "membro_equipas.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_membros():
    """
    Carrega a lista de membros de equipa do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `membro_equipas.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando os membros de equipa.
    """
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        return []

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as file:
        return json.load(file)


# Função para guardar o JSON
def guardar_membros(dados):
    """
    Guarda a lista de membros de equipa no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando os membros de equipa.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar membro da equipa
def editar_membro():
    """
    Permite editar os dados de um membro de equipa específico armazenado no ficheiro JSON.

    A função realiza os seguintes passos:
        1. Carrega a lista de membros de equipa usando `carregar_membros()`.
        2. Exibe todos os membros disponíveis.
        3. Solicita ao utilizador o nome do membro que deseja editar.
        4. Procura o membro pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo no membro correspondente.
        9. Guarda a lista atualizada usando `guardar_membros()`.
       10. Exibe mensagem de confirmação de atualização.

    Se o membro não for encontrado ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
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

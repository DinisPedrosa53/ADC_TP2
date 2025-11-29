import json
import os

# Caminho do ficheiro JSON dentro da pasta Json
PASTA = "src/jsons"
FICHEIRO = "pilotos.json"
CAMINHO_FICHEIRO = os.path.join(PASTA, FICHEIRO)


# Função para carregar o JSON
def carregar_dados():
    """
    Carrega a lista de pilotos do ficheiro JSON.

    Esta função garante que a pasta `src/jsons` exista e
    lê os dados do ficheiro `pilotos.json`. Se o ficheiro não existir,
    retorna uma lista vazia.

    Returns:
        list: Lista de dicionários representando os pilotos.
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
    Guarda a lista de pilotos no ficheiro JSON.

    Args:
        dados (list): Lista de dicionários representando os pilotos.
    """
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


# Função para editar um piloto
def editar_piloto():
    """
    Permite editar os dados de um piloto específico armazenado no ficheiro JSON.

    A função realiza os seguintes passos:
        1. Carrega a lista de pilotos usando `carregar_dados()`.
        2. Exibe todos os pilotos disponíveis.
        3. Solicita ao utilizador o nome do piloto que deseja editar.
        4. Procura o piloto pelo nome.
        5. Exibe os campos disponíveis para edição.
        6. Solicita ao utilizador o campo que deseja alterar.
        7. Solicita o novo valor para o campo selecionado.
        8. Atualiza o valor do campo no piloto correspondente.
        9. Guarda a lista atualizada usando `guardar_dados()`.
       10. Exibe mensagem de confirmação de atualização.

    Se o piloto não for encontrado ou se o campo informado for inválido,
    exibe mensagens apropriadas.
    """
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
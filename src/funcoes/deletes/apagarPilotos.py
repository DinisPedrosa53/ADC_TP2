import json
import os

def carregar_pilotos(ficheiro="pilotos.json"):
    """
    Carrega a lista de pilotos a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `pilotos.json`) 
    localizado na pasta `src/jsons` e retorna a lista de pilotos.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"pilotos.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando um piloto.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            pilotos = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(pilotos, list):
                return []

            return pilotos
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_pilotos(pilotos, ficheiro="pilotos.json"):
    """
    Guarda a lista de pilotos em um ficheiro JSON.

    Esta função escreve a lista de pilotos fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        pilotos (list): Lista de dicionários representando os pilotos.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"pilotos.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(pilotos, file, ensure_ascii=False, indent=4)


def apagar_piloto():
    """
    Apaga um piloto da lista armazenada no ficheiro JSON.

    Esta função permite remover um piloto específico da lista de pilotos
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados corretamente
    após a remoção.

    Passos executados pela função:
        1. Carrega a lista de pilotos usando `carregar_pilotos()`.
        2. Exibe todos os pilotos registados pelo nome.
        3. Solicita ao utilizador o nome do piloto que deseja apagar.
        4. Remove o piloto correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_pilotos()`.
        6. Exibe mensagens apropriadas se o piloto não for encontrado 
           ou se a operação for bem-sucedida.
    """
    pilotos = carregar_pilotos()

    if not pilotos:
        print("Não existem pilotos registados.")
        return

    # Listar os pilotos pelo nome
    print("\n--- LISTA DE PILOTOS ---")
    for idx, piloto in enumerate(pilotos, start=1):
        print(f"{idx} - {piloto['nome']}")

    nome = input("\nDigite o nome do piloto que deseja apagar: ").strip()

    # Filtrar removendo o piloto que tem esse nome
    pilotos_filtrados = [e for e in pilotos if e["nome"].lower() != nome.lower()]

    if len(pilotos_filtrados) == len(pilotos):
        print("O piloto não foi encontrado!")
        return

    # Guardar alterações
    guardar_pilotos(pilotos_filtrados)
    print(f"Piloto '{nome}' apagado com sucesso!")

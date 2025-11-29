import json
import os

def carregar_pistas(ficheiro="pistas.json"):
    """
    Carrega a lista de pistas a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `pistas.json`) 
    localizado na pasta `src/jsons` e retorna a lista de pistas.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"pistas.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando uma pista.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            pistas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(pistas, list):
                return []

            return pistas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_pistas(pistas, ficheiro="pistas.json"):
    """
    Guarda a lista de pistas em um ficheiro JSON.

    Esta função escreve a lista de pistas fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        pistas (list): Lista de dicionários representando as pistas.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"pistas.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(pistas, file, ensure_ascii=False, indent=4)


def apagar_pista():
    """
    Apaga uma pista da lista armazenada no ficheiro JSON.

    Esta função permite remover uma pista específica da lista de pistas
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados corretamente
    após a remoção.

    Passos executados pela função:
        1. Carrega a lista de pistas usando `carregar_pistas()`.
        2. Exibe todas as pistas registadas pelo nome.
        3. Solicita ao utilizador o nome da pista que deseja apagar.
        4. Remove a pista correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_pistas()`.
        6. Exibe mensagens apropriadas se a pista não for encontrada 
           ou se a operação for bem-sucedida.
    """
    pistas = carregar_pistas()

    if not pistas:
        print("Não existem pistas registadas.")
        return

    # Listar as pistas pelo nome
    print("\n--- LISTA DE PISTAS ---")
    for idx, pista in enumerate(pistas, start=1):
        print(f"{idx} - {pista['nome']}")

    nome = input("\nDigite o nome da pista que deseja apagar: ").strip()

    # Filtrar removendo a pista que tem esse nome
    pistas_filtradas = [e for e in pistas if e["nome"].lower() != nome.lower()]

    if len(pistas_filtradas) == len(pistas):
        print("A pista não foi encontrada!")
        return

    # Guardar alterações
    guardar_pistas(pistas_filtradas)
    print(f"pista '{nome}' apagada com sucesso!")

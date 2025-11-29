import json
import os

def carregar_carros(ficheiro="carros.json"):
    """
    Carrega a lista de carros a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `carros.json`) 
    localizado na pasta `src/jsons` e retorna a lista de carros.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"carros.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando um carro.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            carros = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(carros, list):
                return []

            return carros
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_carros(carros, ficheiro="carros.json"):
    """
    Guarda a lista de carros em um ficheiro JSON.

    Esta função escreve a lista de carros fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        carros (list): Lista de dicionários representando os carros.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os carros serão salvos. Padrão é `"carros.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(carros, file, ensure_ascii=False, indent=4)


def apagar_carro():
    """
    Apaga um carro da lista de carros armazenada no ficheiro JSON.

    Esta função permite remover um carro específico da lista de carros
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados
    corretamente após a remoção.

    Passos executados pela função:
        1. Carrega a lista de carros usando `carregar_carros()`.
        2. Exibe todos os carros registados pelo nome.
        3. Solicita ao utilizador o nome do carro que deseja apagar.
        4. Remove o carro correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_carros()`.
        6. Exibe mensagens apropriadas se o carro não for encontrado 
           ou se a operação for bem-sucedida.
    """
    carros = carregar_carros()

    if not carros:
        print("Não existem carros registados.")
        return

    # Listar os carros pelo nome
    print("\n--- LISTA DE CARROSs ---")
    for idx, carro in enumerate(carros, start=1):
        print(f"{idx} - {carro['nome']}")

    nome = input("\nDigite o nome do carro que deseja apagar: ").strip()

    # Filtrar removendo o carro que tem esse nome
    carros_filtrados = [e for e in carros if e["nome"].lower() != nome.lower()]

    if len(carros_filtrados) == len(carros):
        print("O carro não foi encontrado!")
        return

    # Guardar alterações
    guardar_carros(carros_filtrados)
    print(f"carro '{nome}' apagado com sucesso!")

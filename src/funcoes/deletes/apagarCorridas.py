import json
import os

def carregar_corridas(ficheiro="corridas.json"):
    """
    Carrega a lista de corridas a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `corridas.json`) 
    localizado na pasta `src/jsons` e retorna a lista de corridas.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"corridas.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando uma corrida.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            corridas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(corridas, list):
                return []

            return corridas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_corridas(corridas, ficheiro="corridas.json"):
    """
    Guarda a lista de corridas em um ficheiro JSON.

    Esta função escreve a lista de corridas fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        corridas (list): Lista de dicionários representando as corridas.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"corridas.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(corridas, file, ensure_ascii=False, indent=4)


def apagar_corrida():
    """
    Apaga uma corrida da lista armazenada no ficheiro JSON.

    Esta função permite remover uma corrida específica da lista de corridas
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados
    corretamente após a remoção.

    Passos executados pela função:
        1. Carrega a lista de corridas usando `carregar_corridas()`.
        2. Exibe todas as corridas registadas pelo nome.
        3. Solicita ao utilizador o nome da corrida que deseja apagar.
        4. Remove a corrida correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_corridas()`.
        6. Exibe mensagens apropriadas se a corrida não for encontrada 
           ou se a operação for bem-sucedida.
    """
    corridas = carregar_corridas()

    if not corridas:
        print("Não existem corridas registadas.")
        return

    # Listar as corridas pelo nome
    print("\n--- LISTA DE  CORRIDAS ---")
    for idx, corrida in enumerate(corridas, start=1):
        print(f"{idx} - {corrida['nome']}")

    nome = input("\nDigite o nome da corrida que deseja apagar: ").strip()

    # Filtrar removendo a corrida que tem esse nome
    corridas_filtradas = [e for e in corridas if e["nome"].lower() != nome.lower()]

    if len(corridas_filtradas) == len(corridas):
        print("A corrida não foi encontrada!")
        return

    # Guardar alterações
    guardar_corridas(corridas_filtradas)
    print(f"corrida '{nome}' apagada com sucesso!")

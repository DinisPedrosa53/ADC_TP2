import json
import os

def carregar_equipas(ficheiro="equipas.json"):
    """
    Carrega a lista de equipas a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `equipas.json`) 
    localizado na pasta `src/jsons` e retorna a lista de equipas.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"equipas.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando uma equipa.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            equipas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(equipas, list):
                return []

            return equipas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_equipas(equipas, ficheiro="equipas.json"):
    """
    Guarda a lista de equipas em um ficheiro JSON.

    Esta função escreve a lista de equipas fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        equipas (list): Lista de dicionários representando as equipas.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"equipas.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(equipas, file, ensure_ascii=False, indent=4)


def apagar_equipa():
    """
    Apaga uma equipa da lista armazenada no ficheiro JSON.

    Esta função permite remover uma equipa específica da lista de equipas
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados
    corretamente após a remoção.

    Passos executados pela função:
        1. Carrega a lista de equipas usando `carregar_equipas()`.
        2. Exibe todas as equipas registadas pelo nome.
        3. Solicita ao utilizador o nome da equipa que deseja apagar.
        4. Remove a equipa correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_equipas()`.
        6. Exibe mensagens apropriadas se a equipa não for encontrada 
           ou se a operação for bem-sucedida.
    """
    equipas = carregar_equipas()

    if not equipas:
        print("Não existem equipas registadas.")
        return

    # Listar as equipas pelo nome
    print("\n--- LISTA DE EQUIPAS ---")
    for idx, equipa in enumerate(equipas, start=1):
        print(f"{idx} - {equipa['nome']}")

    nome = input("\nDigite o nome da equipa que deseja apagar: ").strip()

    # Filtrar removendo a equipa que tem esse nome
    equipas_filtradas = [e for e in equipas if e["nome"].lower() != nome.lower()]

    if len(equipas_filtradas) == len(equipas):
        print("A equipa não foi encontrada!")
        return

    # Guardar alterações
    guardar_equipas(equipas_filtradas)
    print(f"Equipa '{nome}' apagada com sucesso!")

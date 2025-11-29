import json
import os

def carregar_chefes_equipas(ficheiro="chefes_equipas.json"):
    """
    Carrega a lista de chefes de equipa a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `chefes_equipas.json`) 
    localizado na pasta `src/jsons` e retorna a lista de chefes de equipa.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"chefes_equipas.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando um chefe de equipa.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            chefes_equipas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(chefes_equipas, list):
                return []

            return chefes_equipas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_chefes_equipas(chefes_equipas, ficheiro="chefes_equipas.json"):
    """
    Guarda a lista de chefes de equipa em um ficheiro JSON.

    Esta função escreve a lista de chefes de equipa fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        chefes_equipas (list): Lista de dicionários representando os chefes de equipa.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"chefes_equipas.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(chefes_equipas, file, ensure_ascii=False, indent=4)


def apagar_chefe_equipa():
    """
    Apaga um chefe de equipa da lista armazenada no ficheiro JSON.

    Esta função permite remover um chefe de equipa específico da lista 
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados 
    corretamente após a remoção.

    Passos executados pela função:
        1. Carrega a lista de chefes de equipa usando `carregar_chefes_equipas()`.
        2. Exibe todos os chefes de equipa registados pelo nome.
        3. Solicita ao utilizador o nome do chefe de equipa que deseja apagar.
        4. Remove o chefe de equipa correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_chefes_equipas()`.
        6. Exibe mensagens apropriadas se o chefe de equipa não for encontrado 
           ou se a operação for bem-sucedida.
    """
    chefes_equipas = carregar_chefes_equipas()

    if not chefes_equipas:
        print("Não existem chefes de equipa registados.")
        return

    # Listar os chefes de equipa pelo nome
    print("\n--- LISTA DE CHEFES DE EQUIPAS ---")
    for idx, chefe_equipa in enumerate(chefes_equipas, start=1):
        print(f"{idx} - {chefe_equipa['nome']}")

    nome = input("\nDigite o nome do chefe de equipa que deseja apagar: ").strip()

    # Filtrar removendo o chefe de equipa que tem esse nome
    chefes_equipas_filtrados = [e for e in chefes_equipas if e["nome"].lower() != nome.lower()]

    if len(chefes_equipas_filtrados) == len(chefes_equipas):
        print("O chefe de equipa não foi encontrado!")
        return

    # Guardar alterações
    guardar_chefes_equipas(chefes_equipas_filtrados)
    print(f"chefe de equipa '{nome}' apagado com sucesso!")

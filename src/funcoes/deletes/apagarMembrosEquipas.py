import json
import os

def carregar_membros_equipas(ficheiro="membros_equipas.json"):
    """
    Carrega a lista de membros de equipa a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `membros_equipas.json`) 
    localizado na pasta `src/jsons` e retorna a lista de membros de equipa.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"membros_equipas.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando um membro de equipa.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            membros_equipas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(membros_equipas, list):
                return []

            return membros_equipas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_membros_equipas(membros_equipas, ficheiro="membros_equipas.json"):
    """
    Guarda a lista de membros de equipa em um ficheiro JSON.

    Esta função escreve a lista de membros de equipa fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        membros_equipas (list): Lista de dicionários representando os membros de equipa.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"membros_equipas.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(membros_equipas, file, ensure_ascii=False, indent=4)


def apagar_membro_equipa():
    """
    Apaga um membro de equipa da lista armazenada no ficheiro JSON.

    Esta função permite remover um membro específico da lista de membros de equipa
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados corretamente
    após a remoção.

    Passos executados pela função:
        1. Carrega a lista de membros de equipa usando `carregar_membros_equipas()`.
        2. Exibe todos os membros de equipa registados pelo nome.
        3. Solicita ao utilizador o nome do membro de equipa que deseja apagar.
        4. Remove o membro de equipa correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_membros_equipas()`.
        6. Exibe mensagens apropriadas se o membro de equipa não for encontrado 
           ou se a operação for bem-sucedida.
    """
    membros_equipas = carregar_membros_equipas()

    if not membros_equipas:
        print("Não existem membros de equipa registados.")
        return

    # Listar os membros de equipa pelo nome
    print("\n--- LISTA DE MEMBROS DE EQUIPAS ---")
    for idx, membro_equipa in enumerate(membros_equipas, start=1):
        print(f"{idx} - {membro_equipa['nome']}")

    nome = input("\nDigite o nome do membro de equipa que deseja apagar: ").strip()

    # Filtrar removendo o membro de equipa que tem esse nome
    membros_equipas_filtrados = [e for e in membros_equipas if e["nome"].lower() != nome.lower()]

    if len(membros_equipas_filtrados) == len(membros_equipas):
        print("O membro de equipa não foi encontrado!")
        return

    # Guardar alterações
    guardar_membros_equipas(membros_equipas_filtrados)
    print(f"membro de equipa '{nome}' apagado com sucesso!")

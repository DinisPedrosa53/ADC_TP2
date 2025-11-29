import json
import os


def carregar_utilizadores(ficheiro="utilizadores.json"):
    """
    Carrega a lista de utilizadores a partir de um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `utilizadores.json`) 
    localizado na pasta `src/jsons` e retorna a lista de utilizadores.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser carregado. Padrão é `"utilizadores.json"`.

    Returns:
        list: Retorna uma lista de dicionários, cada um representando um utilizador.
              Retorna uma lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            utilizadores = json.load(file)

            if not isinstance(utilizadores, list):
                return []

            return utilizadores

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_utilizadores(utilizadores, ficheiro="utilizadores.json"):
    """
    Guarda a lista de utilizadores em um ficheiro JSON.

    Esta função escreve a lista de utilizadores fornecida no ficheiro JSON especificado,
    garantindo que a pasta `src/jsons` exista.

    Args:
        utilizadores (list): Lista de dicionários representando os utilizadores.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão salvos. Padrão é `"utilizadores.json"`.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(utilizadores, file, ensure_ascii=False, indent=4)

def apagar_utilizador():
    """
    Apaga um utilizador da lista armazenada no ficheiro JSON.

    Esta função permite remover um utilizador específico da lista de utilizadores
    guardada em ficheiro JSON, garantindo que os dados sejam atualizados corretamente
    após a remoção.

    Passos executados pela função:
        1. Carrega a lista de utilizadores usando `carregar_utilizadores()`.
        2. Exibe todos os utilizadores registados com nome e email.
        3. Solicita ao utilizador o nome do utilizador que deseja apagar.
        4. Remove o utilizador correspondente da lista.
        5. Guarda a lista atualizada usando `guardar_utilizadores()`.
        6. Exibe mensagens apropriadas se o utilizador não for encontrado 
           ou se a operação for bem-sucedida.
    """
    utilizadores = carregar_utilizadores()

    if not utilizadores:
        print("Não existem utilizadores registados.")
        return

    print("\n--- LISTA DE UTILIZADORES ---")
    for idx, user in enumerate(utilizadores, start=1):
        print(f"{idx} - {user['nome']} ({user['email']})")

    nome = input("\nDigite o nome do utilizador que deseja apagar: ").strip()

    utilizadores_filtrados = [u for u in utilizadores if u["nome"].lower() != nome.lower()]

    if len(utilizadores_filtrados) == len(utilizadores):
        print("O utilizador não foi encontrado!")
        return

    guardar_utilizadores(utilizadores_filtrados)
    print(f"Utilizador '{nome}' apagado com sucesso!")

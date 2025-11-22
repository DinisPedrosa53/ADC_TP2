import json
import os


def carregar_utilizadores(ficheiro="utilizadores.json"):
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
    caminho = os.path.join("src/jsons", ficheiro)

    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(utilizadores, file, ensure_ascii=False, indent=4)

def apagar_utilizador():
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

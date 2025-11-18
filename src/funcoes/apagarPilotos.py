import json
import os

# --------------------------
# Carrega pilotos do ficheiro
# --------------------------
def carregar_pilotos(ficheiro="pilotos.json"):
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


# --------------------------
# Grava pilotos no ficheiro
# --------------------------
def guardar_pilotos(pilotos, ficheiro="pilotos.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(pilotos, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar piloto
# --------------------------
def apagar_piloto():
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

    # Salvar alterações
    guardar_pilotos(pilotos_filtrados)
    print(f"Piloto '{nome}' apagado com sucesso!")

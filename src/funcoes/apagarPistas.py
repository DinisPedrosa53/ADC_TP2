import json
import os

# --------------------------
# Carrega pistas do ficheiro
# --------------------------
def carregar_pistas(ficheiro="pistas.json"):
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


# --------------------------
# Grava pistas no ficheiro
# --------------------------
def guardar_pistas(pistas, ficheiro="pistas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(pistas, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar pista
# --------------------------
def apagar_pista():
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

    # Salvar alterações
    guardar_pistas(pistas_filtradas)
    print(f"pista '{nome}' apagada com sucesso!")

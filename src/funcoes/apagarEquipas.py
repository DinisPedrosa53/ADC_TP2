import json
import os

# --------------------------
# Carrega equipas do ficheiro
# --------------------------
def carregar_equipas(ficheiro="equipas.json"):
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


# --------------------------
# Grava equipas no ficheiro
# --------------------------
def guardar_equipas(equipas, ficheiro="equipas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(equipas, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar equipa
# --------------------------
def apagar_equipa():
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

    # Salvar alterações
    guardar_equipas(equipas_filtradas)
    print(f"Equipa '{nome}' apagada com sucesso!")

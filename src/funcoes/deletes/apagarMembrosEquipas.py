import json
import os

# --------------------------
# Carrega membros de equipa do ficheiro
# --------------------------
def carregar_membros_equipas(ficheiro="membros_equipas.json"):
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


# --------------------------
# Grava membros de equipa no ficheiro
# --------------------------
def guardar_membros_equipas(membros_equipas, ficheiro="membros_equipas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(membros_equipas, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar membro de equipa
# --------------------------
def apagar_membro_equipa():
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

    # Salvar alterações
    guardar_membros_equipas(membros_equipas_filtrados)
    print(f"membro de equipa '{nome}' apagado com sucesso!")

import json
import os

# --------------------------
# Carrega chefes de equipa do ficheiro
# --------------------------
def carregar_chefes_equipas(ficheiro="chefes_equipas.json"):
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


# --------------------------
# Grava chefes de equipa no ficheiro
# --------------------------
def guardar_chefes_equipas(chefes_equipas, ficheiro="chefes_equipas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(chefes_equipas, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar chefe de equipa
# --------------------------
def apagar_chefe_equipa():
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

    # Salvar alterações
    guardar_chefes_equipas(chefes_equipas_filtrados)
    print(f"chefe de equipa '{nome}' apagado com sucesso!")

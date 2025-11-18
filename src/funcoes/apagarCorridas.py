import json
import os

# --------------------------
# Carrega corridas do ficheiro
# --------------------------
def carregar_corridas(ficheiro="corridas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            corridas = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(corridas, list):
                return []

            return corridas
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# --------------------------
# Grava corridas no ficheiro
# --------------------------
def guardar_corridas(corridas, ficheiro="corridas.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(corridas, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar corrida
# --------------------------
def apagar_corrida():
    corridas = carregar_corridas()

    if not corridas:
        print("Não existem corridas registadas.")
        return

    # Listar as corridas pelo nome
    print("\n--- LISTA DE corridaS ---")
    for idx, corrida in enumerate(corridas, start=1):
        print(f"{idx} - {corrida['nome']}")

    nome = input("\nDigite o nome da corrida que deseja apagar: ").strip()

    # Filtrar removendo a corrida que tem esse nome
    corridas_filtradas = [e for e in corridas if e["nome"].lower() != nome.lower()]

    if len(corridas_filtradas) == len(corridas):
        print("A corrida não foi encontrada!")
        return

    # Salvar alterações
    guardar_corridas(corridas_filtradas)
    print(f"corrida '{nome}' apagada com sucesso!")

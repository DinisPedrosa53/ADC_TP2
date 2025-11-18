import json
import os

# --------------------------
# Carrega carros do ficheiro
# --------------------------
def carregar_carros(ficheiro="carros.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho, "r", encoding="utf-8") as file:
            carros = json.load(file)

            # Garantir que sempre retorna uma lista
            if not isinstance(carros, list):
                return []

            return carros
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# --------------------------
# Grava carros no ficheiro
# --------------------------
def guardar_carros(carros, ficheiro="carros.json"):
    caminho = os.path.join("src/jsons", ficheiro)

    # Certifica que a pasta existe
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(carros, file, ensure_ascii=False, indent=4)


# --------------------------
# Apagar carro
# --------------------------
def apagar_carro():
    carros = carregar_carros()

    if not carros:
        print("Não existem carros registados.")
        return

    # Listar os carros pelo nome
    print("\n--- LISTA DE carroS ---")
    for idx, carro in enumerate(carros, start=1):
        print(f"{idx} - {carro['nome']}")

    nome = input("\nDigite o nome do carro que deseja apagar: ").strip()

    # Filtrar removendo o carro que tem esse nome
    carros_filtrados = [e for e in carros if e["nome"].lower() != nome.lower()]

    if len(carros_filtrados) == len(carros):
        print("O carro não foi encontrado!")
        return

    # Salvar alterações
    guardar_carros(carros_filtrados)
    print(f"carro '{nome}' apagado com sucesso!")

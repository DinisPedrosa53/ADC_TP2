import json
import os

# --------------------------
# Carregar carros do ficheiro
# --------------------------
def carregar_carros(ficheiro="carros.json"):
    caminho = os.path.join("src/jsons", ficheiro)
    try:
        with open(caminho, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: ficheiro 'carros.json' não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: ficheiro JSON mal formatado.")
        return []

# --------------------------
# Imprimir tabela de carros
# --------------------------
def imprimir_tabela(carros):
    print(f"{'Nome':<20} {'equipa':<10} {'Peso':<10} {'altura':<15} {'potencia':<10} {'preco':<10}{'Ativo':<10}")
    print("=" * 85)
    for p in carros:
        print(f"{p['nome']:<20}  {p['equipa']:<10} {p['peso']:<10} {p['altura']:<15} {p['potencia']:<10} {p['preco']:<10} {p['ativo']:<10}")

# --------------------------
# Função de ordenação
# --------------------------
def ordenar_carros(carros, criterio):
    if criterio == "nome":
        carros.sort(key=lambda x: x["nome"].lower())
    elif criterio == "preco":
        carros.sort(key=lambda x: int(x.get("preco", 0)), reverse=True)
    return carros

# --------------------------
# Listar carros com equipa
# --------------------------
def listar_carros_com_equipa(carros, ordenar_por):
    com_equipa = [p for p in carros if p["equipa_atual"] not in ("", None, "-", "sem equipa")]
    com_equipa = ordenar_carros(com_equipa, ordenar_por)

    if com_equipa:
        print("\n--- carroS COM EQUIPA ---")
        imprimir_tabela(com_equipa)
    else:
        print("Nenhum carro com equipa.")

# --------------------------
# Listar carros sem equipa
# --------------------------
def listar_carros_sem_equipa(carros, ordenar_por):
    sem_equipa = [p for p in carros if p["equipa_atual"] in ("", None, "-", "sem equipa")]
    sem_equipa = ordenar_carros(sem_equipa, ordenar_por)

    if sem_equipa:
        print("\n--- carroS SEM EQUIPA ---")
        imprimir_tabela(sem_equipa)
    else:
        print("Nenhum carro sem equipa.")

# --------------------------
# Função interativa para escolher ordenação
# --------------------------
def listar_carros_interativo():
    print("Como deseja ordenar os carros?")
    print("1 - Nome (alfabético)")
    print("2 - Pontos (decrescente)")
    escolha = input("Escolha: ")

    if escolha == "1":
        ordenar_por = "nome"
    elif escolha == "2":
        ordenar_por = "pontos"
    else:
        print("Opção inválida. Ordenando por nome por defeito.")
        ordenar_por = "nome"

    carros = carregar_carros()
    listar_carros_com_equipa(carros, ordenar_por)
    listar_carros_sem_equipa(carros, ordenar_por)

# --------------------------
# Função principal para chamar
# --------------------------
def listagem_carros():
    listar_carros_interativo()

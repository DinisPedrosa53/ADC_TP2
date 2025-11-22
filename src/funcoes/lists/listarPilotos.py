import json
import os

# --------------------------
# Carregar pilotos do ficheiro
# --------------------------
def carregar_pilotos(ficheiro="pilotos.json"):
    caminho = os.path.join("src/jsons", ficheiro)
    try:
        with open(caminho, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: ficheiro 'pilotos.json' não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: ficheiro JSON mal formatado.")
        return []

# --------------------------
# Imprimir tabela de pilotos
# --------------------------
def imprimir_tabela(pilotos):
    print(f"{'Nome':<20} {'Idade':<10} {'Peso':<10} {'Equipa':<15} {'Vitórias':<10} {'Pontos':<10} {'Ativo':<10}")
    print("=" * 85)
    for p in pilotos:
        print(f"{p['nome']:<20} {p['idade']:<10} {p['peso']:<10} {p['equipa_atual']:<15} {p['vitorias']:<10} {p['pontosPiloto']:<10} {p['ativo']:<10}")

# --------------------------
# Função de ordenação
# --------------------------
def ordenar_pilotos(pilotos, criterio):
    if criterio == "nome":
        pilotos.sort(key=lambda x: x["nome"].lower())
    elif criterio == "pontos":
        pilotos.sort(key=lambda x: int(x.get("pontosPiloto", 0)), reverse=True)
    return pilotos

# --------------------------
# Listar pilotos com equipa
# --------------------------
def listar_pilotos_com_equipa(pilotos, ordenar_por):
    com_equipa = [p for p in pilotos if p["equipa_atual"] not in ("", None, "-", "sem equipa")]
    com_equipa = ordenar_pilotos(com_equipa, ordenar_por)

    if com_equipa:
        print("\n--- PILOTOS COM EQUIPA ---")
        imprimir_tabela(com_equipa)
    else:
        print("Nenhum piloto com equipa.")

# --------------------------
# Listar pilotos sem equipa
# --------------------------
def listar_pilotos_sem_equipa(pilotos, ordenar_por):
    sem_equipa = [p for p in pilotos if p["equipa_atual"] in ("", None, "-", "sem equipa")]
    sem_equipa = ordenar_pilotos(sem_equipa, ordenar_por)

    if sem_equipa:
        print("\n--- PILOTOS SEM EQUIPA ---")
        imprimir_tabela(sem_equipa)
    else:
        print("Nenhum piloto sem equipa.")

# --------------------------
# Função interativa para escolher ordenação
# --------------------------
def listar_pilotos_interativo():
    print("Como deseja ordenar os pilotos?")
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

    pilotos = carregar_pilotos()
    listar_pilotos_com_equipa(pilotos, ordenar_por)
    listar_pilotos_sem_equipa(pilotos, ordenar_por)

# --------------------------
# Função principal para chamar
# --------------------------
def listagem_pilotos():
    listar_pilotos_interativo()

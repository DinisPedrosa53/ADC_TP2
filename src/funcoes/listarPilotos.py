import json
import os

# --------------------------
# Lê o ficheiro JSON
# --------------------------
def carregar_pilotos(ficheiro="pilotos.json"):
    try:
        caminho = os.path.join("src/jsons", ficheiro)
        with open(caminho, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: ficheiro 'pilotos.json' não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: ficheiro JSON mal formatado.")
        return []

# --------------------------
# Tabela formatada
# --------------------------
def imprimir_tabela(pilotos):
    print(f"{'Nome':<20} {'Idade':<10} {'Peso':<10} {'Equipa':<15} {'Vitórias':<10} {'Pontos':<10}")
    print("=" * 85)
    for p in pilotos:
        print(f"{p['nome']:<20} {p['idade']:<10} {p['peso']:<10} {p['equipa_atual']:<15} {p['vitorias']:<10} {p['pontosPiloto']:<10}")


# ------------------------------------
# Pilotos COM equipa
# ------------------------------------
def listar_pilotos_com_equipa():
    pilotos = carregar_pilotos()
    com_equipa = [p for p in pilotos if p["equipa_atual"] not in ("", None, "-", "sem equipa")]
    
    if com_equipa:
        print("\n--- PILOTOS COM EQUIPA ---")
        imprimir_tabela(com_equipa)
    else:
        print("Nenhum piloto com equipa.")

# ------------------------------------
# Pilotos SEM equipa
# ------------------------------------
def listar_pilotos_sem_equipa():
    pilotos = carregar_pilotos()
    sem_equipa = [p for p in pilotos if p["equipa_atual"] in ("", None, "-", "sem equipa")]

    if sem_equipa:
        print("\n--- PILOTOS SEM EQUIPA ---")
        imprimir_tabela(sem_equipa)
    else:
        print("Nenhum piloto sem equipa.")


# --------------------------
# Função principal
# --------------------------
def listagem_pilotos():
    listar_pilotos_com_equipa()
    listar_pilotos_sem_equipa()

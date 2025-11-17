import json
import os

# Função para listar os pilotos do ficheiro JSON
def listar_pilotos(ficheiro="pilotos.json", ordenar_por=None):
    caminho_ficheiro = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            pilotos = json.load(file)

        if not pilotos:
            print("Nenhum piloto encontrado no ficheiro.")
            return

        # Ordenar os pilotos se necessário
        if ordenar_por == "nome":
            pilotos.sort(key=lambda x: x["nome"].lower())
        elif ordenar_por == "pontos":
            # Converter pontos para inteiro antes de ordenar
            pilotos.sort(key=lambda x: int(x.get("pontosPiloto", 0)), reverse=True)

        # Cabeçalho
        print(f"{'Nome':<20} {'Idade':<6} {'Peso':<6} {'Equipa':<15} {'Vitorias':<8} {'Pontos':<8}")
        print("="*70)

        # Listar pilotos
        for piloto in pilotos:
            print(f"{piloto['nome']:<20} {piloto['idade']:<6} {piloto['peso']:<6} "
                  f"{piloto['equipa_atual']:<15} {piloto['vitorias']:<8} {piloto['pontosPiloto']:<8}")

    except FileNotFoundError:
        print("O ficheiro 'pilotos.json' não foi encontrado na pasta 'jsons'.")

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

# Função principal para chamar a listagem
def listagem_pilotos():
    print("Como deseja ordenar os pilotos?")
    print("1 - Alfabeticamente")
    print("2 - Por pontos")
    escolha = input("Escolha: ")

    if escolha == "1":
        listar_pilotos(ordenar_por="nome")
    elif escolha == "2":
        listar_pilotos(ordenar_por="pontos")
    else:
        print("Opção inválida, listando sem ordenação.")
        listar_pilotos()

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

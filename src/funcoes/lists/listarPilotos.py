import json
import os

def carregar_pilotos(ficheiro="pilotos.json"):
    """
    Carrega a lista de pilotos a partir de um ficheiro JSON.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é "pilotos.json".

    Returns:
        list: Lista de dicionários, cada um representando um piloto.
              Retorna lista vazia se o ficheiro não existir ou estiver mal formatado.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        JSONDecodeError: Caso o JSON esteja mal formatado.
    """
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

def imprimir_tabela(pilotos):
    """
    Imprime uma tabela formatada com informações de pilotos.

    Args:
        pilotos (list): Lista de dicionários representando os pilotos.

    Campos exibidos:
        - Nome
        - Idade
        - Peso
        - Equipa Atual
        - Vitórias
        - Pontos
        - Ativo
    """
    print(f"{'Nome':<20} {'Idade':<10} {'Peso':<10} {'Equipa':<15} {'Vitórias':<10} {'Pontos':<10} {'Ativo':<10}")
    print("=" * 85)
    for p in pilotos:
        print(f"{p['nome']:<20} {p['idade']:<10} {p['peso']:<10} {p['equipa_atual']:<15} {p['vitorias']:<10} {p['pontosPiloto']:<10} {p['ativo']:<10}")

def ordenar_pilotos(pilotos, criterio):
    """
    Ordena a lista de pilotos pelo critério especificado.

    Args:
        pilotos (list): Lista de dicionários de pilotos.
        criterio (str): Critério de ordenação, podendo ser:
                        - "nome": ordena alfabeticamente pelo nome.
                        - "pontos": ordena decrescentemente pelos pontos do piloto.

    Returns:
        list: Lista de pilotos ordenada.
    """
    if criterio == "nome":
        pilotos.sort(key=lambda x: x["nome"].lower())
    elif criterio == "pontos":
        pilotos.sort(key=lambda x: int(x.get("pontosPiloto", 0)), reverse=True)
    return pilotos

def listar_pilotos_com_equipa(pilotos, ordenar_por):
    """
    Filtra e imprime os pilotos que têm uma equipa atribuída.

    Args:
        pilotos (list): Lista de dicionários de pilotos.
        ordenar_por (str): Critério de ordenação ("nome" ou "pontos").
    """
    com_equipa = [p for p in pilotos if p["equipa_atual"] not in ("", None, "-", "sem equipa")]
    com_equipa = ordenar_pilotos(com_equipa, ordenar_por)

    if com_equipa:
        print("\n--- PILOTOS COM EQUIPA ---")
        imprimir_tabela(com_equipa)
    else:
        print("Nenhum piloto com equipa.")

def listar_pilotos_sem_equipa(pilotos, ordenar_por):
    """
    Filtra e imprime os pilotos que não têm equipa atribuída.

    Args:
        pilotos (list): Lista de dicionários de pilotos.
        ordenar_por (str): Critério de ordenação ("nome" ou "pontos").
    """
    sem_equipa = [p for p in pilotos if p["equipa_atual"] in ("", None, "-", "sem equipa")]
    sem_equipa = ordenar_pilotos(sem_equipa, ordenar_por)

    if sem_equipa:
        print("\n--- PILOTOS SEM EQUIPA ---")
        imprimir_tabela(sem_equipa)
    else:
        print("Nenhum piloto sem equipa.")

def listar_pilotos_interativo():
    """
    Permite ao utilizador escolher o critério de ordenação e lista os pilotos
    com e sem equipa de forma interativa.

    Critérios disponíveis:
        1 - Nome (alfabético)
        2 - Pontos (decrescente)
    """
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

def listagem_pilotos():
    """
    Função principal que inicia o processo de listagem interativa de pilotos.

    Exemplo de uso:
        listagem_pilotos()
    """
    listar_pilotos_interativo()

import json
import os

# Lê os pontos dos pilotos no ficheiro pilotos.json
def obter_pontos_piloto(nome_piloto, ficheiro="pilotos.json"):
    """
    Obtém os pontos de um piloto a partir do ficheiro JSON de pilotos.

    Esta função procura no ficheiro `pilotos.json` o piloto cujo nome corresponde
    ao fornecido. Caso seja encontrado, retorna os seus pontos. Se o piloto não
    existir ou o ficheiro não for encontrado, retorna 0.

    Args:
        nome_piloto (str): Nome do piloto a procurar.
        ficheiro (str, opcional): Nome do ficheiro JSON onde estão guardados os pilotos.
            Default: "pilotos.json".

    Returns:
        int: Pontuação do piloto. Retorna 0 se o piloto não existir ou se o ficheiro não for encontrado.

    Outras ações:
        - Mostra avisos no terminal caso o ficheiro ou o piloto não sejam encontrados.
    """
    caminho = os.path.join("src/jsons", ficheiro)

    if not os.path.exists(caminho):
        print("Ficheiro pilotos.json não encontrado!")
        return 0

    with open(caminho, "r", encoding="utf-8") as file:
        pilotos = json.load(file)

    for p in pilotos:
        if p["nome"].lower() == nome_piloto.lower():
            return int(p["pontosPiloto"])

    print(f"Aviso: piloto '{nome_piloto}' não encontrado em pilotos.json. Pontos = 0")
    return 0


def obter_dados():
    """
    Solicita ao utilizador as informações necessárias para criar uma nova equipa.

    Esta função recolhe diferentes dados relativos a uma equipa, incluindo os nomes
    dos pilotos. Com base nesses nomes, a função calcula automaticamente os pontos
    totais da equipa, recorrendo à função `obter_pontos_piloto`.

    Returns:
        dict: Dicionário contendo os dados introduzidos pelo utilizador, incluindo:
            - "nome": Nome da equipa.
            - "piloto1": Nome do piloto principal.
            - "piloto2": Nome do piloto secundário.
            - "pontosEquipa": Pontos totais da equipa (calculados automaticamente).
            - "presidente": Nome do presidente.
            - "fundador": Nome do fundador.
            - "mecanicos": Número de mecânicos.
            - "membros_total": Total de membros da equipa.
            - "patrocinadores": Lista de patrocinadores (string separada por vírgulas).
            - "vitorias": Número total de vitórias.
            - "corridas": Número total de corridas participadas.

    Outras ações:
        - Solicita inputs ao utilizador via terminal.
        - Mostra no terminal os pontos totais calculados.
    """
    dados = {}
    dados["nome"] = input("Digite o nome da equipa: ")
    
    dados["piloto1"] = input("Digite o nome do piloto principal: ")
    dados["piloto2"] = input("Digite o nome do piloto secundário: ")

    # Calcula pontos automaticamente
    pontos1 = obter_pontos_piloto(dados["piloto1"])
    pontos2 = obter_pontos_piloto(dados["piloto2"])
    dados["pontosEquipa"] = pontos1 + pontos2

    dados["presidente"] = input("Digite o nome do presidente da equipa: ")
    dados["fundador"] = input("Digite o nome do fundador da equipa: ")
    dados["mecanicos"] = input("Digite o número de mecanicos da equipa: ")
    dados["membros_total"] = input("Digite o número total de membros da equipa: ")
    dados["patrocinadores"] = input("Digite os principais patrocinadores (separados por vírgula): ")
    dados["vitorias"] = input("Digite o número total de vitórias: ")
    dados["corridas"] = input("Digite o número total de corridas participadas: ")

    print(f"\nPontos calculados automaticamente: {dados['pontosEquipa']}\n")

    return dados


def adicionar_equipa_ao_ficheiro(nova_equipa, ficheiro="equipas.json"):
    """
    Adiciona uma nova equipa ao ficheiro JSON que armazena todas as equipas.

    A função garante que a pasta `src/jsons` existe e que o ficheiro é corretamente
    carregado. Se o ficheiro já existir, adiciona a nova equipa à lista; caso contrário,
    cria um novo ficheiro contendo a equipa fornecida.

    Args:
        nova_equipa (dict): Dicionário com os dados da nova equipa.
        ficheiro (str, opcional): Nome do ficheiro JSON onde as equipas são guardadas.
            Default: "equipas.json".

    Outras ações:
        - Cria diretórios se necessário.
        - Lê e escreve dados em JSON.
        - Mostra no terminal uma mensagem de confirmação.
    """
    pasta = "src/jsons"
    caminho_ficheiro = os.path.join(pasta, ficheiro)

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    if os.path.exists(caminho_ficheiro):
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        dados = []

    dados.append(nova_equipa)

    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Nova equipa adicionada com sucesso!")


def criar_equipa():
    """
    Executa o processo completo de criação e registo de uma equipa.

    Esta função:
    - Obtém os dados necessários através de `obter_dados()`
    - Insere a equipa no ficheiro JSON com `adicionar_equipa_ao_ficheiro()`

    Outras ações:
        - Solicita dados ao utilizador.
        - Atualiza o ficheiro JSON.
    """
    nova_equipa = obter_dados()
    adicionar_equipa_ao_ficheiro(nova_equipa)

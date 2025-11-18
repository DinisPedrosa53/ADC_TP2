import json
import os

# Lê os pontos dos pilotos no ficheiro pilotos.json
def obter_pontos_piloto(nome_piloto, ficheiro="pilotos.json"):
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
    nova_equipa = obter_dados()
    adicionar_equipa_ao_ficheiro(nova_equipa)

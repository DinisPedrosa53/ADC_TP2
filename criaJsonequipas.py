import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome da equipa: ")
    dados["piloto1"] = input("Digite o nome do piloto principal: ")
    dados["piloto2"] = input("Digite o nome do piloto secundário: ")
    dados["presidente"] = input("Digite o nome do presidente da equipa: ")
    dados["fundador"] = input("Digite o nome do fundador da equipa: ")
    dados["mecanicos"] = input("Digite o número de mecanicos da equipa: ")
    dados["membros_total"] = input("Digite o número total de membros da equipa: ")
    dados["patrocinadores"] = input("Digite os principais patrocinadores (separados por vírgula): ")
    dados["vitorias"] = input("Digite o número total de vitórias: ")
    dados["corridas"] = input("Digite o número total de corridas participadas: ")
    dados["pontos"] = input("Digite o número de pontos: ")
    dados["pontosPiloto1"] = input("Digite o número de pontos do piloto principal: ")
    dados["pontosPiloto2"] = input("Digite o número de pontos do piloto secundário: ")
    
    return dados

# Função para adicionar uma nova equipa ao ficheiro JSON
def adicionar_equipa_ao_ficheiro(nova_equipa, ficheiro="equipas.json"):
    # Verifica se o ficheiro já existe
    if os.path.exists(ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
        with open(ficheiro, "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        # Se o ficheiro não existe, cria uma lista vazia
        dados = []

    # Adiciona a nova equipa à lista de equipas
    dados.append(nova_equipa)

    # Salva os dados (incluindo a nova equipa) no ficheiro JSON
    with open(ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Nova equipa adicionada com sucesso!")


# Função principal para adicionar uma equipe
def main():
    nova_equipe = obter_dados()
    adicionar_equipa_ao_ficheiro(nova_equipe)

# Chamada principal
main()
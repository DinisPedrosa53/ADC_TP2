import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome da corrida: ")
    dados["data"] = input("Digite o ano: ")
    dados["equipas"] = input("Digite as equipas que irão participar na corrida (separadas por vírgula): ")
    dados["cidade"] = input("Digite a cidade que ocorrerá a corrida: ")
    dados["pais"] = input("Digite o país que ocorrerá a corrida: ")
    dados["horario"] = input("Digite o hórario que a corrida começará: ")
    dados["tempo"] = input("Digite o tempo que esteve/estará durante a corrida(previsão): ")
    
    return dados

# Função para adicionar uma nova corrida ao ficheiro JSON
def adicionar_corrida_ao_ficheiro(nova_corrida, ficheiro="corridas.json"):

    # Caminho completo dentro da pasta Json
    pasta = "src/jsons"
    caminho_ficheiro = os.path.join(pasta, ficheiro)

    # Criar pasta Json se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Verifica se o ficheiro já existe
    if os.path.exists(caminho_ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        # Se o ficheiro não existe, cria uma lista vazia
        dados = []

    # Adiciona uma corrida à lista de corridas
    dados.append(nova_corrida)

    # Salva os dados (incluindo a nova corrida) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("nova corrida adicionada com sucesso!")


# Função principal para adicionar uma corrida
def main():
    nova_corrida = obter_dados()
    adicionar_corrida_ao_ficheiro(nova_corrida)

# Chamada principal
main()
import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome da pista: ")
    dados["distancia"] = input("Digite a distância duma volta: ")
    dados["ncurvas"] = input("Digite ao número de curvas: ")
    dados["recordevolta"] = input("Digite o recorde de volta: ")
   
    return dados

# Função para adicionar uma nova pista ao ficheiro JSON
def adicionar_pista_ao_ficheiro(nova_pista, ficheiro="pistas.json"):

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

    # Adiciona uma pista à lista de pistas
    dados.append(nova_pista)

    # Salva os dados (incluindo a nova pista) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("nova pista adicionada com sucesso!")


# Função principal para adicionar uma pista
def criar_pista():
    nova_pista = obter_dados()
    adicionar_pista_ao_ficheiro(nova_pista)


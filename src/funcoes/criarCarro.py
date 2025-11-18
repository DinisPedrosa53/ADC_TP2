import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome do carro: ")
    dados["peso"] = input("Digite o peso do carro: ")
    dados["altura"] = input("Digite a altura do carro(em cm): ")
    dados["potencia"] = input("Digite a potencia do carro(em cavalos): ")
    dados["preco"] = input("Digite o preço do carro: ")
    dados["ativo"] = input("Digite se o carro está ativo para competir( 1 = sim, 0 = não): ")
    
    
    return dados

# Função para adicionar um novo carro ao ficheiro JSON
def adicionar_carro_ao_ficheiro(novo_carro, ficheiro="carros.json"):

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

    # Adiciona um carro à lista de carros
    dados.append(novo_carro)

    # Salva os dados (incluindo o novo carro) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo carro adicionado com sucesso!")


# Função principal para adicionar um carro
def criar_carro():
    novo_carro = obter_dados()
    adicionar_carro_ao_ficheiro(novo_carro)
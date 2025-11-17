import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome completo do chefe de equipa: ")
    dados["idade"] = input("Digite a idade do chefe de equipa: ")
    dados["equipas"] = input("Digite as equipas que o chefe de equipa ja participou (separados por vírgula): ")
    dados["telefone"] = input("Digite o número de telefone do chefe de equipa: ")
    dados["morada"] = input("Digite a morada do chefe de equipa: ")
    dados["equipa_atual"] = input("Digite a equipa que o chefe de equipa se encontra atualmente: ")
    
    return dados

# Função para adicionar um novo chefe de equipa ao ficheiro JSON
def adicionar_chefe_equipa_ao_ficheiro(novo_chefe_equipa, ficheiro="chefes_equipas.json"):

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

    # Adiciona um chefe de equipa à lista de chefes de equipas
    dados.append(novo_chefe_equipa)

    # Salva os dados (incluindo o novo chefe de equipa) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo chefe de equipa adicionado com sucesso!")


# Função principal para adicionar um chefe de equipa
def main():
    novo_chefe_equipa = obter_dados()
    adicionar_chefe_equipa_ao_ficheiro(novo_chefe_equipa)

# Chamada principal
main()
import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome completo do membro de equipa: ")
    dados["idade"] = input("Digite a idade do membro de equipa: ")
    dados["equipas"] = input("Digite as equipas que o membro de equipa ja participou (separados por vírgula): ")
    dados["telefone"] = input("Digite o número de telefone do membro de equipa: ")
    dados["morada"] = input("Digite a morada do membro de equipa: ")
    dados["equipa_atual"] = input("Digite a equipa que o membro de equipa se encontra atualmente: ")
    dados["tipo"] = input("Digite o tipo de membro de equipa: ")
    dados["salario"] = input("Digite o salário anual do membro de equipa (em euros): ")
    
    return dados

# Função para adicionar um novo membro de equipa ao ficheiro JSON
def adicionar_membro_equipa_ao_ficheiro(novo_membro_equipa, ficheiro="membro_equipas.json"):

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

    # Adiciona um membro de equipa à lista de membros de equipas
    dados.append(novo_membro_equipa)

    # Salva os dados (incluindo o novo membro de equipa) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo membro de equipa adicionado com sucesso!")


# Função principal para adicionar um membro de equipa
def criar_membro_equipa():
    novo_membro_equipa = obter_dados()
    adicionar_membro_equipa_ao_ficheiro(novo_membro_equipa)
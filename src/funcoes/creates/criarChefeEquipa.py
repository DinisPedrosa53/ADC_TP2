import json
import os

def obter_dados():
    """
    Solicita ao utilizador informações para criar um novo chefe de equipa.

    Esta função interage com o utilizador através do terminal, pedindo os dados
    necessários para registar um novo chefe de equipa. Cada campo é solicitado
    individualmente e armazenado num dicionário.

    Returns:
        dict: Dicionário contendo os dados inseridos pelo utilizador, com as chaves:
            - "nome": Nome completo do chefe de equipa.
            - "idade": Idade do chefe de equipa.
            - "equipas": Lista de equipas em que o chefe já participou
              (fornecida como string separada por vírgulas).
            - "telefone": Número de telefone.
            - "morada": Morada completa.
            - "equipa_atual": Equipa onde trabalha atualmente.
    """
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
    """
    Adiciona um novo chefe de equipa a um ficheiro JSON.

    Esta função garante que o ficheiro e a pasta onde ele deve estar existem.
    Se o ficheiro já existir, os seus dados são carregados e o novo chefe
    é acrescentado. Caso contrário, um novo ficheiro será criado.

    Args:
        novo_chefe_equipa (dict): Dicionário contendo os dados do chefe de equipa
            (normalmente fornecido pela função `obter_dados`).
        ficheiro (str, opcional): Nome do ficheiro JSON onde os dados serão guardados.
            Default: "chefes_equipas.json".

    Outras ações:
        - Cria a pasta "src/jsons" caso não exista.
        - Lê e escreve no ficheiro JSON correspondente.
        - Exibe no terminal uma mensagem de sucesso.
    """
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

    # Guarda os dados (incluindo o novo chefe de equipa) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo chefe de equipa adicionado com sucesso!")


# Função principal para adicionar um chefe de equipa
def criar_chefe():
    """
    Fluxo principal para criação de um novo chefe de equipa.

    Esta função reúne todo o processo: obtém os dados do utilizador através
    de `obter_dados()` e guarda-os no ficheiro JSON através de
    `adicionar_chefe_equipa_ao_ficheiro()`.

    Outras ações:
        - Lê dados do utilizador pelo terminal.
        - Escreve num ficheiro JSON.
        - Exibe mensagem de confirmação.
    """
    novo_chefe_equipa = obter_dados()
    adicionar_chefe_equipa_ao_ficheiro(novo_chefe_equipa)


import json
import os

def obter_dados():
    """
    Solicita ao utilizador as informações necessárias para criar um novo membro de equipa.

    Esta função recolhe dados através de inputs no terminal, permitindo que o utilizador
    introduza todas as informações relevantes para o registo de um membro de equipa.
    Todos os valores introduzidos são guardados num dicionário.

    Returns:
        dict: Dicionário contendo os dados do membro de equipa, incluindo:
            - "nome": Nome completo.
            - "idade": Idade do membro.
            - "equipas": Lista (em formato string) das equipas onde já participou.
            - "telefone": Número de contacto.
            - "morada": Morada completa.
            - "equipa_atual": Equipa onde trabalha atualmente.
            - "tipo": Função / papel dentro da equipa (ex.: mecânico, engenheiro, etc.).
            - "salario": Salário anual em euros.
    """
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
    """
    Adiciona um novo membro de equipa ao ficheiro JSON que armazena todos os membros registados.

    Esta função garante que a pasta `src/jsons` existe. Em seguida, verifica se o ficheiro
    com os membros já existe: caso exista, carrega os dados e adiciona o novo membro; caso não,
    cria uma nova lista contendo o elemento. Por fim, guarda o ficheiro atualizado.

    Args:
        novo_membro_equipa (dict): Dicionário que contém os dados do membro de equipa.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os membros são armazenados.
            Default: "membro_equipas.json".

    Outras ações:
        - Cria diretórios caso não existam.
        - Lê e escreve no ficheiro JSON especificado.
        - Mostra no terminal uma mensagem de confirmação.
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

    # Adiciona um membro de equipa à lista de membros de equipas
    dados.append(novo_membro_equipa)

    # Guarda os dados (incluindo o novo membro de equipa) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo membro de equipa adicionado com sucesso!")


# Função principal para adicionar um membro de equipa
def criar_membro_equipa():
    """
    Executa todo o processo de criação e registo de um novo membro de equipa.

    Esta função:
    - Obtém os dados através de `obter_dados()`
    - Regista o membro no ficheiro JSON através de `adicionar_membro_equipa_ao_ficheiro()`

    Outras ações:
        - Solicita inputs ao utilizador.
        - Atualiza o ficheiro JSON com um novo registo.
    """
    novo_membro_equipa = obter_dados()
    adicionar_membro_equipa_ao_ficheiro(novo_membro_equipa)
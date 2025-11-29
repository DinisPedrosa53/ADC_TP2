import json
import os

def obter_dados():
    """
    Solicita ao utilizador todas as informações necessárias para criar um novo piloto.

    Esta função recolhe dados através de inputs no terminal, permitindo ao utilizador
    introduzir informações pessoais, desportivas e contratuais de um piloto. Todos os
    valores recolhidos são armazenados num dicionário.

    Returns:
        dict: Dicionário contendo os dados do piloto, incluindo:
            - "nome": Nome completo.
            - "idade": Idade.
            - "altura": Altura em centímetros.
            - "peso": Peso em quilogramas.
            - "equipas": Equipas anteriores (string separada por vírgulas).
            - "telefone": Contacto telefónico.
            - "morada": Residência.
            - "equipa_atual": Equipa atual do piloto.
            - "pontosPiloto": Número de pontos do piloto.
            - "vitorias": Número total de vitórias.
            - "data_contrato": Data de contratação.
            - "ativo": Estado de atividade (1 = ativo, 0 = inativo).
            - "salario": Salário anual em euros.
    """
    dados = {}
    dados["nome"] = input("Digite o nome completo do piloto: ")
    dados["idade"] = input("Digite a idade do piloto: ")
    dados["altura"] = input("Digite a altura do piloto(em cm): ")
    dados["peso"] = input("Digite o peso do piloto(em kg): ")
    dados["equipas"] = input("Digite as equipas que o piloto ja participou (separados por vírgula): ")
    dados["telefone"] = input("Digite o número de telefone do piloto: ")
    dados["morada"] = input("Digite a morada do piloto: ")
    dados["equipa_atual"] = input("Digite a equipa que o piloto se encontra atualmente: ")
    dados["pontosPiloto"] = input("Digite o número de pontos do piloto principal: ")
    dados["vitorias"] = input("Digite o número de vitórias do piloto: ")
    dados["data_contrato"] = input("Digite a data que o piloto foi contratado: ")
    dados["ativo"] = input("Digite se o piloto está ativo para competir (1 = sim, 0 = não): ")
    dados["salario"] = input("Digite o salário anual do piloto (em euros): ")
    
    return dados

# Função para adicionar um novo piloto ao ficheiro JSON
def adicionar_piloto_ao_ficheiro(novo_piloto, ficheiro="pilotos.json"):
    """
    Adiciona um novo piloto ao ficheiro JSON que armazena todos os pilotos registados.

    Esta função garante a existência da pasta `src/jsons`, verifica se o ficheiro já existe
    e, caso exista, carrega os dados atuais. O novo piloto é então adicionado à lista, que
    é posteriormente guardada no ficheiro JSON atualizado.

    Args:
        novo_piloto (dict): Dados do piloto a serem adicionados.
        ficheiro (str, optional): Nome do ficheiro JSON a ser utilizado.
            Default: "pilotos.json".

    Outras ações:
        - Cria diretórios caso necessário.
        - Lê e escreve no ficheiro JSON de destino.
        - Apresenta uma mensagem de confirmação no terminal.
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

    # Adiciona um piloto à lista de pilotos
    dados.append(novo_piloto)

    # Guarda os dados (incluindo o novo piloto) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo piloto adicionado com sucesso!")


# Função principal para adicionar um piloto
def criar_piloto():
    """
    Executa o processo completo de criação e registo de um piloto.

    Esta função recolhe os dados introduzidos pelo utilizador através de `obter_dados()`
    e de seguida guarda o novo piloto no ficheiro JSON utilizando
    `adicionar_piloto_ao_ficheiro()`.

    Outras ações:
        - Solicita inputs no terminal.
        - Atualiza o ficheiro JSON com um novo registo.
    """
    novo_piloto = obter_dados()
    adicionar_piloto_ao_ficheiro(novo_piloto)
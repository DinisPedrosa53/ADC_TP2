import json
import os

def obter_dados():
    """
    Solicita ao utilizador as informações necessárias para criar um novo carro.

    Esta função recolhe vários dados através de inputs no terminal, permitindo
    que o utilizador introduza todas as características relevantes de um carro.
    Todos os valores são armazenados num dicionário.

    Returns:
        dict: Dicionário contendo os dados introduzidos pelo utilizador, com as chaves:
            - "nome": Nome do carro.
            - "equipa": Equipa a que o carro pertence.
            - "peso": Peso do carro em quilogramas.
            - "altura": Altura do carro em centímetros.
            - "potencia": Potência do carro em cavalos.
            - "preco": Preço do carro.
            - "ativo": Indica se o carro está ativo para competir (1 = sim, 0 = não).
    """ 
    dados = {}
    dados["nome"] = input("Digite o nome do carro: ")
    dados["equipa"] = input("Digite a equipa do carro: ")
    dados["peso"] = input("Digite o peso do carro (em Kg): ")
    dados["altura"] = input("Digite a altura do carro(em cm): ")
    dados["potencia"] = input("Digite a potencia do carro(em cavalos): ")
    dados["preco"] = input("Digite o preço do carro: ")
    dados["ativo"] = input("Digite se o carro está ativo para competir( 1 = sim, 0 = não): ")
    
    
    return dados

def adicionar_carro_ao_ficheiro(novo_carro, ficheiro="carros.json"):
    """
    Adiciona um novo carro ao ficheiro JSON que armazena a lista de carros.

    Esta função garante que o ficheiro existe dentro da pasta `src/jsons`.
    Caso exista, carrega os dados atuais e acrescenta o novo carro. Caso não exista,
    cria uma lista nova e adiciona o carro, guardando tudo num novo ficheiro JSON.

    Args:
        novo_carro (dict): Dicionário contendo os dados do novo carro.
        ficheiro (str, opcional): Nome do ficheiro JSON onde os carros são guardados.
            Por padrão, é usado "carros.json".

    Outras ações:
        - Cria a pasta "src/jsons" se não existir.
        - Lê e escreve no ficheiro JSON indicado.
        - Mostra no terminal uma mensagem de sucesso.
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

    # Adiciona um carro à lista de carros
    dados.append(novo_carro)

    # Guarda os dados (incluindo o novo carro) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo carro adicionado com sucesso!")


# Função principal para adicionar um carro
def criar_carro():
    """
    Executa o processo completo de criação e armazenamento de um carro.

    Esta função coordena todo o fluxo:
    - Obtém os dados através de `obter_dados()`
    - Guarda-os no ficheiro JSON usando `adicionar_carro_ao_ficheiro()`

    Outras ações:
        - Solicita dados ao utilizador.
        - Atualiza o ficheiro JSON com um novo registo.
    """
    novo_carro = obter_dados()
    adicionar_carro_ao_ficheiro(novo_carro)
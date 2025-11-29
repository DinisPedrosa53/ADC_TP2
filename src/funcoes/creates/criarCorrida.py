import json
import os

def obter_dados():
    """
    Solicita ao utilizador as informações necessárias para criar uma nova corrida.

    Esta função recolhe vários dados através de inputs no terminal, pedindo ao
    utilizador que introduza todas as informações relevantes sobre a corrida.
    Os valores introduzidos são armazenados num dicionário e devolvidos.

    Returns:
        dict: Dicionário contendo os dados introduzidos pelo utilizador, com as chaves:
            - "nome": Nome da corrida.
            - "data": Ano da corrida.
            - "equipas": Lista (em formato string) das equipas participantes, separadas por vírgulas.
            - "cidade": Cidade onde ocorrerá a corrida.
            - "pais": País onde ocorrerá a corrida.
            - "horario": Horário previsto para o início da corrida.
            - "tempo": Previsão ou estado do tempo durante a corrida.
            - "bilhete": Preço do bilhete.
            - "podio": Pilotos que ficaram (ou ficarão) em 1º, 2º e 3º lugar, separados por vírgulas.
    """
    dados = {}
    dados["nome"] = input("Digite o nome da corrida: ")
    dados["data"] = input("Digite o ano: ")
    dados["equipas"] = input("Digite as equipas que irão participar na corrida (separadas por vírgula): ")
    dados["cidade"] = input("Digite a cidade que ocorrerá a corrida: ")
    dados["pais"] = input("Digite o país que ocorrerá a corrida: ")
    dados["horario"] = input("Digite o hórario que a corrida começará: ")
    dados["tempo"] = input("Digite o tempo que esteve/estará durante a corrida(previsão): ")
    dados["bilhete"] = input("Digite o preço do bilhete: ")
    dados["podio"] = input("Digite os pilotos que ficaram em 1º, 2º e 3º (por ordem e separados por vírgulas): ")

    
    return dados

# Função para adicionar uma nova corrida ao ficheiro JSON
def adicionar_corrida_ao_ficheiro(nova_corrida, ficheiro="corridas.json"):
    """
    Adiciona uma nova corrida ao ficheiro JSON que armazena a lista de corridas.

    Esta função verifica se a pasta e o ficheiro JSON existem. Caso o ficheiro exista,
    carrega os dados e adiciona a nova corrida à lista. Caso contrário, cria um novo
    ficheiro com a corrida inserida.

    Args:
        nova_corrida (dict): Dicionário contendo os dados da nova corrida.
        ficheiro (str, opcional): Nome do ficheiro JSON onde as corridas são guardadas.
            Por omissão, utiliza "corridas.json".

    Outras ações:
        - Cria a pasta "src/jsons" se esta não existir.
        - Lê e escreve no ficheiro JSON indicado.
        - Exibe no terminal uma mensagem de confirmação.
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

    # Adiciona uma corrida à lista de corridas
    dados.append(nova_corrida)

    # Guarda os dados (incluindo a nova corrida) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("nova corrida adicionada com sucesso!")


# Função principal para adicionar uma corrida
def criar_corrida():
    """
    Executa o processo completo de criação e registro de uma nova corrida.

    Esta função:
    - Obtém os dados necessários através de `obter_dados()`
    - Adiciona a corrida ao ficheiro JSON usando `adicionar_corrida_ao_ficheiro()`

    Outras ações:
        - Solicita dados ao utilizador.
        - Atualiza o ficheiro JSON.
    """
    nova_corrida = obter_dados()
    adicionar_corrida_ao_ficheiro(nova_corrida)


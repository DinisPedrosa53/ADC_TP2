import json
import os

def obter_dados():
    """
    Recolhe informações fornecidas pelo utilizador para criar uma nova pista.

    Esta função solicita vários inputs no terminal relacionados com as
    características principais de uma pista, como nome, distância da volta,
    número de curvas e recorde da volta. Os dados recolhidos são armazenados
    num dicionário.

    Returns:
        dict: Dicionário com os dados introduzidos, contendo:
            - "nome": Nome da pista.
            - "distancia": Distância de uma volta.
            - "ncurvas": Número de curvas.
            - "recordevolta": Recorde oficial de volta da pista.
    """
    dados = {}
    dados["nome"] = input("Digite o nome da pista: ")
    dados["distancia"] = input("Digite a distância duma volta: ")
    dados["ncurvas"] = input("Digite ao número de curvas: ")
    dados["recordevolta"] = input("Digite o recorde de volta: ")
   
    return dados

# Função para adicionar uma nova pista ao ficheiro JSON
def adicionar_pista_ao_ficheiro(nova_pista, ficheiro="pistas.json"):
    """
    Adiciona uma nova pista ao ficheiro JSON que contém a lista de pistas registadas.

    Esta função garante que o diretório `src/jsons` existe, carrega os dados
    atuais caso o ficheiro exista e adiciona a nova pista à lista. No final,
    guarda os dados atualizados de volta no ficheiro JSON.

    Args:
        nova_pista (dict): Dicionário contendo os dados da nova pista.
        ficheiro (str, optional): Nome do ficheiro que deverá ser utilizado.
            Default: "pistas.json".

    Outras ações:
        - Cria diretórios se não existirem.
        - Lê e escreve no ficheiro JSON.
        - Exibe uma mensagem de sucesso no terminal.
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

    # Adiciona uma pista à lista de pistas
    dados.append(nova_pista)

    # Guarda os dados (incluindo a nova pista) no ficheiro JSON
    with open(caminho_ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("nova pista adicionada com sucesso!")


# Função principal para adicionar uma pista
def criar_pista():
    """
    Executa o processo completo de criação e registo de uma pista.

    Esta função recolhe os dados da pista através de `obter_dados()`,
    e posteriormente guarda essa pista no ficheiro JSON utilizando
    `adicionar_pista_ao_ficheiro()`.

    Outras ações:
        - Solicita inputs ao utilizador no terminal.
        - Atualiza o ficheiro JSON com um novo registo de pista.
    """
    nova_pista = obter_dados()
    adicionar_pista_ao_ficheiro(nova_pista)


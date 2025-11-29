import json
import os

# Função para listar as corridas do ficheiro JSON
def listar_corridas(ficheiro="corridas.json"):
    """
    Lista todas as corridas armazenadas em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `"corridas.json"`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada contendo informações 
    sobre cada corrida, incluindo nome, pódio, país, cidade, tempo, data, bilhete e horário.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"corridas.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.

    Saída:
        Imprime uma tabela com as corridas ou mensagens de erro apropriadas caso não haja
        corridas no ficheiro ou se ocorrer algum problema de leitura.

    Exemplo de uso:
        listar_corridas()
    """
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            corridas = json.load(file)

        # Verificando se há corridas no ficheiro
        if corridas:
            print(f"{'Nome':<20} {'pódio':<15} {'país 1':<15} {'cidade':<15} {'tempo':<15} {'data':<15} {'bilhete':<15} {'hórario':<15}")
            print("="*95)

            # Listando as corridas
            for corrida in corridas:
                print(f"{corrida['nome']:<20} {corrida['podio']:<15} {corrida['pais']:<15} {corrida['cidade']:<15} {corrida['tempo']:<15} {corrida['data']:<15} {corrida['bilhete']:<15} {corrida['horario']:<15}")
        else:
            print("Nenhuma corrida encontrada no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'corridas.json' não foi encontrado na pasta 'jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_corridas():
    """
    Função auxiliar para iniciar a listagem de corridas.

    Esta função chama `listar_corridas()` sem argumentos, utilizando o ficheiro padrão
    `"corridas.json"`.

    Exemplo de uso:
        listagem_corridas()
    """
    listar_corridas()
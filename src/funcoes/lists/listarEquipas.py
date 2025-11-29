import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_equipas(ficheiro="equipas.json"):
    """
    Lista todas as equipas armazenadas em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `"equipas.json"`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada contendo informações 
    sobre cada equipa, incluindo nome, pilotos, presidente, fundador e pontos da equipa.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"equipas.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.

    Saída:
        Imprime uma tabela com as equipas ou mensagens de erro apropriadas caso não haja
        equipas no ficheiro ou se ocorrer algum problema de leitura.

    Exemplo de uso:
        listar_equipas()
    """
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Piloto 1':<15} {'Piloto 2':<15} {'Presidente':<15} {'Fundador':<15} {'Pontos':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['piloto1']:<15} {equipa['piloto2']:<15} {equipa['presidente']:<15} {equipa['fundador']:<15} {equipa['pontosEquipa']:<15}")
        else:
            print("Nenhuma equipa encontrada no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'equipas.json' não foi encontrado na pasta 'jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_equipas():
    """
    Função auxiliar para iniciar a listagem de equipas.

    Esta função chama `listar_equipas()` sem argumentos, utilizando o ficheiro padrão
    `"equipas.json"`.

    Exemplo de uso:
        listagem_equipas()
    """
    listar_equipas()
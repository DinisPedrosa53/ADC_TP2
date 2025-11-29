import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_membro_equipas(ficheiro="membro_equipas.json"):
    """
    Lista todos os membros de equipas armazenados em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `"membro_equipas.json"`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada contendo informações sobre 
    cada membro de equipa, incluindo nome, idade, salário, equipa atual, histórico de equipas e tipo.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"membro_equipas.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.

    Saída:
        Imprime uma tabela com os membros de equipa ou mensagens de erro apropriadas caso não haja
        membros no ficheiro ou se ocorrer algum problema de leitura.

    Exemplo de uso:
        listar_membro_equipas()
    """
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Idade':<15}  {'salario':<15} {'equipa Atual':<15} {'equipas':<15} {'tipo':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['idade']:<15} {equipa['salario']:<15}  {equipa['equipa_atual']:<15}  {equipa['equipas']:<15} {equipa['tipo']:<15} ")
        else:
            print("Nenhum membro_equipa encontrado no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'membro_equipas.json' não foi encontrado na pasta 'Json'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_membro_equipas():
    """
    Função auxiliar para iniciar a listagem de membros de equipas.

    Esta função chama `listar_membro_equipas()` sem argumentos, utilizando o ficheiro padrão
    `"membro_equipas.json"`.

    Exemplo de uso:
        listagem_membro_equipas()
    """
    listar_membro_equipas()
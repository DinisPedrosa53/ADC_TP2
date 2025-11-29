import json
import os

def listar_carros(ficheiro="carros.json"):
    """
    Lista todos os carros armazenados em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `carros.json`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada com as informações 
    de cada carro, incluindo nome, equipa, peso, altura, potência, preço e estado ativo.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"carros.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.
        Exception: Captura quaisquer outros erros inesperados durante a execução.

    Saída:
        Imprime uma tabela com os carros ou mensagens de erro apropriadas se houver problemas
        com o ficheiro ou se a lista de carros estiver vazia.

    Exemplo de uso:
        listar_carros()
    """
    try:
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            carros = json.load(file)

        if not carros:
            print("Nenhum carro encontrado no ficheiro.")
            return

        print(f"{'Nome':<20} {'Equipa':<10} {'Peso':<10} {'Altura':<10} {'Potência':<10} {'Preço':<10} {'Ativo':<10}")
        print("=" * 90)

        for p in carros:
            print(f"{p['nome']:<20} {p['equipa']:<10} {p['peso']:<10} {p['altura']:<10} {p['potencia']:<10} {p['preco']:<10} {str(p['ativo']):<10}")

    except FileNotFoundError:
        print("O ficheiro não foi encontrado na pasta 'src/jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o JSON — formato inválido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def listagem_carros():
    """
    Função auxiliar para iniciar a listagem de carros.

    Esta função simplesmente chama `listar_carros()` sem argumentos, utilizando o ficheiro
    padrão `carros.json`.

    Exemplo de uso:
        listagem_carros()
    """
    listar_carros()

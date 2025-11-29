import json
import os

def listar_chefes(ficheiro="chefes_equipas.json"):
    """
    Lista todos os chefes de equipa armazenados em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `chefes_equipas.json`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada com as informações 
    de cada chefe, incluindo nome, idade, equipas associadas, telefone, morada e equipa atual.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"chefes_equipas.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.
        Exception: Captura quaisquer outros erros inesperados durante a execução.

    Saída:
        Imprime uma tabela com os chefes de equipa ou mensagens de erro apropriadas 
        se houver problemas com o ficheiro ou se a lista estiver vazia.

    Exemplo de uso:
        listar_chefes()
    """
    try:
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            chefes = json.load(file)

        if not chefes:
            print("Nenhum chefe encontrado no ficheiro.")
            return

        # Cabeçalho
        print(f"{'Nome':<15} {'Idade':<10} {'Equipas':<15} {'Telefone':<15} {'Morada':<20} {'Equipa Atual':<15}")
        print("=" * 100)

        # Linhas da tabela
        for c in chefes:
            print(f"{c['nome']:<15} {c['idade']:<10} {c['equipas']:<15} {c['telefone']:<15} "
                  f"{c['morada']:<20} {c['equipa_atual']:<15}")

    except FileNotFoundError:
        print("O ficheiro não foi encontrado na pasta 'src/jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o JSON — formato inválido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def listagem_chefes():
    """
    Função auxiliar para iniciar a listagem de chefes de equipa.

    Esta função simplesmente chama `listar_chefes()` sem argumentos, utilizando o ficheiro
    padrão `chefes_equipas.json`.

    Exemplo de uso:
        listagem_chefes()
    """
    listar_chefes()

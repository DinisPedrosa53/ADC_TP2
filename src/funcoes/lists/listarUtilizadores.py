import json
import os

def listar_utilizadores(ficheiro="utilizadores.json"):
    """
    Lista todos os utilizadores armazenados em um ficheiro JSON.

    Esta função lê os dados do ficheiro JSON especificado (por defeito `utilizadores.json`) 
    localizado na pasta `src/jsons` e imprime uma tabela formatada com as informações 
    de cada utilizador, incluindo nome, idade, email e tipo de permissão.

    Args:
        ficheiro (str, opcional): Nome do ficheiro JSON a ser lido. Padrão é `"utilizadores.json"`.

    Exceções tratadas:
        FileNotFoundError: Caso o ficheiro não exista.
        json.JSONDecodeError: Caso o conteúdo do ficheiro não seja um JSON válido.
        Exception: Captura quaisquer outros erros inesperados durante a execução.

    Saída:
        Imprime uma tabela com os utilizadores ou mensagens de erro apropriadas se houver problemas
        com o ficheiro ou se a lista de utilizadores estiver vazia.

    Exemplo de uso:
        listar_utilizadores()
    """
    try:
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            utilizadores = json.load(file)

        if not utilizadores:
            print("Nenhum utilizador encontrado no ficheiro.")
            return

        # Cabeçalho
        print(f"{'Nome':<15} {'Idade':<10} {'Email':<30} {'Permissão':<20}")
        print("=" * 80)

        # Corpo da tabela
        for u in utilizadores:
            print(f"{u['nome']:<15} {str(u['idade']):<10} {u['email']:<30} {u['permissao']:<20}")

    except FileNotFoundError:
        print("O ficheiro não foi encontrado na pasta 'src/jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o JSON — formato inválido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def listagem_utilizadores():
    """
    Função auxiliar para iniciar a listagem de utilizadores.

    Esta função simplesmente chama `listar_utilizadores()` sem argumentos, utilizando o ficheiro
    padrão `utilizadores.json`.

    Exemplo de uso:
        listagem_utilizadores()
    """
    listar_utilizadores()

import json
import os

def listar_utilizadores(ficheiro="utilizadores.json"):
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
    listar_utilizadores()

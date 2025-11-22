import json
import os

def listar_chefes(ficheiro="chefes_equipas.json"):  
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
    listar_chefes()

import json
import os

def listar_carros(ficheiro="carros.json"):
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
    listar_carros()

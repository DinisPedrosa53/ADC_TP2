import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_membro_equipas(ficheiro="membro_equipas.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Idade':<15} {'Equipa':<15} {'Vitorias':<15} {'Pontos':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['idade']:<15} {equipa['peso']:<15} {equipa['equipa_atual']:<15}  ")
        else:
            print("Nenhum membro_equipa encontrado no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'membro_equipas.json' não foi encontrado na pasta 'Json'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_membro_equipas():
    listar_membro_equipas()
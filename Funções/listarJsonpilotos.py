import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_pilotos(ficheiro="pilotos.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("Jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Idade':<15} {'Peso':<15} {'Equipa':<15} {'Vitorias':<15} {'Pontos':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['idade']:<15} {equipa['peso']:<15} {equipa['equipa_atual']:<15} {equipa['vitorias']:<15} {equipa['pontosPiloto']:<15}")
        else:
            print("Nenhum piloto encontrado no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'pilotos.json' não foi encontrado na pasta 'Json'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_pilotos():
    listar_pilotos()
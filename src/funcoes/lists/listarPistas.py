import json
import os

# Função para listar as pistas do ficheiro JSON
def listar_pistas(ficheiro="pistas.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            pistas = json.load(file)

        # Verificando se há pistas no ficheiro
        if pistas:
            print(f"{'Nome':<20} {'Distancia':<15} {'Nº Curvas':<15} {'Recorde':<15}")
            print("="*95)

            # Listando as pistas
            for pista in pistas:
                print(f"{pista['nome']:<20} {pista['distancia']:<15} {pista['ncurvas']:<15} {pista['recordevolta']:<15}")
        else:
            print("Nenhuma pista encontrada no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'pistas.json' não foi encontrado na pasta 'jsons'.")
        
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_pistas():
    listar_pistas()
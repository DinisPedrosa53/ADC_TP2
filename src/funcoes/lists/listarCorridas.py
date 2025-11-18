import json
import os

# Função para listar as corridas do ficheiro JSON
def listar_corridas(ficheiro="corridas.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            corridas = json.load(file)

        # Verificando se há corridas no ficheiro
        if corridas:
            print(f"{'Nome':<20} {'pódio':<15} {'país 1':<15} {'cidade':<15} {'tempo':<15} {'data':<15} {'bilhete':<15} {'hórario':<15}")
            print("="*95)

            # Listando as corridas
            for corrida in corridas:
                print(f"{corrida['nome']:<20} {corrida['podio']:<15} {corrida['pais']:<15} {corrida['cidade']:<15} {corrida['tempo']:<15} {corrida['data']:<15} {corrida['bilhete']:<15} {corrida['horario']:<15}")
        else:
            print("Nenhuma corrida encontrada no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'corridas.json' não foi encontrado na pasta 'jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_corridas():
    listar_corridas()
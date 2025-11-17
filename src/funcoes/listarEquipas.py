import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_equipas(ficheiro="equipas.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Piloto 1':<15} {'Piloto 2':<15} {'Presidente':<15} {'Fundador':<15} {'Pontos':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['piloto1']:<15} {equipa['piloto2']:<15} {equipa['presidente']:<15} {equipa['fundador']:<15} {equipa['pontosEquipa']:<15}")
        else:
            print("Nenhuma equipa encontrada no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'equipas.json' não foi encontrado na pasta 'jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_equipas():
    listar_equipas()
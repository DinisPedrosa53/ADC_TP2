import json
import os

# Função para listar as equipas do ficheiro JSON
def listar_membro_equipas(ficheiro="membro_equipas.json"):
    try:
        # Construir caminho para o ficheiro na pasta "Json"
        caminho_ficheiro = os.path.join("src/jsons", ficheiro)

        # Abrir o ficheiro JSON e carregar os dados
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            equipas = json.load(file)

        # Verificando se há equipas no ficheiro
        if equipas:
            print(f"{'Nome':<20} {'Idade':<15}  {'salario':<15} {'equipa Atual':<15} {'equipas':<15} {'tipo':<15}")
            print("="*95)

            # Listando as equipas
            for equipa in equipas:
                print(f"{equipa['nome']:<20} {equipa['idade']:<15} {equipa['salario']:<15}  {equipa['equipa_atual']:<15}  {equipa['equipas']:<15} {equipa['tipo']:<15} ")
        else:
            print("Nenhum membro_equipa encontrado no ficheiro.")
    except FileNotFoundError:
        print("O ficheiro 'membro_equipas.json' não foi encontrado na pasta 'Json'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")

# Função principal
def listagem_membro_equipas():
    listar_membro_equipas()
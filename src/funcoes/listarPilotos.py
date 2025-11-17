import json
import os

# Função para listar os pilotos do ficheiro JSON
def listar_pilotos(ficheiro="pilotos.json", ordenar_por=None):
    caminho_ficheiro = os.path.join("src/jsons", ficheiro)

    try:
        with open(caminho_ficheiro, "r", encoding="utf-8") as file:
            pilotos = json.load(file)

        if not pilotos:
            print("Nenhum piloto encontrado no ficheiro.")
            return

        # Ordenar os pilotos se necessário
        if ordenar_por == "nome":
            pilotos.sort(key=lambda x: x["nome"].lower())
        elif ordenar_por == "pontos":
            # Converter pontos para inteiro antes de ordenar
            pilotos.sort(key=lambda x: int(x.get("pontosPiloto", 0)), reverse=True)

        # Cabeçalho
        print(f"{'Nome':<20} {'Idade':<6} {'Peso':<6} {'Equipa':<15} {'Vitorias':<8} {'Pontos':<8}")
        print("="*70)

        # Listar pilotos
        for piloto in pilotos:
            print(f"{piloto['nome']:<20} {piloto['idade']:<6} {piloto['peso']:<6} "
                  f"{piloto['equipa_atual']:<15} {piloto['vitorias']:<8} {piloto['pontosPiloto']:<8}")

    except FileNotFoundError:
        print("O ficheiro 'pilotos.json' não foi encontrado na pasta 'jsons'.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro JSON. Ele pode estar corrompido ou mal formatado.")


# Função principal para chamar a listagem
def listagem_pilotos():
    print("Como deseja ordenar os pilotos?")
    print("1 - Alfabeticamente")
    print("2 - Por pontos")
    escolha = input("Escolha: ")

    if escolha == "1":
        listar_pilotos(ordenar_por="nome")
    elif escolha == "2":
        listar_pilotos(ordenar_por="pontos")
    else:
        print("Opção inválida, listando sem ordenação.")
        listar_pilotos()

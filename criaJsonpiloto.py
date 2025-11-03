import json
import os

def obter_dados():
    dados = {}
    dados["nome"] = input("Digite o nome completo do piloto: ")
    dados["idade"] = input("Digite a idade do piloto: ")
    dados["altura"] = input("Digite a altura do piloto(em cm): ")
    dados["peso"] = input("Digite o peso do piloto(em kg): ")
    dados["equipas"] = input("Digite as equipas que o piloto ja participou (separados por vírgula): ")
    dados["telefone"] = input("Digite o número de telefone do piloto: ")
    dados["morada"] = input("Digite a morada do piloto: ")
    dados["equipa_atual"] = input("Digite a equipa que o piloto se encontra atualmente: ")
    dados["pontosPiloto"] = input("Digite o número de pontos do piloto principal: ")
    dados["vitorias"] = input("Digite o número de vitórias do piloto: ")
    dados["salario"] = input("Digite o salário anual do piloto (em euros): ")
    
    return dados

# Função para adicionar um novo piloto ao ficheiro JSON
def adicionar_piloto_ao_ficheiro(novo_piloto, ficheiro="pilotos.json"):
    # Verifica se o ficheiro já existe
    if os.path.exists(ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
        with open(ficheiro, "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        # Se o ficheiro não existe, cria uma lista vazia
        dados = []

    # Adiciona um piloto à lista de pilotos
    dados.append(novo_piloto)

    # Salva os dados (incluindo o novo piloto) no ficheiro JSON
    with open(ficheiro, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print("Novo piloto adicionado com sucesso!")


# Função principal para adicionar um piloto
def main():
    novo_piloto = obter_dados()
    adicionar_piloto_ao_ficheiro(novo_piloto)

# Chamada principal
main()
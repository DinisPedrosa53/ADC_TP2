import json
import os

def listarPontosEquipas(equipas="equipas.json"):  
        caminho_ficheiro = os.path.join("jsons", equipas)
        if os.path.exists(caminho_ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
            with open(caminho_ficheiro, "r", encoding="utf-8") as file:
                dadosEquipas = json.load(file)
            return dadosEquipas
        else:
            print("Ficheiro não encontrado.")


        # Ordenar equipas por pontos (decrescente)
        dadosEquipas_ordenado = sorted(dadosEquipas, key=lambda x: x['pontos'], reverse=True)
        for equipa in dadosEquipas_ordenado:
            print(f"Equipa: {equipa['nome']}, Pontos: {equipa['pontos']}")


def listarPontosPilotos(pilotos="pilotos.json"):
        caminho_ficheiro = os.path.join("jsons", pilotos)
        if os.path.exists(caminho_ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
            with open(caminho_ficheiro, "r", encoding="utf-8") as file:
                dadosPilotos = json.load(file)
            return dadosPilotos
        else:
            print("Ficheiro não encontrado.")


        # Ordenar pilotos por pontos (decrescente)
        dadosPilotos_ordenado = sorted(dadosPilotos, key=lambda x: x['pontosPiloto'], reverse=True)
        for piloto in dadosPilotos_ordenado:
            print(f"Piloto: {piloto['piloto']}, Pontos: {piloto['pontosPiloto']}")


        
       
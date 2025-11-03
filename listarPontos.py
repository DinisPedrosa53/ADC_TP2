import json
import os

def listarPontos(equipas="equipas.json", pilotos="pilotos.json"):
        if os.path.exists(equipas):
        # Se o ficheiro existe, abre e carrega os dados existentes
            with open(equipas, "r", encoding="utf-8") as file:
                dadosEquipas = json.load(file)
            return dadosEquipas
        else:
            print("Ficheiro não encontrado.")

        if os.path.exists(pilotos):
        # Se o ficheiro existe, abre e carrega os dados existentes
            with open(pilotos, "r", encoding="utf-8") as file:
                dadosPilotos = json.load(file)
            return dadosPilotos
        else:
            print("Ficheiro não encontrado.")

        

        for equipa in dadosEquipas:
            print(f"Equipa: {equipa['nome']}, Pontos: {equipa['pontos']}")

        for piloto in dadosPilotos:
            print(f"Piloto: {piloto['piloto']}, Pontos: {piloto['pontosPiloto']}")




        
       
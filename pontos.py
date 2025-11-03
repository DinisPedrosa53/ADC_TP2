import json
import os

def printPontos(ficheiro="equipas.json"):
        if os.path.exists(ficheiro):
        # Se o ficheiro existe, abre e carrega os dados existentes
            with open(ficheiro, "r", encoding="utf-8") as file:
                dados = json.load(file)
            return dados
        else:
            print("Ficheiro não encontrado.")

        for equipa in dados:
            print(f"Equipa: {equipa['nome']}, Pontos: {equipa['pontos']}")

        for piloto in dados:
            print(f"Piloto: {piloto['piloto1']}, Pontos: {piloto['pontosPiloto1']}")
            print(f"Piloto: {piloto['piloto2']}, Pontos: {piloto['pontosPiloto2']}")



        
       
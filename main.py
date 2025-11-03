# Ficheiro main do projeto
import os
import json
from criaJsonequipas import criar_equipa
from criaJsonpiloto import criar_piloto
from listarPontos import *

while True:
    os.system("cls")
    print("Menu")
    print("Opções")
    print("1-Utilizadores")
    print("2-Equipas")
    print("3-Pilotos")
    print("4-")
    print("0- Sair")
    opcao1 = input("Escolha: ")

    if opcao1 == "1":
        os.system("cls")
        print("Menu -> Utilizadores")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        opcao2 = input("Escolha: ")
    elif opcao1 == "2":
        os.system("cls")
        print("Menu -> Equipas")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        opcao2 = input("Escolha: ")  

        if opcao2 == "1":
            criar_equipa()

        if opcao2 == "2":
            listarPontosEquipas()

    elif opcao1 == "3":
        os.system("cls")
        print("Menu -> Pilotos")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        opcao2 = input("Escolha: ")

        if opcao2 == "1":
            criar_piloto()

        if opcao2 == "2":
            listarPontosPilotos()
            
    elif opcao1 == "0":
            print("Saindo... Até logo!")
            break  # Sai do loop e termina o programa

# Ficheiro main do projeto
import os
import json
from funcoes.criarEquipas import criar_equipa
from funcoes.criarPiloto import criar_piloto
from funcoes.criarCorrida import criar_corrida
from funcoes.criarMembroEquipa import criar_membro_equipa
from funcoes.listarPontos import *
from funcoes.listarEquipas import listagem_equipas
from funcoes.listarPilotos import listagem_pilotos
from funcoes.listarMembroEquipa import listagem_membro_equipas
from funcoes.listarCorridas import listagem_corridas
from funcoes.editarEquipa import editar_equipa
from funcoes.editarPiloto import editar_piloto

#   Parte para fazer login antes de ter acesso ao menu
#   para que depois seja possível tratar de como as permissões vão funcionar
#
# Menu básico com loop para manipular dados nos ficheiros JSON
while True:
    os.system("cls")
    print("Menu")
    print("Opções")
    print("1- Utilizadores")
    print("2- Equipas")
    print("3- Pilotos")
    print("4- Chefes")
    print("5- Membros de Equipas")
    print("6- Corridas")
    print("0- Sair")
    opcao1 = input("Escolha: ")

    if opcao1 == "1":
        os.system("cls")
        print("Menu -> Utilizadores")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        opcao2 = input("Escolha: ")
        if opcao2 == "1":
            os.system("cls")
            # Chamar função para criar utilizador
            pass  # Placeholder for user creation function

        elif opcao2 == "2":
            os.system("cls")
            # Chamar função para listar utilizadores
            pass  # Placeholder for user listing function
        
    elif opcao1 == "2":
        os.system("cls")
        print("Menu -> Equipas")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        print("3- Editar")
        print("4- Apagar")
        opcao2 = input("Escolha: ")  

        if opcao2 == "1":
            os.system("cls")
            criar_equipa()
        elif opcao2 == "2":
            os.system("cls")
            listagem_equipas()
            print("")
            input("Enter para continuar...")
        elif opcao2 == "3":
            os.system("cls")
            editar_equipa()
            input("Enter para continuar...")
            

    elif opcao1 == "3":
        os.system("cls")
        print("Menu -> Pilotos")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        print("3- Editar")
        print("4- Apagar")
        opcao2 = input("Escolha: ")

        if opcao2 == "1":
            os.system("cls")
            criar_piloto()           
        elif opcao2 == "2":
            os.system("cls")
            listagem_pilotos()
            input("Enter para continuar...")
        elif opcao2 == "3":
            os.system("cls")
            editar_piloto()
            input("Enter para continuar...")

    elif opcao1 == "4":
        os.system("cls")
        print("Menu -> Chefes")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        print("3- Editar")
        print("4- Apagar")
        opcao2 = input("Escolha: ")

        if opcao2 == "1":
            os.system("cls")
            
        elif opcao2 == "2":
            os.system("cls")
            
            input("Enter para continuar...")

    elif opcao1 == "5":
        os.system("cls")
        print("Menu -> Membros de Equipa")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        print("3- Editar")
        print("4- Apagar")
        opcao2 = input("Escolha: ")

        if opcao2 == "1":
            os.system("cls")
            criar_membro_equipa()
            
        elif opcao2 == "2":
            os.system("cls")
            listagem_membro_equipas()
            input("Enter para continuar...")

    elif opcao1 == "6":
        os.system("cls")
        print("Menu -> Corridas")
        print("Opções")
        print("1- Criar")
        print("2- Listar")
        print("3- Editar")
        print("4- Apagar")
        opcao2 = input("Escolha: ")

        if opcao2 == "1":
            os.system("cls")
            criar_corrida()
            
        elif opcao2 == "2":
            os.system("cls")
            listagem_corridas()
            input("Enter para continuar...")
            
    elif opcao1 == "0":
            print("Saindo...")
            break  # Sai do loop e termina o programa

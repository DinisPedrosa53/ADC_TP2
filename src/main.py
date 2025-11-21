import os
import json
from funcoes.creates.user_creator import user_creator
from funcoes.user_login import login
from funcoes.creates.criarEquipas import criar_equipa
from funcoes.creates.criarPiloto import criar_piloto
from funcoes.creates.criarCorrida import criar_corrida
from funcoes.creates.criarCarro import criar_carro
from funcoes.creates.criarMembroEquipa import criar_membro_equipa
from funcoes.creates.criarPista import criar_pista
from funcoes.lists.listarPontos import *
from funcoes.lists.listarEquipas import listagem_equipas
from funcoes.lists.listarCarros import listagem_carros
from funcoes.lists.listarPilotos import listagem_pilotos
from funcoes.lists.listarMembroEquipa import listagem_membro_equipas
from funcoes.lists.listarCorridas import listagem_corridas
from funcoes.lists.listarPistas import listagem_pistas
from funcoes.edits.editarEquipa import editar_equipa
from funcoes.edits.editarPiloto import editar_piloto
from funcoes.deletes.apagarEquipas import apagar_equipa
from funcoes.deletes.apagarPilotos import apagar_piloto


inform = None

# Menu básico com loop para manipular dados nos ficheiros JSON
def main(permissao):
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
        print("7- Pistas")
        print("8- Carros")
        print("0- Sair")
        opcao1 = input("Escolha: ")

        if opcao1 == "1" and (permissao == "admin"):
            os.system("cls")
            print("Menu -> Utilizadores")
            print("Opções")
            print("1- Criar")
            print("2- Listar")
            opcao2 = input("Escolha: ")
            if opcao2 == "1":
                os.system("cls")
                user_creator()

            elif opcao2 == "2":
                os.system("cls")
                # Chamar função para listar utilizadores
                pass  # Placeholder for user listing function
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
                input("Enter para continuar...")
            
        elif opcao1 == "2":
            os.system("cls")
            print("Menu -> Equipas")
            print("Opções")
            print("1- Criar")
            print("2- Listar")
            print("3- Editar")
            print("4- Apagar")
            opcao2 = input("Escolha: ")  

            if opcao2 == "1" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                criar_equipa()
            elif opcao2 == "2":
                os.system("cls")
                listagem_equipas()
                print("")
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                editar_equipa()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                apagar_equipa()
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
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

            if opcao2 == "1" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                criar_piloto()           
            elif opcao2 == "2":
                os.system("cls")
                listagem_pilotos()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                editar_piloto()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                apagar_piloto()
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
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

            if opcao2 == "1" and (permissao == "admin"):
                os.system("cls")
                
            elif opcao2 == "2":
                os.system("cls")
                
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
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

            if opcao2 == "1"  and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                criar_membro_equipa()
                
            elif opcao2 == "2":
                os.system("cls")
                listagem_membro_equipas()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
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

            if opcao2 == "1"  and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                criar_corrida()
                
            elif opcao2 == "2":
                os.system("cls")
                listagem_corridas()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
                input("Enter para continuar...")


        elif opcao1 == "7":
            os.system("cls")

            print("Menu -> Pistas")
            print("Opções")
            print("1- Criar")
            print("2- Listar")
            print("3- Editar")
            print("4- Apagar")
            opcao2 = input("Escolha: ")

            if opcao2 == "1"  and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                criar_pista()

            elif opcao2 == "2":
                os.system("cls")
                listagem_pistas()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
                input("Enter para continuar...")


        elif opcao1 == "8":
            os.system("cls")
            print("Menu -> Carros")
            print("Opções")
            print("1- Criar")
            print("2- Listar")
            print("3- Editar")
            print("4- Apagar")
            opcao2 = input("Escolha: ")

            if opcao2 == "1"  and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                criar_carro()
                
            elif opcao2 == "2":
                os.system("cls")
                listagem_carros()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                #placeholde função
                input("Enter para continuar...")
            else:
                os.system("cls")
                print("Opção inválida/ permissão negada.")
                input("Enter para continuar...")
                
        elif opcao1 == "0":
                os.system("cls")
                print("Saindo...")
                break  # Sai do loop e termina o programa
        else:
            os.system("cls")
            print("Opção inválida/ permissão negada.")
            input("Enter para continuar...")



while True:

    escolha = input("1 - criar utilizador\n2 - login\nEscolha: ")
    if escolha == "1":
        user_creator()
    elif escolha == "2":
        inform = login()
        break
name = inform[0]
permissao = inform[1]

if permissao == "admin":
    main(permissao)
elif permissao == "chefe de corrida":
    main(permissao)
elif permissao == "FIA":
    main(permissao)
elif permissao == "utilizador":
    main(permissao)
        
if __name__ == "__main__":
    main()

import os
import json
from funcoes.creates.criarUtilizador import criar_utilizador
from funcoes.loginUtilizadores import login
from funcoes.creates.criarEquipas import criar_equipa
from funcoes.creates.criarPiloto import criar_piloto
from funcoes.creates.criarCorrida import criar_corrida
from funcoes.creates.criarCarro import criar_carro
from funcoes.creates.criarMembroEquipa import criar_membro_equipa
from funcoes.creates.criarPista import criar_pista
from funcoes.creates.criarChefeEquipa import criar_chefe

from funcoes.lists.listarPontos import *
from funcoes.lists.listarEquipas import listagem_equipas
from funcoes.lists.listarCarros import listagem_carros
from funcoes.lists.listarPilotos import listagem_pilotos
from funcoes.lists.listarMembroEquipa import listagem_membro_equipas
from funcoes.lists.listarCorridas import listagem_corridas
from funcoes.lists.listarPistas import listagem_pistas
from funcoes.lists.listarUtilizadores import listagem_utilizadores
from funcoes.lists.listarChefes import listagem_chefes

from funcoes.edits.editarEquipa import editar_equipa
from funcoes.edits.editarPiloto import editar_piloto
from funcoes.edits.editarCorrida import editar_corrida
from funcoes.edits.editarCarro import editar_carro
from funcoes.edits.editarMembro import editar_membro
from funcoes.edits.editarPista import editar_pista
from funcoes.edits.editarUtilizador import editar_utilizador
from funcoes.edits.editarChefeEquipa import editar_chefe_equipa

from funcoes.deletes.apagarEquipas import apagar_equipa
from funcoes.deletes.apagarPilotos import apagar_piloto
from funcoes.deletes.apagarCarros import apagar_carro
from funcoes.deletes.apagarCorridas import apagar_corrida
from funcoes.deletes.apagarUtilizadores import apagar_utilizador
from funcoes.deletes.apagarPistas import apagar_pista
from funcoes.deletes.apagarMembrosEquipas import apagar_membro_equipa
from funcoes.deletes.apagarChefesEquipas import apagar_chefe_equipa


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
            print("3- Editar")
            print("4- Apagar")
            opcao2 = input("Escolha: ")
            if opcao2 == "1":
                os.system("cls")
                criar_utilizador()
            elif opcao2 == "2":
                os.system("cls")
                listagem_utilizadores()
                input("Enter para continuar...")
            elif opcao2 == "3":
                os.system("cls")
                editar_utilizador()
                input("Enter para continuar...")
            elif opcao2 == "4":
                os.system("cls")
                apagar_utilizador()
                input("Enter para continuar...")
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
                criar_chefe()
            elif opcao2 == "2":
                os.system("cls")
                listagem_chefes()
                input("Enter para continuar...")
            elif opcao2 == "3" and (permissao == "admin"):
                os.system("cls")
                editar_chefe_equipa()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin"):
                os.system("cls")
                apagar_chefe_equipa()
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
                editar_membro()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida" or permissao == "FIA"):
                os.system("cls")
                apagar_membro_equipa()
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
                editar_corrida()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                apagar_corrida()
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
                editar_pista()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "FIA"):
                os.system("cls")
                apagar_pista()
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
                editar_carro()
                input("Enter para continuar...")
            elif opcao2 == "4" and (permissao == "admin" or permissao == "chefe de corrida"):
                os.system("cls")
                apagar_carro()
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
        criar_utilizador()
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

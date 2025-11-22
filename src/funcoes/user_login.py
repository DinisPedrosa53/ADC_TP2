import json 
import os

filename = "src/jsons/user_data.json"

def login():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # If file is empty or invalid
    else:
        data = []

    while True:
        os.system("cls")
        name = input("Escreve o teu nome: ")
        user = next((user for user in data if user["nome"].lower() == name.lower()), None)
        if user:
            os.system("cls")
            password = input("Escreve a tua password: ")
            if password == user.get("password"):
                os.system("cls")
                print(f"Benvindo de volta, '{name}'!")
                permissao = user.get("permissao")
                input("Enter para continuar...")
                break
            else:
                os.system("cls")
                print("Password incorreta, por favor tente outra vez.")
        else:
            os.system("cls")
            print(f"O nome '{name}' nao existe. Por favor tente um nome diferente.")

    return name, permissao

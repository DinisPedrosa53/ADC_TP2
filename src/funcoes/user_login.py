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
        name = input("Escreve o teu nome: ")
        user = next((user for user in data if user["nome"].lower() == name.lower()), None)
        if user:
            password = input("Escreve a tua password: ")
            if password == user.get("password"):
                print(f"✅ Benvindo de volta, '{name}'!")
                permissao = user.get("permissao")
                break
            else:
                print("❌ Password incorreta, por favor tente outra vez.")
        else:
            print(f"⚠️ O nome '{name}' nao existe. Por favor tente um nome diferente.")

    return name, permissao
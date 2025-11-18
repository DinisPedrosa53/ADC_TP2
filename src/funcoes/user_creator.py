import json
import os

# File name
filename = "src/jsons/user_data.json"

# Step 1: Load existing data if the file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []  # If file is empty or invalid
else:
    data = []

# Step 2: Ask for name until it's unique
while True:
    name = input("Escreve o teu nome: ")
    if any(user["nome"].lower() == name.lower() for user in data):
        print(f"⚠️ O nome '{name}' ja existe. Por favor escolhe um nome diferente.")
    else:
        break

# Step 3: Ask for other info
age = int(input("qual é a tua idade: "))
email = input("escreve o teu email: ")
password = input("qual a tua password: ")
print("1 - admin")
print("2 - chefe de corrida")
print("3 - FIA")
print("4 - utilizador")
while True:
    try:
        permissao = int(input("qual a tua permissão: "))
        if permissao < 1 or permissao > 4:
            print("erro, permissão invalida")
        else:
            break
    except:
        print("digite um valor valido")
    
if permissao == 1:
    permissao = "admin"
elif permissao == 2:
    permissao = "chefe de corrida"
elif permissao == 3:
    permissao = "FIA"
elif permissao == 4:
    permissao = "utilizador"

# Step 4: Create new user record
new_user = {
    "nome": name,
    "idade": age,
    "email": email,
    "password" : password,
    "permissao" : permissao
}

# Step 5: Append and save
data.append(new_user)

with open(filename, "w") as file:
    json.dump(data, file, indent=4)

print(f"✅ New user '{name}' added successfully!")

import json 
import os

filename = "src/jsons/utilizadores.json"

def login():
    """
    Função para autenticar um utilizador existente.

    Esta função permite que um utilizador faça login no sistema através do terminal.
    Os dados dos utilizadores são armazenados em ficheiros JSON localizados em `src/jsons/utilizadores.json`.

    Funcionamento:
        1. Verifica se o ficheiro de utilizadores existe; caso contrário, inicializa uma lista vazia.
        2. Solicita ao utilizador o nome.
        3. Verifica se o nome existe na lista de utilizadores.
        4. Se existir, pede a password e valida.
        5. Se o login for bem-sucedido, retorna o nome do utilizador e o nível de permissão.
        6. Em caso de erro (nome inexistente ou password incorreta), repete o processo até sucesso.

    Returns:
        tuple: Retorna uma tupla contendo:
            - `name` (str): Nome do utilizador autenticado
            - `permissao` (str): Nível de permissão do utilizador (`admin`, `chefe de corrida`, `FIA`, `utilizador`)

    Outras ações:
        - A função limpa o terminal (`os.system("cls")`) entre os inputs para melhorar a experiência do utilizador.
        - A função mantém o loop até que um login válido seja efetuado.
        - Utiliza a correspondência de nomes de utilizador de forma **case-insensitive**.
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
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

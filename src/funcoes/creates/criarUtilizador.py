import json
import os

filename = "src/jsons/utilizadores.json"
def criar_utilizador():
    """
    Cria e regista um novo utilizador no sistema.

    Esta função recolhe dados através do terminal e adiciona um novo
    utilizador ao ficheiro JSON `utilizadores.json`. Inclui validações
    importantes, tais como:

    - Verificação da existência do ficheiro JSON.
    - Tratamento de ficheiros JSON corrompidos ou vazios.
    - Garantia de que não existem nomes duplicados.
    - Validação da permissão escolhida (1 a 4).
    - Conversão automática do número da permissão para o respetivo nome.

    O utilizador insere:
        - nome (único)
        - idade
        - email
        - password
        - permissão (admin, chefe de corrida, FIA ou utilizador)

    Após validar todos os dados, o novo utilizador é guardado no ficheiro JSON.

    Outras ações:
        - Limpa o ecrã repetidamente com `os.system("cls")`.
        - Lê e escreve no ficheiro JSON.
        - Imprime mensagens de estado no terminal.
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
        if any(user["nome"].lower() == name.lower() for user in data):
            os.system("cls")
            print(f"O nome '{name}' ja existe. Por favor escolhe um nome diferente.")
        else:
            break

    os.system("cls")
    age = int(input("qual é a tua idade: "))
    os.system("cls")
    email = input("escreve o teu email: ")
    os.system("cls")
    password = input("qual a tua password: ")
    print("1 - admin")
    print("2 - chefe de corrida")
    print("3 - FIA")
    print("4 - utilizador")
    while True:
        try:
            permissao = int(input("qual a tua permissão: "))
            if permissao < 1 or permissao > 4:
                os.system("cls")
                print("erro, permissão invalida")
            else:
                break
        except:
            os.system("cls")
            print("digite um valor valido")
        
    if permissao == 1:
        permissao = "admin"
    elif permissao == 2:
        permissao = "chefe de corrida"
    elif permissao == 3:
        permissao = "FIA"
    elif permissao == 4:
        permissao = "utilizador"

    new_user = {
        "nome": name,
        "idade": age,
        "email": email,
        "password" : password,
        "permissao" : permissao
    }

    data.append(new_user)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    os.system("cls")
    print(f"Novo utilizador '{name}' adicionado com sucesso!")

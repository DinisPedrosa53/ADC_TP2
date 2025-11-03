import json 
import os

filename = "user_data.json"

def lobby(name):
    print(f"Entering lobby for {name}...")

if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []  # If file is empty or invalid
else:
    data = []

while True:
    name = input("Enter your name: ")
    user = next((user for user in data if user["name"].lower() == name.lower()), None)
    if user:
        password = input("Enter your password: ")
        if password == user.get("password"):
            print(f"✅ Welcome back, '{name}'!")
            lobby(name)
            break
        else:
            print("❌ Incorrect password. Please try again.")
    else:
        print(f"⚠️ The name '{name}' does not exist. Please enter a different name.")
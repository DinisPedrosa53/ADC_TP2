import json
import os

# File name
filename = "user_data.json"

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
    name = input("Enter your name: ")
    if any(user["name"].lower() == name.lower() for user in data):
        print(f"⚠️ The name '{name}' is already taken. Please enter a different name.")
    else:
        break

# Step 3: Ask for other info
age = int(input("Enter your age: "))
email = input("Enter your email: ")
password = input("Enter your password: ")

# Step 4: Create new user record
new_user = {
    "name": name,
    "age": age,
    "email": email,
    "password" : password
}

# Step 5: Append and save
data.append(new_user)

with open(filename, "w") as file:
    json.dump(data, file, indent=4)

print(f"✅ New user '{name}' added successfully!")

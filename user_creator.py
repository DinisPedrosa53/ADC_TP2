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
            data = []  # Empty or invalid file — start fresh
else:
    data = []  # File doesn’t exist yet


# Step 2: Determine the next user ID
if data:
    last_id = max(user["id"] for user in data)
else:
    last_id = 0

next_id = last_id + 1

# Step 3: Ask for new user info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")

# Step 4: Create new user record
new_user = {
    "id": next_id,
    "name": name,
    "age": age,
    "email": email
}

# Step 5: Append new data and save
data.append(new_user)

with open(filename, "w") as file:
    json.dump(data, file, indent=4)

print(f"✅ New user added successfully with ID {next_id}!")
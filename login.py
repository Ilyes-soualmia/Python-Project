import json

def login(username):
    
    with open("user.json", "r") as f:
        users = json.load(f)
    if username in users:
        print(f"Welcome {username}")
    else:
        users.append(username)
        with open("user.json", "w") as f:
            json.dump(users, f)
        print(f"User {username} added and logged in.")





user_input = input("Enter your username: ")
login(user_input)
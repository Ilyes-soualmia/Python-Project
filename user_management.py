import json
import hashlib
from datetime import datetime
import os

# Utility functions
def load_json(file_path, default_data):
    """Load data from a JSON file, creating it if it doesn't exist."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump(default_data, file, indent=4)
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# File paths
USERS_FILE = 'QCM/users.json'
HISTORY_FILE = 'QCM/history.json'

# Default structures
DEFAULT_USERS = {"users": []}
DEFAULT_HISTORY = {"history": []}

# Load and save functions
def load_users():
    return load_json(USERS_FILE, DEFAULT_USERS)

def save_users(users):
    save_json(USERS_FILE, users)

def load_history():
    return load_json(HISTORY_FILE, DEFAULT_HISTORY)

def save_history(history):
    save_json(HISTORY_FILE, history)

# Core functionality
def login():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in users['users']:
        if user['username'] == username:
            if user['password'] == hashed_password:
                print("Login successful!")
                return username
            else:
                print("Incorrect password!")
                return None

    print("User not found. Creating new user...")
    users['users'].append({
        "username": username,
        "password": hashed_password
    })
    save_users(users)
    print("User created successfully!")
    return username

def record_exam_result(username, module, score):
    history = load_history()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history['history'].append({
        "username": username,
        "module": module,
        "score": score,
        "date": current_time
    })
    save_history(history)
    print(f"Exam history recorded for {username}: {module} - {score} on {current_time}")

def view_exam_history(username):
    history = load_history()
    user_history = [entry for entry in history['history'] if entry['username'] == username]

    if user_history:
        print(f"Exam history for {username}:")
        for entry in user_history:
            print(f"Module: {entry['module']}, Score: {entry['score']}, Date: {entry['date']}")
    else:
        print(f"No exam history found for {username}.")

if __name__ == "__main__":
    username = login()
    if username:
        record_exam_result(username, "Python", 85) 
        view_exam_history(username)


from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt
import json
import hashlib
from datetime import datetime
import os

console = Console()
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
USERS_FILE = 'Users.json'
HISTORY_FILE = 'History.json'

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
    username = Prompt.ask("[bold cyan]Enter your name[/bold cyan]")
    password = Prompt.ask("[bold cyan]Enter your password[/bold cyan]")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    for user in users['users']:
        if user['username'] == username and user['password'] == hashed_password:
            console.print("[bold green]Login successful![/bold green]")
            return username
    console.print("[red]User not found.[/red]")
    console.print("[blue]Creating new user...[/blue]")
    users['users'].append({
        "username": username,
        "password": hashed_password,
        "exam_results": []
    })
    save_users(users)
    console.print("[bold green]User created successfully![/bold green]")
    return username

def record_exam_result(username, module, score):
    users = load_users()
    for user in users['users']:
        if user['username'] == username:
            current_date = datetime.now().strftime("%Y-%m-%d")
            user['exam_results'].append({
                "module": module,
                "score": score,
                "date": current_date
            })
            save_users(users)
            print(f"Exam result recorded for {username}: {module} - {score}")
            log_exam_history(username, module, score)
            return
    print("User not found!")

def log_exam_history(username, module, score):
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

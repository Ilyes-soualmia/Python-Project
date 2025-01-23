from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt
import json
import hashlib
from datetime import datetime
import os
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
import re

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
        if user['username'] == username:
            if user['password'] == hashed_password:
                console.print("[bold green]Login successful![/bold green]")
                return username
            else:
                console.print("[red]Username already exists , and password is wrong[/red]")
                return login()
    email = Prompt.ask("[bold cyan]Enter your email[/bold cyan]") #to be entered only once when the user is created
        
    console.print("[blue]Creating new user...[/blue]")
    users['users'].append({
        "username": username,
        "email": email,
        "password": hashed_password,
        "exam_results": []
    })
    save_users(users)
    console.print("[bold green]User created successfully![/bold green]")
    return username

def welcome(username):
    console.print(f"[bold green]Welcome, {username}![/bold green]")

def record_exam_result(username, module , exam , score ,remarks):
    users = load_users()
    for user in users['users']:
        if user['username'] == username:
            current_date = datetime.now().strftime("%Y-%m-%d")
            user['exam_results'].append({
                "module": module,
                "exam": exam,
                "score": score,
                "remarks": remarks,
                "date": current_date
            })
            save_users(users)
            print(f"Exam result recorded for {username}: {exam} - {score}")
            log_exam_history(username, module,exam, score,remarks)
            return
    print("User not found!")

def log_exam_history(username, module, exam , score,remarks):
    history = load_history()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history['history'].append({
        "username": username,
        "module": module,
        "exam": exam,
        "score": score,
        "remarks": remarks,
        "date": current_time
    })
    save_history(history)
    console.print(f"[bold blue]Exam history recorded successfully![/bold blue] for {username} : {module} - {score} on {current_time}")

def view_exam_history(username):
    history = load_history()
    user_history = [entry for entry in history['history'] if entry['username'] == username]
    if user_history:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Module", style="bold cyan")
        table.add_column("Exam", style="bold cyan")
        table.add_column("Score /20", style="bold cyan")
        table.add_column("Remarks", style="bold cyan")
        table.add_column("Date", style="bold cyan")
        for entry in user_history:
            table.add_row(entry['module'],entry['exam'], str(entry['score']), entry['remarks'],entry['date'])
        console.print(f"[bold blue]Exam history for {username}:[/bold blue]", justify="center")    
        console.print(table , justify="center")
    else:
        console.print("[blue]You have not taken any exams yet.[/blue]")

def remarks(score):
    if score >= 18:
        return "Excellent!"
    elif score >= 15:
        return "Good job!"
    elif score >= 10:
        return "Not bad!"
    else:
        return "You can do better!"
    

def Save_history_in_users_os(history):
    # Initialize the Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open a "Save As" dialog to let the user choose the folder and file name
    file_path = asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        title="Save user's History",
    )
    print("Opening file save dialog...")
    if file_path:
        try:
            # Create the JSON file and write the history to it
            with open(file_path, "w") as file:
                json.dump(history, file, indent=4)
            print(f"Exam history file created and saved to {file_path}")
            print("Done.")
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")
    else:
        print("Operation canceled by the user.")
    
    
def modify_user_infos(username):
    users = load_users()
    for user in users['users']:
        if user['username'] == username:
            console.print("[bold cyan]1. Change username[/bold cyan]")
            console.print("[bold cyan]2. Change password[/bold cyan]")
            console.print("[bold cyan]3. change email[/bold cyan]")
            console.print("[bold cyan]4. Cancel[/bold cyan]")
            while True:
                choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]")
                if choice == '1':
                    while True:
                        new_username = Prompt.ask("[bold cyan]Enter new username[/bold cyan]")
                        if any(u['username'] == new_username for u in users['users']):
                            user['username'] = new_username
                            break
                        console.print("[red]Username already exists![/red]")
                    save_users(users)
                    console.print("[bold green]Username changed successfully![/bold green]")
                elif choice == '2':
                    while True:
                        new_password = Prompt.ask("[bold cyan]Enter new password[/bold cyan]")
                        confirm_password = Prompt.ask("[bold cyan]Confirm new password[/bold cyan]")
                        if new_password != confirm_password:
                            console.print("[red]Passwords do not match![/red]")
                        else:
                            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                            user['password'] = hashed_password
                            save_users(users)
                            console.print("[bold green]Password changed successfully![/bold green]")
                            break
                        choice_2 = Prompt.ask("[bold yellow in white]Do you want to repeat(r) the operation?[/bold yellow in white]")
                        if choice_2 != 'r':
                            break
                elif choice == '3':
                    while True:
                        new_email = Prompt.ask("[bold cyan]Enter new email[/bold cyan]")
                        if validate_email(new_email):

                            break
                    user['email'] = new_email
                elif choice == '4':
                    console.print("[bold cyan]Operation canceled[/bold cyan]")
                    break
                else:
                    console.print("[red]Invalid choice![/red]")
    console.print("[red]User not found![/red]")

def validate_email(email):
    return bool(re.match(r'[^@]+@[^@]+\.[^@]+', email))


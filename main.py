from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import os
import qcm_handler as qcm
import user_data_handler as udh
import email_sender as es

data = qcm.load_data()

console = Console()
console.print("QUIZZY 🤖",justify="center" , style="bold red")
console.print("Welcome to the best QCM APP! 👍", justify="center", style="bold magenta")
print("\n")

username = udh.login()
udh.welcome(username)
print("\n")

if username:
    while True:
        console.print("[bold cyan]1. Take an exam[/bold cyan]")
        console.print("[bold cyan]2. View exam history[/bold cyan]")
        console.print("[bold cyan]3. download exam history[/bold cyan]")
        console.print("[bold cyan]4. modify user infos[/bold cyan]")
        console.print("[bold cyan]5. Logout[/bold cyan]")
        choice = input("Enter your choice: ")
        if choice == '1':
            subject = qcm.choose_subject()
            exam_name = qcm.show_exam_titles(data, subject)
            result = qcm.show_exam(data, subject, exam_name)
            remarks = udh.remarks(result)
            udh.record_exam_result(username, subject,exam_name, result , remarks)
            
            print(f"Your result is: {result} / 20")
            for key, value in qcm.temp_dect.items():
                if value:                       #if value is not empty 
                    print(f'{key}: {value}')
                else:                           #if value is empty, like it was the last question
                    break
        elif choice == '2':
            udh.view_exam_history(username)
        elif choice == '3':
            users = udh.load_users()
            for user in users['users']:
                if user['username'] == username:
                    if user['exam_results']:
                        console.print("     1. Save exam history in a file" , style="bold cyan")
                        console.print("     2. Send exam history to email" , style="bold cyan")
                        console.print("     3. Cancel" , style="bold cyan")
                        while True:
                            save_choice = Prompt.ask("Do you want to save your exam history? (1/2/3)")
                            if save_choice == '1':
                                udh.Save_history_in_users_os(user['exam_results'])
                            elif save_choice == '2':
                                es.send_email(username , user['exam_results'] , user['email'])
                                if os.path.exists("file.json"):
                                    os.remove("file.json")
                                break
                            elif save_choice == '3':
                                break
                            else:
                                console.print("Invalid choice. Please try again.", style="bold red")
                    else:
                        console.print("No results found!" , style="bold red")
        elif choice == '4':
            udh.modify_user_infos(username)
        elif choice == '5':
            console.print("Logging out...", style="bold red")
            while True:
                exit_choice = Prompt.ask("Do you want to exit the app? (yes/no)")
                if exit_choice == "yes": 
                    console.print("Goodbye! 👋", style="bold magenta")
                    break
                elif exit_choice == "no":
                    username = udh.login()
                    console.print(f"[bold green]Welcome back✨, {username}!, i knew you can't quit this beautiful app 😁[/bold green]")
                    break
                else:
                    console.print("Invalid choice. Please try again.", style="bold red") #aaaaaaah it's not that hard , just yes or no 
            if exit_choice == "yes":
                break  
        else:
            console.print("Invalid choice. Please try again.", style="bold red") 
        
    



   
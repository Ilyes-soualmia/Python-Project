from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import json
import qcm_handler as qcm
import user_data_handler as udh

# Main function
data = qcm.load_data()

console = Console()
message = Text("Welcome, that's me the best QCM APP! 👍", justify="center", style="bold magenta")
console.print(message)
print(2*"\n")

username = udh.login()
name = qcm.welcome()

if username:
    while True:
        print("1. Take an exam")
        print("2. View exam history")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            subject = qcm.choose_subject()
            exam_name = qcm.choose_exam(data, subject)
            result = qcm.show_exam(data, subject, exam_name)
            udh.record_exam_result(username, exam_name, result)
            
            #print result and correct answers
            print(f"Your result is: {result} / 10")
            for key, value in qcm.temp_dect.items():
                if value:                       #if value is not empty 
                    print(f'{key}: {value}')
                else:                           #if value is empty, like it was the last question
                    break

        elif choice == '2':
            udh.view_exam_history(username)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
        
    



   
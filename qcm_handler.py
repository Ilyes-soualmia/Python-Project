import json 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
temp_dect = {'question1':'','question2':'','question3':'','question4':'','question5':'','question6':'','question7':'','question8':'','question9':'','question10':'','question11':'','question12':'','question13':'','question14':'','question15':'','question16':'','question17':'','question18':'','question19':'','question20':''}

# Load the data from the json file
def load_data():
    with open("QCM.json", "r") as f:
        data = json.loads(f.read())
        return data

# choose subject function
def choose_subject():
    console.print("[bold cyan]Here are the available subjects: [/bold cyan]")
    data = load_data()
    for exam in data["exams"]:
        console.print(f"[bold magenta] | {exam["subject"]} [/bold magenta]")
    while True:
        subject = Prompt.ask("[bold cyan]Choose a subject: [/bold cyan] ")
        if subject.lower() in [exam["subject"].lower() for exam in data["exams"]]:
            return subject
        else:
            console.print("[red]Invalid choice. Please enter a valid subject.[/red]")

# show choosed subject function
def show_exam_titles(data, subject):
    console.print("[bold cyan]You have choosen the subject: [/bold cyan]")
    console.print("[bold cyan]Here are the available exams in the choosen subject: [/bold cyan]")
    for exam in data["exams"]:
        if exam["subject"].lower() == subject.lower():
            console.print(f"[bold magenta] | {exam["name"]} [/bold magenta]")
    exam_name = Prompt.ask("[bold cyan]Choose an exam: [/bold cyan] ")
    return exam_name

# show choosed exam function
def show_exam(data, subject , exam_name):
    result = 0
    console.print(f"[bold cyan]You have choosen the subject: [/bold cyan][bold magenta]{subject[0]}[/bold magenta]")
    console.print(f"[bold cyan]You have choosen the exam: [/bold cyan][bold magenta]{exam_name}[/bold magenta]")
    console.print("[bold cyan]Here are the questions: [/bold cyan]")

    for exam in data["exams"]:
        if exam["subject"] == subject and exam["name"] == exam_name:
            question_nbr = 1
            for question in exam["questions"]:
                console.print(f"[bold magenta]{question_nbr} / {question["question"]}: [/bold magenta]")
                console.print(f"[bold magenta]a) {question["options"][0]}[/bold magenta]")
                console.print(f"[bold magenta]b) {question["options"][1]}[/bold magenta]")
                console.print(f"[bold magenta]c) {question["options"][2]}[/bold magenta]")
                console.print(f"[bold magenta]d) {question["options"][3]}[/bold magenta]")
                while True:
                    answer = Prompt.ask("[bold cyan]Your answer(a,b,c or d) =>: [/bold cyan] ")
                    if answer.lower() in ["a", "b", "c", "d"]:
                        break
                    else:
                        console.print("[red]Invalid choice. Please try again.[/red]")

                if answer == question["correct_letter"]:
                    temp_dect.update({f'question{question_nbr}': 'Correct!'})
                    result += question["points"]
                else:
                    temp_dect.update({f'question{question_nbr}': f'Wrong!, the correct answer is {question["correct_answer"]}'})
                question_nbr += 1
            console.print("[bold magenta]Exam finished![/bold magenta]")
    return result


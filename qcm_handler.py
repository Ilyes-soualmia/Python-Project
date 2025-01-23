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
    temp_array = [] #to store the subjects and not printing them more once
    for exam in data["exams"]:
        if exam["subject"] not in temp_array:
            temp_array.append(exam["subject"])
            console.print(f"[bold magenta] | {exam["subject"]} [/bold magenta]")
    while True:
        subject = Prompt.ask("[bold cyan]Choose a subject: [/bold cyan] ")
        while True:
            for exam in data["exams"]:
                if subject.lower() == exam["subject"].lower():
                    return exam["subject"]
            console.print("[red]Invalid choice. Please enter a valid subject.[/red]")

# show choosed subject function
def show_exam_titles(data, subject):
    console.print(f"[bold cyan]Here are the available exams in {subject} : [/bold cyan]")
    for exam in data["exams"]:
        if exam["subject"] == subject: 
            console.print(f"[bold magenta] | {exam["name"]} [/bold magenta]")
    exam_name = Prompt.ask("[bold cyan]Choose an exam: [/bold cyan] ")
    while True:
        for exam in data["exams"]:
            if exam["name"].lower() == exam_name.lower() and exam["subject"] == subject:
                return exam["name"]
        console.print("[red]Invalid choice. Please enter a valid exam.[/red]")

# show choosed exam function
def show_exam(data, subject , exam_name):
    result = 0
    console.print(f"[bold cyan]You have choosen the subject: [/bold cyan][bold magenta]{subject[0].upper()}{subject[1:].lower()}[/bold magenta]")
    console.print(f"[bold cyan]You have choosen the exam: [/bold cyan][bold magenta]{exam_name}[/bold magenta]")
    console.print("[bold cyan]Here are the questions: [/bold cyan]")

    for exam in data["exams"]:
        if exam["subject"] == subject and exam["name"] == exam_name:
            if exam["total_points"] == 0:
                cndtn = True                #if it's 0 then we calculate the total points of the exam
            question_nbr = 1
            for question in exam["questions"]:
                console.print(f"[bold cyan in white]{question_nbr} / {question["question"]}: [/bold cyan in white]")
                console.print(f"[bold magenta]a) {question["options"][0]}[/bold magenta]")
                console.print(f"[bold magenta]b) {question["options"][1]}[/bold magenta]")
                console.print(f"[bold magenta]c) {question["options"][2]}[/bold magenta]")
                console.print(f"[bold magenta]d) {question["options"][3]}[/bold magenta]")
                if question["hint"] != "no-hint":
                    console.print(f"[bold yellow]✨Hint: {question["hint"]}[/bold yellow]")
                if cndtn:
                    exam["total_points"] += question["points"]   #add the points of the question to the total points of the exam
                print("\n")
                while True:
                    answer = Prompt.ask("[bold cyan]Your answer(a,b,c or d) =>: [/bold cyan] ")
                    if answer.lower() in ["a", "b", "c", "d"]:
                        break
                    else:
                        console.print("[red]Invalid choice. Please try again.[/red]")

                if answer.lower() == question["correct_letter"]:
                    temp_dect.update({f'question{question_nbr}': 'Correct!'})
                    result += question["points"]
                else:
                    temp_dect.update({f'question{question_nbr}': f'Wrong!, the correct answer is {question["correct_answer"]}'})
                question_nbr += 1
            console.print("[bold magenta]Exam finished![/bold magenta]")
        
            result / exam["total_points"] * 20    
    return result


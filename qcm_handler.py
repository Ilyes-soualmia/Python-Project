import json 

temp_dect = {'question1':'','question2':'','question3':'','question4':'','question5':'','question6':'','question7':'','question8':'','question9':'','question10':''}

# Load the data from the json file
def load_data():
    with open("QCM.json", "r") as f:
        data = json.loads(f.read())
        return data

# Welcome function
def welcome():
    print("Welcome to the quiz game!")
    name = input("Please enter your name: ")
    return name
# choose subject function
def choose_subject():
    subject = input("Choose a subject: ")
    return subject

# show choosed subject function
def choose_exam(data, subject):
    print("You have choosen the subject: ", subject)
    print("Here are the available exams in the choosen subject: ")
    for exam in data["exams"]:
        if exam["subject"] == subject:
            print(exam["name"])
    print("***************")
    exam_name = input("Choose an exam: ")
    return exam_name
result = 0
# show choosed exam function
def show_exam(data, subject , exam_name , result = 0):
    print("You have choosen the subject: ", subject)
    print("You have choosen the exam: ", exam_name)
    print("Here are the questions: ")
    for exam in data["exams"]:
        if exam["subject"] == subject and exam["name"] == exam_name:
            question_nbr = 1
            for question in exam["questions"]:
                print(question["question"])
                print("a) ", question["options"][0])
                print("b) ", question["options"][1])
                print("c) ", question["options"][2])
                print("d) ", question["options"][3])
                # print("Answer: ", question["answer"])
                answer = input("Your answer(a,b,c or d): ")
                if answer == question["correct_letter"]:
                    temp_dect.update({f'question{question_nbr}': 'Correct!'})
                    result += question["points"]
                else:
                    temp_dect.update({f'question{question_nbr}': f'Wrong!, the correct answer is {question["correct_answer"]}'})
                question_nbr += 1
            print("***************")
    return result


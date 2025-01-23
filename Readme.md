# ENG3 CYBER SECURITY PYTHON PROJECT.

## Project description:
This project is buildt to serve QCM exams for students, it's a simple console application that allows the user to take an exam and get the results, it shows also the wrong answers and their correct answer,  for sure there is a lot of exams and modules that the user can choose from, also the user 
The project is built using Python and the data is stored in a JSON file





/* <ins>_this is a simple description, if you want more details check_</ins> [Project_Documentation](https://github.com/Ilyes-soualmia/Python-Project/blob/master/ProjectDescription.pdf) 

## Project features:
- User can take an exam:
    * User can choose from a variety of subjects.
    * Each subject has a set of exams.
    * Each exam has a 20 questions with 4 choices for each question , & only one correct answer. 
    * questions of different levels of difficulty (easy, medium, hard).
    * Difficult questions are worth more points than. easy questions , and they may show a hint to help the user.
    * At the end of the exam the user gets his score ( /20) and the wrong answered questions with the correct answers.
- User can see his exams history:
    * User can see the exams he took and the scores he got.
    * User can export his exams history to a json file in his computer.
    * User can receive his exams history by email.

## Project technologies:
- Python:
    * Important Libraries used:
        - smtplib -> to send emails.
        - json -> to read and write JSON files.
        - rich -> to make the console output more beautiful.
        - TKinter -> even it's Cli app i did used it for the downloading exams history option ,else simple users will suffer with paths.
- JSON -> to store the data & handle it(users,history & qcms).

- I used HTML & CSS to make a professional email template that does contain our contact for those who want to contact us.
- Talking more about Rich Library i implemented many features like Console,Prompt,.... to make the perfect CLI UI.

## Prerequities:
### 1. Python 3.8 or higher
### 2. Rich Library
```bash
    pip install rich
```
### 3. smtplib Library
```bash
    pip install secure-smtplib
```
//for the smtp you need to do some configurations
## How to run the project:

### 1.Clone the project:
```bash

    git clone https://github.com/Ilyes-soualmia/Python-Project.git

    cd Python-Project

```

### 2.Run main:
```bash
    python main.py

```
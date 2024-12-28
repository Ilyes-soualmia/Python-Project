import json
import qcm_handler as qcm

# Main function

data = qcm.load_data()
name = qcm.welcome()
subject = qcm.choose_subject()
exam_name = qcm.choose_exam(data, subject)
result = qcm.show_exam(data, subject, exam_name)

#print result and correct answers
print(f"Your result is: {result} / 10")
for key, value in qcm.temp_dect.items():
    print(f'{key}: {value}')
   
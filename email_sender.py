import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import json

# Setup port number and server name
smtp_port = 587                 # i used 578 cuz it's the standard secure SMTP port
smtp_server = "smtp.gmail.com" 

# Set up the email lists
email_from = "techtitans1594@gmail.com"


pswd = "phyjmhjvjfedvope"


# name the email subject
subject = "Quizzy - Your Quiz history"

def send_email(username , jsonfile):

    email_to = input("Enter the email address you want to send the email to: ")

    # Body of the email
    body = f"""
    Hello, {username}!
    this is your quiz history
    attached in a json file
    thanks for using our service
    """

    # make a MIME object to define parts of the email
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    # Attach the body of the message
    msg.attach(MIMEText(body, 'plain'))
    # turn the data into a json file
    with open("file.json", "w") as file:
        json.dump(jsonfile, file, indent=4)
    filename = "file.json"
    attachment= open(filename, 'rb')

    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(attachment_package)
    # Cast as string
    text = msg.as_string()
    # Connect with the server
    print("Connecting to server...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_from, pswd)
    print("Succesfully connected to server")
    print()
    print(f"Sending email to: {email_to}...")
    server.sendmail(email_from, email_to, text)
    print(f"Email sent to: {email_to}")
    print()
    # Close the port
    server.quit()

# Usage example 
#send_email("ilyes", "file1.json")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from rich.console import Console
from time import sleep
import json
import personal_data_email as pde

# Setup port number and server name
smtp_port = 587                 # i used 578 cuz it's the standard secure SMTP port
smtp_server = "smtp.gmail.com" 

# Set up the email lists
email_from = pde.email_from

pswd = pde.pswd


# name the email subject
subject = "Quizzy - Your Quiz history"

def send_email(username , jsonfile , email_to):

    #email_to = input("Enter the email address you want to send the email to: ")

    # Body of the email
    body = f"""
                <!--
                * This email was built using Tabular.
                * For more information, visit https://tabular.email
                -->
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
                <head>
                <title></title>
                <meta charset="UTF-8" />
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <!--[if !mso]>-->
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <!--<![endif]-->
                <meta name="x-apple-disable-message-reformatting" content="" />
                <meta content="target-densitydpi=device-dpi" name="viewport" />
                <meta content="true" name="HandheldFriendly" />
                <meta content="width=device-width" name="viewport" />
                <meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
                <style type="text/css">
                table {{
                border-collapse: separate;
                table-layout: fixed;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt
                }}
                table td {{
                border-collapse: collapse
                }}
                .ExternalClass {{
                width: 100%
                }}
                .ExternalClass,
                .ExternalClass p,
                .ExternalClass span,
                .ExternalClass font,
                .ExternalClass td,
                .ExternalClass div {{
                line-height: 100%
                }}
                body, a, li, p, h1, h2, h3 {{
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%;
                }}
                html {{
                -webkit-text-size-adjust: none !important
                }}
                body, #innerTable {{
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale
                }}
                #innerTable img+div {{
                display: none;
                display: none !important
                }}
                img {{
                Margin: 0;
                padding: 0;
                -ms-interpolation-mode: bicubic
                }}
                h1, h2, h3, p, a {{
                line-height: inherit;
                overflow-wrap: normal;
                white-space: normal;
                word-break: break-word
                }}
                a {{
                text-decoration: none
                }}
                h1, h2, h3, p {{
                min-width: 100%!important;
                width: 100%!important;
                max-width: 100%!important;
                display: inline-block!important;
                border: 0;
                padding: 0;
                margin: 0
                }}
                a[x-apple-data-detectors] {{
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important
                }}
                u + #body a {{
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
                }}
                a[href^="mailto"],
                a[href^="tel"],
                a[href^="sms"] {{
                color: inherit;
                text-decoration: none
                }}
                </style>
                <style type="text/css">
                @media (min-width: 481px) {{
                .hd {{ display: none!important }}
                }}
                </style>
                <style type="text/css">
                @media (max-width: 480px) {{
                .hm {{ display: none!important }}
                }}
                </style>
                <style type="text/css">
                @media (max-width: 480px) {{
                .t3,.t54{{width:480px!important}}.t48,.t52{{padding:40px 30px!important}}.t50{{background-color:#f7f7f7!important;width:420px!important}}.t6{{padding-bottom:20px!important}}.t14,.t19,.t25,.t31,.t41,.t46,.t8{{width:360px!important}}.t5{{line-height:28px!important;font-size:26px!important;letter-spacing:-1.04px!important;color:#1a1a1a!important}}.t33{{color:#f7f7f7!important}}.t11,.t16{{color:#1a1a1a!important}}
                }}
                </style>
                <!--[if !mso]>-->
                <link href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@500;800&amp;display=swap" rel="stylesheet" type="text/css" />
                <!--<![endif]-->
                <!--[if mso]>
                <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
                </xml>
                <![endif]-->
                </head>
                <body id="body" class="t58" style="min-width:100%;Margin:0px;padding:0px;background-color:#242424;"><div class="t57" style="background-color:#242424;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t56" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#242424;" valign="top" align="center">
                <!--[if mso]>
                <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
                <v:fill color="#242424"/>
                </v:background>
                <![endif]-->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td align="center">
                <table class="t4" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="502" class="t3" style="width:502px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t3" style="width:502px;">
                <!--<![endif]-->
                <table class="t2" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t1"><div style="font-size:0px;"><img class="t0" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="502" height="344.875" alt="" src="https://b719d855-dc5f-4e56-bfb7-272910d42d2d.b-cdn.net/e/8fbae572-0a90-4086-bb5f-8b35cebf2a53/8d5ed31d-853e-4243-bd17-109f3ad4ef01.jpeg"/></div></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t55" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="600" class="t54" style="width:600px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t54" style="width:600px;">
                <!--<![endif]-->
                <table class="t53" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t52" style="padding:14px 50px 48px 50px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td align="center">
                <table class="t51" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="500" class="t50" style="background-color:#F8F8F8;width:500px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t50" style="background-color:#F8F8F8;width:500px;">
                <!--<![endif]-->
                <table class="t49" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t48" style="padding:96px 50px 60px 50px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td align="center">
                <table class="t9" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t8" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t8" style="width:400px;">
                <!--<![endif]-->
                <table class="t7" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t6" style="padding:0 0 25px 0;"><h1 class="t5" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:41px;font-weight:800;font-style:normal;font-size:39px;text-decoration:none;text-transform:none;letter-spacing:-1.56px;direction:ltr;color:#191919;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">Quizzy app 🤖</h1></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="left">
                <table class="t15" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t14" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t14" style="width:400px;">
                <!--<![endif]-->
                <table class="t13" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t12" style="padding:0 0 6px 0;"><h1 class="t11" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:16px;font-weight:800;font-style:normal;font-size:25px;text-decoration:none;text-transform:uppercase;letter-spacing:3px;direction:ltr;color:#191919;text-align:center;mso-line-height-rule:exactly;mso-text-raise:-3px;">HI, <span class="t10" style="margin:0;Margin:0;color:#00FF9D;mso-line-height-rule:exactly;"> {username} </span>👋</h1></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="left">
                <table class="t20" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t19" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t19" style="width:400px;">
                <!--<![endif]-->
                <table class="t18" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t17" style="padding:0 0 6px 0;"><h1 class="t16" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:16px;font-weight:800;font-style:normal;font-size:25px;text-decoration:none;text-transform:uppercase;letter-spacing:3px;direction:ltr;color:#191919;text-align:center;mso-line-height-rule:exactly;mso-text-raise:-3px;"></h1></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t26" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t25" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t25" style="width:400px;">
                <!--<![endif]-->
                <table class="t24" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t23" style="padding:0 0 22px 0;"><p class="t22" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">This is your quiz 📝 history attached in a JSON file. <br/><span class="t21" style="margin:0;Margin:0;mso-line-height-rule:exactly;">Thanks for using Quizzy.</span></p></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t32" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t31" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t31" style="width:400px;">
                <!--<![endif]-->
                <table class="t30" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t29" style="padding:0 0 22px 0;"><p class="t28" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;"><span class="t27" style="margin:0;Margin:0;mso-line-height-rule:exactly;"></span></p></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t37" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="250" class="t36" style="background-color:#171717;overflow:hidden;width:250px;border-radius:44px 44px 44px 44px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t36" style="background-color:#171717;overflow:hidden;width:250px;border-radius:44px 44px 44px 44px;">
                <!--<![endif]-->
                <table class="t35" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t34" style="text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;"><a class="t33" href="mailto:techtitans1594@gmail.com" style="display:block;margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:44px;font-weight:800;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;letter-spacing:2.4px;direction:ltr;color:#F8F8F8;text-align:center;mso-line-height-rule:exactly;mso-text-raise:10px;" target="_blank">Contact us</a></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t42" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t41" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t41" style="width:400px;">
                <!--<![endif]-->
                <table class="t40" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t39"><p class="t38" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#888888;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;"></p></td></tr></table>
                </td></tr></table>
                </td></tr><tr><td align="center">
                <table class="t47" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr>
                <!--[if mso]>
                <td width="400" class="t46" style="width:400px;">
                <![endif]-->
                <!--[if !mso]>-->
                <td class="t46" style="width:400px;">
                <!--<![endif]-->
                <table class="t45" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t44"><p class="t43" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#888888;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">ALL RIGHTS RESERVED FOR ILYES SLM</p></td></tr></table>
                </td></tr></table>
                </td></tr></table></td></tr></table>
                </td></tr></table>
                </td></tr></table></td></tr></table>
                </td></tr></table>
                </td></tr></table></td></tr></table></div><div class="gmail-fix" style="display: none; white-space: nowrap; font: 15px courier; line-height: 0;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div></body>
                </html>
            """

    console = Console()
    # make a MIME object to define parts of the email
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    # Attach the body of the message
    msg.attach(MIMEText(body, 'html'))
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
    with console.status("[bold green]Connecting to server...") as status:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_from, pswd)
    console.print("[bold green]Succesfully connected to server[/bold green]")
    print()
    with console.status(f"[bold green]Sending email to: {email_to}...") as status:
        server.sendmail(email_from, email_to, text)
        sleep(1.5)
    console.print(f"[bold green]Email sent to: {email_to}[/bold green]")
    print()
    # Close the port
    server.quit()

# Usage example 
#send_email(username, "file1.json")

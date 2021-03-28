import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # command send by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.starttls()
    server.ehlo()

    server.login('<usser@mail.com>', 'password')

    subject = 'Enter subject here'
    body = 'Enter the text of the email here'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('from-mail', 'to-mail', msg)
    print('-email has been send-')
    server.quit()

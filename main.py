import smtplib
from getpass import getpass


def login(email, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
        server.starttls()  # Use TLS
        server.login(email, password)  # Login to the email server
        return server
    except smtplib.SMTPException:
        print('login error')
        exit()


def send_email(recipient, num_emails_to_send, email, server):
    while num_emails_to_send != 0:
        try:
            message = 'Subject: {}\n\n{}'.format("Hello from Python part {}".format(num_emails_to_send),
                                                 "I wrote this app to destroy you, this is the {}th email".format(
                                                     num_emails_to_send))
            server.sendmail(email, recipient, message)  # Send the email
            print('Success: Sent to {}'.format(recipient))
        except smtplib.SMTPException:
            print("Error: Unable to send email")
        num_emails_to_send = num_emails_to_send - 1


if __name__ == '__main__':
    run_again = True
    username = input("Username: ")
    pword = getpass()
    while run_again:
        send_to = input("Who do you want to email: ")
        if '@' not in send_to:
            print("Invalid address!")
            exit()
        num_emails = int(input("How many times do you want to email: "))
        if num_emails > 4:
            print("That's too many emails!")
            exit()
        print("================================================" + "\n")
        email_server = login(username, pword)
        send_email(send_to, num_emails, username, email_server)
        again = input("Want to send more emails? (y,n): ")
        if again != 'y':
            run_again = False
    email_server.quit()  # Logout of the email server

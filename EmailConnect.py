# ###############################################################################

# from email.mime.text import MIMEText
# import smtplib

# ###############################################################################

# class Email:
#     def __init__(self, port, smtp_server, sender_email, receiver_email, sender_email_password):
#         # Email settings
#         self.port = port
#         self.smtp_server = smtp_server
#         self.sender_email = sender_email
#         self.receiver_email = receiver_email
#         self.password = sender_email_password

#     def send_email(self, subject, my_message):
#         message = MIMEText(str(my_message))
#         message['Subject'] = subject
#         message['From'] = self.sender_email
#         message['To'] = ', '.join(self.receiver_email)
#         my_server = smtplib.SMTP_SSL(self.smtp_server, self.port)
#         my_server.login(self.sender_email, self.password)
#         my_server.sendmail(self.sender_email,
#                            self.receiver_email, message.as_string())
#         my_server.quit()

# ###############################################################################

# # Email Accounts:
# EMAIL_ACCOUNT = Email(port=465, smtp_server='smtp.gmail.com', sender_email='sender email', receiver_email=[list of reciver], sender_email_password='********')

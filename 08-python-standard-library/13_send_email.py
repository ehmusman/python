from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib

message = MIMEMultipart()

message["from"] = "Usman Test"
message["to"] = "ehmusman@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))


with smtplib.SMTP(host="", port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("", "")
    smtp.send_message(message)
    print("Sent...")
import smtplib
from email.mime.text import MIMEText

body = "Test Message"
msg = MIMEText(body)

msg['From'] = "leafs3598@gmail.com"
msg['To'] = "leafs3598@gmail.com"
msg['Subject'] = "WAAASSUP"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("leafs3598@gmail.com", "Rachana11")

server.send_message(msg)

print("Message sent")

server.quit()


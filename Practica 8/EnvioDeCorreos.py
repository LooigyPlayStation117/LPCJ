import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


#a="Envio de correos"
parser = argparse.ArgumentParser(description="Hi", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-rmt', type=str , help='Correo del remitente.')
parser.add_argument('-to', type=str , help='Correo del destinatario')
parser.add_argument('-pwd', type=str , help='Contraseña del remitente')
parser.add_argument('-msg', type=str, help='Mensaje dentro del correo')
parser.add_argument('-sub', type=str, help='Asunto del correo')

params = parser.parse_args()
email_msg = MIMEMultipart("alternative")
de = (params.rmt)
email_msg["From"] = de
to = (params.to)
email_msg["To"] = to
sub = (params.sub)
email_msg["Subject"] = sub
pwd = (params.pwd)
message = params.msg
email_msg.attach(MIMEText(message, "plain"))


server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
server.login(de, pwd)
server.sendmail(email_msg["From"], to, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))





























































#!/usr/bin/env python3
#este es el script llamado send_email modificado para uso personal

# Bibliotecas necessárias
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# Criar objeto que enviará
msg = MIMEMultipart()
 
 
message = "E-mail que eu tentei enviar"
 
# Parametros
senha = "rwmsdgxcivqqiypl"
msg['From'] = "viny6888@gmail.com"
msg['To'] = "viniciusgcaetano@hotmail.com"
msg['Subject'] = "EMAIL ENVIADO COM SUCESSO"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#Criar sessão
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Realizar login
server.login(msg['From'], senha)
 
 
# Enviar mensagem.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 

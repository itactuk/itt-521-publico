import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

LISTA_CONTACTOS = "C:\\Users\\Ivan's PC\\Documents\\tmp\\contactos.txt"
ARCHIVO_PLANTILLA = "C:\\Users\\Ivan's PC\\Documents\\tmp\\plantilla.txt"

MI_CORREO = 'pruenaitt521@gmail.com'
PASSWORD = 'estaesmicontrasena0!'

MTA_HOST = 'smtp.gmail.com'
MTA_PORT = 587 # SSL: 465, TLS: 587

def lee_contactos(filename):
    """
    Returna dos listas nombres, correos que contiene
    nombres y direcciones de correos electrónicos
    leídos del archivo filename
    """
    
    nombres = []
    correos = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            nombres.append(a_contact.split()[0])
            correos.append(a_contact.split()[1])
    return nombres, correos

def lee_plantilla(filename):
    """
    Returna un objeto Template que encapsula el contenido de filename
    """
    
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return Template(contenido)

def main():
    nombres, correos = lee_contactos(LISTA_CONTACTOS)
    message_template = lee_plantilla(ARCHIVO_PLANTILLA)

    # crea sesión SMTP
    s = smtplib.SMTP(host=MTA_HOST, port=MTA_PORT)
    s.starttls()
    s.set_debuglevel(1) # esto se debería de remover en un ambiente real
    s.login(MI_CORREO, PASSWORD)

    # Para cada contacto, envía correo:
    for nombre, correo in zip(nombres, correos):
        msj = MIMEMultipart()       # create a message

        # agrega el nombre de la persona en el mensaje de la plantilla
        mensaje = message_template.substitute(NOMBRE_PERSONA=nombre.title())

        # Imprime el mensaje
        # print(mensaje)

        # asigna parámetros al correo
        msj['From']=MI_CORREO
        msj['To']=correo
        msj['Subject']="Esto es una prueba"
        
        # agrega mensaje al cuerpo del correo
        msj.attach(MIMEText(mensaje, 'plain'))
        
        # envía mensaje usando sesión creada anteriormente
        s.send_message(msj)
        del msj
        
    # Termina la sesión SMTP y cierra la conexión
    s.quit()
    
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import poplib

GOOGLE_POP3_SERVER = 'pop.googlemail.com'
POP3_SERVER_PORT = '995'

MI_CORREO = 'pruenaitt521@gmail.com'
PASSWORD = 'estaesmicontrasena0!'

def fetch_email(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, POP3_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    num_messages = len(mailbox.list()[1])
    print("Total emails: {0}".format(num_messages))
    print("Getting last message")
    for msg in mailbox.retr(num_messages)[1]:
        print(msg)
    mailbox.quit()

if __name__ == '__main__':
    username = MI_CORREO
    password = PASSWORD
    fetch_email(username, password)

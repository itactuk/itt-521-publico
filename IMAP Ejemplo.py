#!/usr/bin/env python3
import imaplib
import pprint

GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT = '993'

MI_CORREO = 'pruenaitt521@gmail.com'
PASSWORD = 'estaesmicontrasena0!'

def check_email(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select('Inbox')
    tmp, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        tmp, data = mailbox.fetch(num, '(RFC822)')
        print('Message: {0}\n'.format(num))
        pprint.pprint(data[0][1])
        break
    mailbox.close()
    mailbox.logout()


if __name__ == '__main__':
    username = MI_CORREO
    password = PASSWORD
    check_email(username, password)

# from ftplib import FTP
#
# ftp = FTP('192.168.77.23')
#
# ftp.login('root', '20091665')

import pysftp

with pysftp.Connection('192.168.77.23', username='root', password='20091665') as sftp:
    with sftp.cd('holaThu_sFeb_s28_s12:14:41_s2019'):             # cambiar de directorio temporalmente
        print(sftp.listdir())
        print(sftp.pwd) # retorna directorio en el que se está trabajando actualmente
        sftp.put("C:\\Users\\Ivan's PC\\Documents\\tmp\\firstkeypair.pem")  # cargar archivo
        sftp.get('firstkeypair.pem', "C:\\Users\\Ivan's PC\\Documents\\firstkeypair.pem")         # descargar archivo


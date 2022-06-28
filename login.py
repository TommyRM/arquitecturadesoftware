import socket
import sys
import psycopg2
connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="nicobolton",
    host="arquidatabase.cmd1vp7e8zfb.us-east-1.rds.amazonaws.com",
    port='5432'
)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))

#sock.bind(server_address)
sock.connect(server_address)
message = b'00005sinitlogin'
print('sending {!r}'.format(message))
sock.send(message)

#sock.bind(server_address)

# Listen for incoming connections

while True:
    recibido=sock.recv(1024)
    if recibido:
        #print(recibido.decode().split(' '))
        if len(recibido.decode().split(' '))==3:
            correo=recibido.decode().split(' ')[1]
            clave=recibido.decode().split(' ')[2]
            cursor = connection.cursor()
            postgreSQL_select_Query = f"select * from usuario where email = '{correo}' and pass = '{clave}'"

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            if len(mobile_records)==1:
                mensaje=f'00015login logeado {mobile_records[0][4]}'.encode()
                sock.send(mensaje)
            else:
                sock.send(b'00022login datos no validos')


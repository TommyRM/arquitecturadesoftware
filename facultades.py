import socket
import sys
import psycopg2
import pickle
connection = psycopg2.connect(
     database="postgres",
     user="postgres",
     password="nicobolton",
     host="arquidatabase.cmd1vp7e8zfb.us-east-1.rds.amazonaws.com",
     port='5432'
 )
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))

#sock.bind(server_address)
sock.connect(server_address)
message = b'00005sinitfacul'
print('sending {!r}'.format(message))
sock.send(message)

#sock.bind(server_address)

# Listen for incoming connections

while True:
    recibido=sock.recv(4096)
    if recibido:
        print(recibido.decode().split(' '))
        if len(recibido.decode().split(' '))==2:
            #correo=recibido.decode().split(' ')[1]
            #clave=recibido.decode().split(' ')[2]
            cursor = connection.cursor()
            postgreSQL_select_Query = f"select * from facultad"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            print(mobile_records)
            largo=len(mobile_records)+5+1
            mensaje=f'00177facul {mobile_records}'.encode()
            sock.send(mensaje)

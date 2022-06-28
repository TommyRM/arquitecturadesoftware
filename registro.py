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
message = b'00005sinitregis'
print('sending {!r}'.format(message))
sock.send(message)

#sock.bind(server_address)

# Listen for incoming connections

while True:
    recibido=sock.recv(1024)
    if recibido:
        print(recibido.decode().split(' '))
        if len(recibido.decode().split(' '))==3:
            correo=recibido.decode().split(' ')[1]
            clave=recibido.decode().split(' ')[2]
            cursor = connection.cursor()
            postgreSQL_select_Query = f"select * from usuario where email = '{correo}'"

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            print(mobile_records)
            if len(mobile_records)>0:
                 sock.send(b'00026regis Correo ya registrado')
            else:
                try:
                     postgreSQL_select_Query = f"INSERT INTO USUARIO (EMAIL, PASS, ID_FACULTAD, ROL) VALUES ('{correo}', '{clave}',1,0)" #0 usuario normal  1 usuario admin 2 usuario soporte
                     cursor.execute(postgreSQL_select_Query)
                     commit=connection.commit()
                     print(commit)
                     sock.send(b'00022regis registro exitoso')
                except:
                     print("error")






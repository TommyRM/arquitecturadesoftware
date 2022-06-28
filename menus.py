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

#Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))

#sock.bind(server_address)
sock.connect(server_address)
message = b'00005sinitmenus'
print('sending {!r}'.format(message))
sock.send(message)

#sock.bind(server_address)

# Listen for incoming connections

while True:
    recibido=sock.recv(4096)
    if recibido:
        #print(recibido.decode().split(' '))
        if len(recibido.decode().split(' '))==2:
            #correo=recibido.decode().split(' ')[1]
            #clave=recibido.decode().split(' ')[2]
            cursor = connection.cursor()
            postgreSQL_select_Query = f"select id_menu,nombre,descripcion from menu where id_facultad = '{recibido.decode().split(' ')[1]}'"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            #print(mobile_records)
            largo=len(str(mobile_records))+5+1
            if largo >999:
                 largo=str(largo)
                 mensaje=f'0{largo}menus {mobile_records}'.encode()
            elif largo>99:
                 largo=str(largo)
                 mensaje=f'00{largo}menus {mobile_records}'.encode()
            else:
                mensaje=f'000{largo}menus {mobile_records}'.encode()
            #largo=str(largo)
            #mensaje=f'00{largo}menus {mobile_records}'.encode()
            sock.send(mensaje)

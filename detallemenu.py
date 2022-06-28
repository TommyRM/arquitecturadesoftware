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
message = b'00005sinitdetal'
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
            postgreSQL_select_Query = f"SELECT MENU.ID_MENU, MENU.NOMBRE, MENU.DESCRIPCION FROM MENU WHERE  ID_MENU = '{recibido.decode().split(' ')[1]}'"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()

            postgreSQL_select_Query = f"SELECT * FROM resenia  WHERE  ID_MENU = '{recibido.decode().split(' ')[1]}'"
            cursor.execute(postgreSQL_select_Query)
            resenas=cursor.fetchall()
            lista=[mobile_records,resenas]
            print(lista)
            #print(mobile_records)
            largo=len(str(lista))+5+1
            #print(largo)
            if largo >999:
                 largo=str(largo)
                 mensaje=f'0{largo}detal {lista}'.encode()
            elif largo>99:
                largo=str(largo)
                mensaje=f'00{largo}detal {lista}'.encode()
            else:
                largo=str(largo)
                mensaje=f'000{largo}detal {lista}'.encode()
            #mensaje=f'00074detal {mobile_records}'.encode()
            sock.send(mensaje)

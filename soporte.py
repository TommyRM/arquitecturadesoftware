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
message = b'00005sinitsopor'
print('sending {!r}'.format(message))
sock.send(message)

#sock.bind(server_address)

# Listen for incoming connections

while True:
    recibido=sock.recv(1024)
    if recibido:
        print(recibido.decode().split(' '))
        if len(recibido.decode().split(' '))>=3:
            try:
                #print("sfjinsafsjnnsfajafsjkjk")
                print(recibido.decode().split(' ')[1])
                cursor = connection.cursor()
                postgreSQL_select_Query = f"INSERT INTO SOPORTE (CORREO,COMENTARIO) VALUES ('{recibido.decode().split(' ',2)[1]}','{recibido.decode().split(' ',2)[2]}')"
                cursor.execute(postgreSQL_select_Query)
                commit=connection.commit()
                #print(commit)
                sock.send(b'00042sopor gracias por comunicarte con nosotros')
            except:
                sock.send(b'00019sopor hubo un error')






import socket
import sys
import pickle
mensaje=None
#tipousuario=None
def soporte(correo,comentario):
    #largo=len(correo)+len(clave)+7
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global  mensaje
    #global tipousuario
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    #print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        largo=5+1+1+len(correo)+len(comentario)
        if largo>999:
             message = f'0{largo}sopor {correo} {comentario}'.encode()
        elif largo>99:
             message = f'00{largo}sopor {correo} {comentario}'.encode()
        else:
            message = f'000{largo}sopor {correo} {comentario}'.encode()
        #print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #while amount_received < amount_expected:
        #print("hola mundo")
        data = sock.recv(4096).decode().split(' ')
        mensaje=''
        for i in range(len(data)):
            if i!=0:
                mensaje+=data[i]
                mensaje+=' '
        #datos=data.decode().split('[')[1].strip(']').split(',')
        print(mensaje)
        '''
        for i in range(len(datos)):
            if i==0:
                lista.append(datos[i][1])
            elif i%3==0:
                lista.append(datos[i][2])
            else:
                lista.append(datos[i])
        listaauxiliar=[]
        for elemento in lista:
            listaauxiliar.append(elemento.strip(')'))
        print(listaauxiliar)
        return(listaauxiliar)
        #pickle.loads(datos)

        #mensaje=data[1]
        #tipousuario=data[2]
        data=pickle.loads(data)
        amount_received += len(data)
        for tupla in data:
            print(f'{tupla[0]}. {tupla[1]}')
        #print(mensaje)
        #print(tipousuario)

        #break'''

    finally:
        #print('closing socket')
        sock.close()

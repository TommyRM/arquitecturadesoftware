import socket
import sys
import pickle
mensaje=None
#tipousuario=None
def vermenusfacultad(idfacultad):
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
        message = f'00007menus {idfacultad}'.encode()
        #print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #while amount_received < amount_expected:
        #print("hola mundo")
        data = sock.recv(4096).decode()
        #datos=data.decode().split('[')[1].strip(']').split(',')
        data=data.split('[',1)[1].strip(']').replace("(","").replace(")","").split(',')
        numero = len(data)
        cont = 0
        for i in data:
            if(cont+1<numero and cont+2<numero):
                print("Id menú: ",data[cont],".","--", "Nombre: ",data[cont+1],"--", "Descripción:", data[cont+2])
            cont=cont+3
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

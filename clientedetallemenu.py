import socket
import sys
import pickle
mensaje=None
#tipousuario=None
def verdetallemenu(idmenu):
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
        message = f'00007detal {idmenu}'.encode()
        #print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #while amount_received < amount_expected:
        #print("hola mundo")
        data = sock.recv(4096).decode()
        #datos=data.decode().split('[')[1].strip(']').split(',')
        data = data[12:]
        b = data.split("]")
        b[1] = b[1].split(")")
        characters = "'[]()"

        for i in range(len(characters)):
            b[0] = b[0].replace(characters[i],"")
            for j in range(len(b)):
                b[1][j] = b[1][j].replace(characters[i],"")

        b[0] = b[0].split(",")
        for i in range(len(b)):
            b[1][i] = b[1][i].split(",")


        print("-------------------------------------------------------------------------------------")
        print("nombre : " + b[0][1])
        print("Descripción :" + b[0][2])
        print("Reseñas :")
        for i in range(len(b[1])-2):
            print("    " + b[1][i][4] + "  --->  "+"Nota: "+b[1][i][2]+", " + b[1][i][3])

        print("-------------------------------------------------------------------------------------")


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

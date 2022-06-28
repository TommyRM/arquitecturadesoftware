import socket
import sys
mensaje=None
tipousuario=None
def login(correo,clave):
    largo=len(correo)+len(clave)+7
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global  mensaje
    global tipousuario
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    #print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        message = f'000{largo}login {correo} {clave}'.encode()
        #print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #while amount_received < amount_expected:
        data = sock.recv(1024).decode().split(' ')
        mensaje=data[1]
        tipousuario=data[2]
        amount_received += len(data)
        #print(mensaje)
        #print(tipousuario)
        if mensaje=='logeado':
            logeado=True
        else:
            logeado=False
        tupla=(logeado,tipousuario)
        #break

    finally:
        #print('closing socket')
        sock.close()
        return(tupla)

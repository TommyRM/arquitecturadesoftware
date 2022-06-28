import socket
import sys
numero=None
def registro(correo,clave):
    largo=len(correo)+len(clave)+7
    global numero
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    #print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try:

        # Send data
        message = f'000{largo}regis {correo} {clave}'.encode()
        #print('sending {!r}'.format(message))
        sock.sendall(message)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            #data=data.decode().split(' ')[1]
            mensaje=(data[13:]).decode()
            print(mensaje)
            break

    finally:
        #print('closing socket')
        sock.close()

import socket
import sys




#Direccion del Servidor IP y Puerto
ip ="13.85.31.211"
port = int("80")


# Creando el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociaciando el socket al puerto
server_address = (ip, port)
s.bind(server_address)


# Datos DB


# Sevidor esperando mensaje

while True:

    print("####### El servidor esta escuchando #######")
    data, address = s.recvfrom(4096)
    print(" IP Cliente: ",address)
    print(" Datos Recibidos: ", data.decode('utf-8'))

    
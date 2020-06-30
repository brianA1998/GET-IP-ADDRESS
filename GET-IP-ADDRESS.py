# importacion de modulo 
import socket 

# obtener nombre de maquina
hostname = socket.gethostname() 

# obtener direccion IP
IPAddr = socket.gethostbyname(hostname) 

# imprimir nombre del host
print("Your Computer Name is:" + hostname) 

# imprimir direccion IP
print("Your Computer IP Address is:" + IPAddr) 
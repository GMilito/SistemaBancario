
from operator import truediv
import socket
import json
import base64
import threading

from Datos import *
from Encryption import decrypt


# Función para recibir todos los datos del socket
def recvall(sock, tamaño):
    print("recvall")
    datos = b""
    while len(datos) < tamaño:
        fragmento = sock.recv(tamaño - len(datos))
        if not fragmento:
            raise IOError("Conexión cerrada inesperadamente por el cliente")
        datos += fragmento
    print(datos)
    return datos


        
def procesarTransaccion(tipo,jsonBytes,KEY,IV):
    print("procesarTransaccion")
    if tipo == 0:
        
        return procesarRetiro(jsonBytes,KEY,IV)
        
    if tipo == 1:
        #jsonConsulta = json.loads(jsonstr)
        pass
    if tipo == 2:
        #jsonCambio = json.loads(jsonstr)
        pass
def limpiarString(input_string):     
    # Filtrar caracteres no imprimibles y caracteres especiales 
    cleaned_string = ''.join(char for char in input_string if char.isprintable())
    return cleaned_string  

def validarTarjeta(nroTarjeta,Pin,FecVec):
    print("validarTarjeta")
    dict = verificarTarjetaDB(nroTarjeta)
    DBNroTarjeta = dict['numeroTarjeta']
    DBPin = dict['PIN']
    DBFecVec = dict['fechaVencimiento']
    print("fecha: ",dict['fechaVencimiento'])
    if DBNroTarjeta == nroTarjeta and DBPin == Pin and DBFecVec == FecVec:
        return True
    else:
        return False

def procesarRetiro(jsonBytes,KEY,IV):
    print("procesarRetiro")
    print("Bytes:",jsonBytes)
    jsonStr = jsonBytes.decode('utf-8')
    jsonRetiro = json.loads(jsonStr)
    print("String:",jsonStr)
    print("jsonRetiro:",jsonRetiro)
    print(jsonRetiro['NumeroTarjeta']) 
    print("Desencriptados:")
    
    NroTarjeta = decrypt(jsonRetiro['NumeroTarjeta'],KEY,IV)
    PINstr = decrypt(jsonRetiro['PIN'],KEY,IV)
    FecVec = decrypt(jsonRetiro['FechaVencimiento'],KEY,IV)
    
    NroTarjeta = NroTarjeta.decode('utf-8')
    PINstr = PINstr.decode('utf-8')     
    FecVec = FecVec.decode('utf-8')
    NroTarjeta = limpiarString(NroTarjeta)
    PINstr = limpiarString(PINstr)
    FecVec = limpiarString(FecVec)
    
    monto = jsonRetiro['MontoTransaccion']
    codigo = jsonRetiro['CodigoVerificacion']
    
    print("tarjeta ",NroTarjeta,"PIN ",PINstr, "fec" ,FecVec)
    
    validada = validarTarjeta(NroTarjeta,PINstr,FecVec)
    
    if validada:
        resp = verificarTipoTarjeta(NroTarjeta)
        tipoTarjeta = resp['tipoTarjeta']
        if tipoTarjeta == "credito":
            pass
        elif tipoTarjeta == 'debito':
            nroCuenta = getNroCuenta(NroTarjeta)
            trama = "0:"+nroCuenta+":"+monto+":"+NroTarjeta+":"+codigo
    else:
        return "Datos incorrectos"
        
    
    
def capturarClave(datos):
    print("capturarClave")
    key = None
    iv = None
    print(datos)
    # Asignar los primeros 32 bytes a una variable
    keyBytes = datos[:32]

    # Asignar los siguientes 16 bytes a otra variable
    ivBytes = datos[32:48]

    # Imprimir los resultados
    print("Primeros 32 bytes:", keyBytes)
    print("Siguientes 16 bytes:", ivBytes)
    keyB64 = base64.b64encode(keyBytes)
    ivB64 = base64.b64encode(ivBytes)
    print("KEY:", keyB64)
    print("IV:", ivB64)
    key = base64.b64decode(keyB64)
    iv = base64.b64decode(ivB64)
    print("Recibido Key y iv",key,iv)
    return key , iv    

def manejarCliente(client_socket, client_address):
    print("manejarCliente")
    print("Conexión entrante desde:", client_address)
    respuesta = None
    key = None
    iv = None
    # Procesar la conexión entrante
    
    try:
        trama1=[]
        # Recibir el primer mensaje de 71 bytes
        primer_mensaje = recvall(client_socket, 8).decode('UTF-8')
        
        trama1 = primer_mensaje.split(':')
        
        tamañoClave = int(trama1[1])
        tamañoJson = int(trama1[2])
        
     
        if trama1[0] == '0':
            segundo_mensaje = recvall(client_socket, tamañoClave)
            
            tercer_mensaje = recvall(client_socket, tamañoJson)
            print("Segundo mensaje: ",segundo_mensaje)
            print("Tercer mensaje: ",tercer_mensaje)
            key , iv =  capturarClave(segundo_mensaje)
            respuesta = procesarTransaccion(0,tercer_mensaje,key,iv)
        if trama1[0] == '1':
            segundo_mensaje = recvall(client_socket, tamañoClave)
            tercer_mensaje = recvall(client_socket, tamañoJson)
            key , iv =  capturarClave(segundo_mensaje)
            respuesta = procesarTransaccion(1,tercer_mensaje,key,iv)
        if trama1[0] == '2':
            segundo_mensaje = recvall(client_socket, tamañoClave)
            tercer_mensaje = recvall(client_socket, tamañoJson)
            key , iv =  capturarClave(segundo_mensaje)
            respuesta = procesarTransaccion(2,tercer_mensaje,key,iv)
        
        
        print("Primer mensaje recibido:", primer_mensaje)
        print("Segundo mensaje recibido:", segundo_mensaje)
        print("Tercer mensaje recibido:", tercer_mensaje)

    finally:
        pass
    
    # Ejemplo: enviar un mensaje de bienvenida al cliente
    client_socket.sendall(respuesta.encode())

    # Cerrar la conexión con el cliente
    client_socket.close()
            

# Definir el host y el puerto en el que escuchará el servidor
HOST = '127.0.0.1'  # El servidor escuchará en localhost
PORT = 8000        

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto especificados
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen(5)  # Permitir hasta 5 conexiones en cola

print("Servidor escuchando en {}:{}".format(HOST, PORT))

while True:
    client_threads = []
    # Aceptar una nueva conexión entrante
    client_socket, client_address = server_socket.accept()

    # Manejar la conexión entrante utilizando la función manejar_cliente
    client_thread = threading.Thread(target=manejarCliente, args=(client_socket, client_address))
    client_thread.start()
    client_threads.append(client_thread)
  

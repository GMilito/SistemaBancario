
from operator import truediv
import socket
import json
import base64
import threading

from datetime import datetime
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

def registrarBitacora():
    with open("bitacora.json", mode='w', encoding='utf-8') as f:
        json.dump([], f)
        
def procesarTransaccion(tipo,jsonBytes,KEY,IV):
    print("procesarTransaccion")
    if tipo == 0:
        respuesta = procesarRetiro(jsonBytes,KEY,IV)
        print("Respuesta de Java: ",respuesta)
        return respuesta
        
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

    # Obtener el formato "MM/YY"
    fechaFormateada = DBFecVec.strftime("%m/%y")
    print("Tarjetas")
    print(DBNroTarjeta == nroTarjeta)
    print("pines")
    print(int(DBPin) == int(Pin))
    print(DBPin)
    print(Pin)
    print("fechas")
    print(fechaFormateada == FecVec)
    
    if DBNroTarjeta == nroTarjeta and int(DBPin) == int(Pin) and fechaFormateada == FecVec:
        return True
    else:
        return False
    
def validarEstadoTarjeta(nroTarjeta):
    print("validarEstadoTarjeta")
    dict = verificarEstadoTarjetaDB(nroTarjeta)
    estadoTarjeta = dict['estadoTarjeta']
    
    if estadoTarjeta == "activa":
        return True
    else:
        return False
    
def validarCajero(idCajero):
    print("validarCajero")
    dict = verificarCajero(idCajero)
    print(dict)
    if dict is None:
        return False
    idCajeroDB = dict['idCajero']
    print("id cajero")
    print(idCajero)
    
    print("id cajero DB")
    print(idCajeroDB)
    
    print("Validacion")
    print(idCajero == idCajeroDB)
    
    if int(idCajero) == idCajeroDB:
        return True
    else:
        return False
    
def validarFechaTarjeta(nroTarjeta):
    print("validarFechaTarjeta")
    dict = verificarFechaTarjetaDB(nroTarjeta)
    print(dict)
    fechaVencimiento = dict['fechaVencimiento']
    print(fechaVencimiento)
    fecha_actual = datetime.now().date()
    print("Fecha Validacion")
    print(fecha_actual , fechaVencimiento)
    print(fecha_actual < fechaVencimiento)
    print(fechaVencimiento , fecha_actual)
    print(fechaVencimiento < fecha_actual)
    if fechaVencimiento > fecha_actual:
        return True
    else:
        return False
    
def enviarCore(host, port, mensaje):
    print("enviarCore")
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar el socket al servidor
        sock.connect((host, port))
        
        # Enviar el mensaje al servidor
        sock.sendall(mensaje.encode())
        
        # Esperar la respuesta del servidor
        respuesta = sock.recv(5)
        
        # Imprimir la respuesta del servidor
        print("Respuesta del servidor:", respuesta.decode())
        return respuesta.decode()
    finally:
        # Cerrar el socket
        sock.close()

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
    idCajero = jsonRetiro['IdentificacionCajero']
    
    print("tarjeta ",NroTarjeta,"PIN ",PINstr, "fec" ,FecVec)
    
    validada = validarTarjeta(NroTarjeta,PINstr,FecVec)
    activa = validarEstadoTarjeta(NroTarjeta)
    alDia = validarFechaTarjeta(NroTarjeta)
    cajeroValido = validarCajero(idCajero) 
    print("Validacion")
    print(validada)
    if (cajeroValido):
        if validada:
            print("Validada")
            if activa:
                if alDia:
                    print("alDia")
                    resp = verificarTipoTarjeta(NroTarjeta)
                    tipoTarjeta = resp['tipoTarjeta']
                    if tipoTarjeta == "credito":
                        
                        
                        
                        #CREDITO
                        
                        
                        
                        resp = getNroCuenta(NroTarjeta)
                        print(resp)
                        nroCuenta = resp['numeroCuenta']
                        print(nroCuenta)
                        montoDisponible = consultarSaldo(NroTarjeta)
                        
                        
                        if monto <= montoDisponible:
                            data = {
                                "status": "OK",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                        elif monto > montoDisponible:
                            data = {
                                "status": "1: Fondos insuficientes",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                        elif montoDisponible is None:
                            data = {
                                "status": "5: Error no controlado.",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                    elif tipoTarjeta == 'debito':
                        
                        
                        
                    
                        #DEBITO
                        
                        
                        
                        resp = getNroCuenta(NroTarjeta)
                        print(resp)
                        nroCuenta = resp['numeroCuenta']
                        print(nroCuenta)
                        trama = "0:"+nroCuenta+":"+monto+":"+NroTarjeta+":"+codigo
                        respuesta = enviarCore('localhost',8080,trama)
                        if respuesta == "OK???":
                            data = {
                                "status": "OK",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                        elif respuesta == "INSUF":
                            data = {
                                "status": "1: Fondos insuficientes",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                        elif respuesta == "ERROR":
                            data = {
                                "status": "5: Error no controlado.",
                                "autorizacion": codigo,
                            }
                            respJson = json.dumps(data)
                            return respJson
                else:
                    data = {
                        "status": "4: Tarjeta vencida.",
                        "autorizacion": codigo,
                    }
                    respJson = json.dumps(data)
                    return respJson
            else:
                data = {
                    "status": "3: Tarjeta inactiva.",
                    "autorizacion": codigo,
                }
                respJson = json.dumps(data)
                return respJson
        else:
            data = {
                "status": "2: Datos incorrectos.",
                "autorizacion": codigo,
            }
            respJson = json.dumps(data)
            return respJson    
    else:
        data = {
                "status": "6: Cajero Invalido.",
                "autorizacion": codigo,
            }
        respJson = json.dumps(data)
        return respJson    
        
    
    
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
    
    # Enviar respuesta al cajero
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
  

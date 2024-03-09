import pymysql

conexion = pymysql.connect(
    host='localhost',
    user='gamili',
    password='3578951',
    database='dbautenticador',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def verificarTarjetaDB(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT numeroTarjeta, PIN, fechaVencimiento FROM tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None
    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None
    
def verificarEstadoTarjetaDB(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT estadoTarjeta FROM tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None

    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None
    
def verificarCajero(idCajero):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT idCajero FROM cajero WHERE idCajero = %s"
            cursor.execute(sql, (idCajero,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None

    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None
    
def verificarFechaTarjetaDB(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT fechaVencimiento FROM tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None

    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None
    
def verificarTipoTarjeta(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT tipoTarjeta FROM tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None
    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None
    
def getNroCuenta(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos de la tarjeta
            sql = "SELECT numeroCuenta FROM tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            datos_tarjeta = cursor.fetchone()
            if datos_tarjeta:
                return datos_tarjeta
            else:
                return None
    except pymysql.Error as e:
        print(f"Error al consultar datos de la tarjeta: {e}")
        return None

def consultarSaldo(numeroTarjeta):
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener el saldo disponible de la tarjeta
            sql = "SELECT montoDisponible FROM Tarjeta WHERE numeroTarjeta = %s"
            cursor.execute(sql, (numeroTarjeta,))
            saldo = cursor.fetchone()
            if saldo:
                # Convertir el saldo a texto
                montoSaldo = str(saldo)
                return montoSaldo
            else:
                # mensaje de error
                return "Tarjeta no encontrada o saldo no disponible"
    except pymysql.Error as e:
        print(f"Error al consultar saldo de la tarjeta: {e}")
        return "error"


# 2 Realizar avance de efectivo
def avanceEfectivo(numTarjeta, monto):
    try:
        with conexion.cursor() as cursor:
            # Consulta para actualizar el monto disponible de la tarjeta
            sql = "UPDATE Tarjeta SET montoDisponible = montoDisponible - %s WHERE numeroTarjeta = %s"
            cursor.execute(sql, (monto, numTarjeta))
            conexion.commit()
            return "ok"  # Avance de efectivo exitoso
    except pymysql.Error as e:
        print(f"Error al realizar avance de efectivo: {e}")
        return "error"


# 3 Cambiar PIN de la tarjeta
def cambiarPIN(numTarjeta, nuevo_PIN):
    try:
        with conexion.cursor() as cursor:
            # Consulta para actualizar el PIN de la tarjeta
            sql = "UPDATE Tarjeta SET PIN = %s WHERE numeroTarjeta = %s"
            cursor.execute(sql, (nuevo_PIN, numTarjeta))
            conexion.commit()
            return "ok"  # Cambio de PIN exitoso
    except pymysql.Error as e:
        print(f"Error al cambiar PIN de la tarjeta: {e}")
        return "error"
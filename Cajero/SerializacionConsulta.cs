using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cajero
{
    public class SerializacionConsulta
    {
        public byte[] NumeroTarjeta { get; set; }
        public byte[] PIN { get; set; }
        public byte[] FechaVencimiento { get; set; }
        public string CodigoVerificacion { get; set; }
        public string IdentificacionCajero { get; set; }
        public string TipoTransaccion { get; set; }

        // Constructor vacío necesario para la deserialización
        public SerializacionConsulta()
        {
        }

        // Constructor para inicializar los campos
        public SerializacionConsulta(byte[] numeroTarjeta, byte[] pin, byte[] fechaVencimiento, string codigoVerificacion,
                           string identificacionCajero, string tipoTransaccion)
        {
            NumeroTarjeta = numeroTarjeta;
            PIN = pin;
            FechaVencimiento = fechaVencimiento;
            CodigoVerificacion = codigoVerificacion;
            IdentificacionCajero = identificacionCajero;
            TipoTransaccion = tipoTransaccion;
        }
    }
}
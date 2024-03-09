using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cajero
{
    public class SerializacionCambio
    {
        public string NumeroTarjeta { get; set; }
        public string PIN { get; set; }
        public string nuevoPIN { get; set; }
        public string FechaVencimiento { get; set; }
        public string CodigoVerificacion { get; set; }
        public string IdentificacionCajero { get; set; }
        public string TipoTransaccion { get; set; }
   

        // Constructor vacío necesario para la deserialización
        public SerializacionCambio()
        {
        }

        // Constructor para inicializar los campos
        public SerializacionCambio(string numeroTarjeta, string pin, string nuevoPin, string fechaVencimiento, string codigoVerificacion,
                           string identificacionCajero, string tipoTransaccion)
        {
            NumeroTarjeta = numeroTarjeta;
            PIN = pin;
            nuevoPIN = nuevoPin;
            FechaVencimiento = fechaVencimiento;
            CodigoVerificacion = codigoVerificacion;
            IdentificacionCajero = identificacionCajero;
            TipoTransaccion = tipoTransaccion;
        }
    }
}
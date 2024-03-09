using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cajero
{
    public class SerializacionRetiro
    {
        public string NumeroTarjeta { get; set; }
        public string PIN { get; set; }
        public string FechaVencimiento { get; set; }
        public string CodigoVerificacion { get; set; }
        public string IdentificacionCajero { get; set; }
        public string TipoTransaccion { get; set; }
        public string MontoTransaccion { get; set; }

        // Constructor vacío necesario para la deserialización
        public SerializacionRetiro()
        {
        }

        // Constructor para inicializar los campos
        public SerializacionRetiro(string numeroTarjeta, string pin, string fechaVencimiento, string codigoVerificacion,
                           string identificacionCajero, string tipoTransaccion, string montoTransaccion)
        {
            NumeroTarjeta = numeroTarjeta;
            PIN = pin;
            FechaVencimiento = fechaVencimiento;
            CodigoVerificacion = codigoVerificacion;
            IdentificacionCajero = identificacionCajero;
            TipoTransaccion = tipoTransaccion;
            MontoTransaccion = montoTransaccion;
        }
    }
}
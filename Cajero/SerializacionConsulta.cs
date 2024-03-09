using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cajero
{
    public class SerializacionConsulta
    {
        public string NumeroTarjeta { get; set; }
        public string PIN { get; set; }
        public string FechaVencimiento { get; set; }
        public string CodigoVerificacion { get; set; }
        public string IdentificacionCajero { get; set; }
        public string TipoTransaccion { get; set; }

        // Constructor vacío necesario para la deserialización
        public SerializacionConsulta()
        {
        }

        // Constructor para inicializar los campos
        public SerializacionConsulta(string numeroTarjeta, string pin, string fechaVencimiento, string codigoVerificacion,
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
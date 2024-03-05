using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Cajero
{
    public partial class FrmConsulta : Form
    {
        public FrmConsulta()
        {
            InitializeComponent();
        }

        private void FrmConsulta_Load(object sender, EventArgs e)
        {

        }

        private void btAceptar_Click(object sender, EventArgs e)
        {
            AuthCode authObj = new AuthCode();
            byte[] key = null;
            byte[] iv = null;

            //encriptacion AES
            using (Aes aesAlg = Aes.Create())
            {
                // Genera un IV aleatorio de 16 bytes
                iv = aesAlg.IV;
                key = aesAlg.Key;
            }

            byte[] encNumeroTarjeta = AesEncryption.Encrypt(tbTarjeta.Text, key, iv);
            byte[] encFecVenc = AesEncryption.Encrypt(tbFecVenc.Text, key, iv);
            byte[] encPIN = AesEncryption.Encrypt(tbPIN.Text, key, iv);

            //Codigo autorizacion
            string authCode = authObj.GenerarCodigoAutorizacion(8);

            //asignaciones
            SerializacionRetiro transaccion = new SerializacionRetiro
            {
                NumeroTarjeta = encNumeroTarjeta,
                PIN = encPIN,
                FechaVencimiento = encFecVenc,
                CodigoVerificacion = authCode,
                IdentificacionCajero = "CAJERO123",
                TipoTransaccion = "consulta",
                MontoTransaccion = null
            };


            string json = JsonConvert.SerializeObject(transaccion);
            Console.WriteLine(json);


            // Abrir socket
            Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            socket.Connect("localhost", 8000);
            Console.WriteLine("Conectado al servidor.");


            // Convertir el json a un arreglo de bytes
            byte[] buffer = Encoding.UTF8.GetBytes(json);

            // Enviar el arreglo de bytes al servidor
            socket.Send(buffer);

            // Obtener la respuesta del servidor
            buffer = new byte[1024];
            int received = socket.Receive(buffer, SocketFlags.None);

            // Convertir el arreglo de bytes a un string
            string response = Encoding.UTF8.GetString(buffer, 0, received);

            Console.WriteLine(response);

            // Cerrar el socket
            socket.Close();

            Console.ReadLine();
        }
    }
}

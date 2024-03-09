﻿using Newtonsoft.Json;
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
    public partial class FrmCambio : Form
    {
        public FrmCambio()
        {
            InitializeComponent();
        }

        private void retiroToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FrmRetiro frm = new FrmRetiro();
            frm.Show();
        }

        private void consultaToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            FrmConsulta frm = new FrmConsulta();
            frm.Show();
        }

        private void cambioDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FrmCambio frm = new FrmCambio();
            frm.Show();
            
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

  

            string encNumeroTarjeta = AesEncryption.Encrypt(tbTarjeta.Text, key, iv);
            string encPIN = AesEncryption.Encrypt(tbPIN.Text, key, iv);
            string encNuevoPIN = AesEncryption.Encrypt(tbNuevoPIN.Text, key, iv);
            string encFecVenc = AesEncryption.Encrypt(tbFecVenc.Text, key, iv);

            //Codigo autorizacion
            string authCode = authObj.GenerarCodigoAutorizacion(8);

            //asignaciones
            SerializacionCambio transaccion = new SerializacionCambio
            {
                NumeroTarjeta = encNumeroTarjeta,
                PIN = encPIN,
                nuevoPIN = encNuevoPIN,
                FechaVencimiento = encFecVenc,
                CodigoVerificacion = authCode,
                IdentificacionCajero = "CAJERO123",
                TipoTransaccion = "cambio",
            
            };


            string json = JsonConvert.SerializeObject(transaccion);
            Console.WriteLine(json);


            // Abrir socket
            Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            socket.Connect("127.0.0.1", 8000);
            Console.WriteLine("Conectado al servidor.");
            //Trama para enviar clave de encriptado
            string keyBase64 = Convert.ToBase64String(key);
            string ivBase64 = Convert.ToBase64String(iv);
            string trama = "2:" + keyBase64 + ":" + ivBase64;
            // Convertir la trama a un arreglo de bytes
            byte[] bufferKey = Encoding.UTF8.GetBytes(trama);
            // Convertir el json a un arreglo de bytes
            byte[] buffer = Encoding.UTF8.GetBytes(json);
            int tmaño1 = bufferKey.Length;
            int tmaño2 = buffer.Length;

            Console.WriteLine(tmaño1);
            Console.WriteLine(tmaño2);

            // Enviar el arreglo de bytes al servidor
            socket.Send(bufferKey);

            // Enviar el arreglo de bytes al servidor
            socket.Send(buffer);

            // Obtener la respuesta del servidor
            buffer = new byte[1024];
            int received = socket.Receive(buffer, SocketFlags.None);

            // Convertir el arreglo de bytes a un string
            string response = Encoding.UTF8.GetString(buffer, 0, received);

            Console.WriteLine(response);

            lblResul.Text = response;

            // Cerrar el socket
            socket.Close();

            Console.ReadLine();
        }

        private void FrmCambio_Load(object sender, EventArgs e)
        {

        }
    }
}
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Cajero
{
    public partial class FrmPrincipal : Form
    {
        int nroTarjeta = 0;
        string fechaVenc = string.Empty;
        int PIN = 0;
        public FrmPrincipal()
        {
            InitializeComponent();
        }

        private void retiroToolStripMenuItem_Click(object sender, EventArgs e)
        {  
            FrmRetiro frm = new FrmRetiro();
            frm.Show();
        }

        private void consultaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FrmConsulta frm = new FrmConsulta();
            frm.Show();
        }

        private void cambioDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FrmCambio frm = new FrmCambio();
            frm.Show();
        }
    }
}

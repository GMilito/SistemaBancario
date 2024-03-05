namespace Cajero
{
    partial class FrmCambio
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.retiroToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.consultaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cambioDeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.tbNuevoPIN = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.btAceptar = new System.Windows.Forms.Button();
            this.tbPIN = new System.Windows.Forms.TextBox();
            this.tbFecVenc = new System.Windows.Forms.TextBox();
            this.tbTarjeta = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.retiroToolStripMenuItem,
            this.consultaToolStripMenuItem,
            this.cambioDeToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(334, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // retiroToolStripMenuItem
            // 
            this.retiroToolStripMenuItem.Name = "retiroToolStripMenuItem";
            this.retiroToolStripMenuItem.Size = new System.Drawing.Size(50, 20);
            this.retiroToolStripMenuItem.Text = "Retiro";
            this.retiroToolStripMenuItem.Click += new System.EventHandler(this.retiroToolStripMenuItem_Click);
            // 
            // consultaToolStripMenuItem
            // 
            this.consultaToolStripMenuItem.Name = "consultaToolStripMenuItem";
            this.consultaToolStripMenuItem.Size = new System.Drawing.Size(66, 20);
            this.consultaToolStripMenuItem.Text = "Consulta";
            this.consultaToolStripMenuItem.Click += new System.EventHandler(this.consultaToolStripMenuItem_Click_1);
            // 
            // cambioDeToolStripMenuItem
            // 
            this.cambioDeToolStripMenuItem.Name = "cambioDeToolStripMenuItem";
            this.cambioDeToolStripMenuItem.Size = new System.Drawing.Size(99, 20);
            this.cambioDeToolStripMenuItem.Text = "Cambio de PIN";
            this.cambioDeToolStripMenuItem.Click += new System.EventHandler(this.cambioDeToolStripMenuItem_Click);
            // 
            // tbNuevoPIN
            // 
            this.tbNuevoPIN.Location = new System.Drawing.Point(117, 105);
            this.tbNuevoPIN.Name = "tbNuevoPIN";
            this.tbNuevoPIN.Size = new System.Drawing.Size(100, 20);
            this.tbNuevoPIN.TabIndex = 19;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(10, 112);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(63, 13);
            this.label4.TabIndex = 18;
            this.label4.Text = "Nuevo PIN:";
            // 
            // btAceptar
            // 
            this.btAceptar.Location = new System.Drawing.Point(142, 141);
            this.btAceptar.Name = "btAceptar";
            this.btAceptar.Size = new System.Drawing.Size(75, 23);
            this.btAceptar.TabIndex = 17;
            this.btAceptar.Text = "Aceptar";
            this.btAceptar.UseVisualStyleBackColor = true;
            this.btAceptar.Click += new System.EventHandler(this.btAceptar_Click);
            // 
            // tbPIN
            // 
            this.tbPIN.Location = new System.Drawing.Point(117, 79);
            this.tbPIN.Name = "tbPIN";
            this.tbPIN.Size = new System.Drawing.Size(100, 20);
            this.tbPIN.TabIndex = 16;
            // 
            // tbFecVenc
            // 
            this.tbFecVenc.Location = new System.Drawing.Point(117, 53);
            this.tbFecVenc.Name = "tbFecVenc";
            this.tbFecVenc.Size = new System.Drawing.Size(100, 20);
            this.tbFecVenc.TabIndex = 15;
            // 
            // tbTarjeta
            // 
            this.tbTarjeta.Location = new System.Drawing.Point(117, 27);
            this.tbTarjeta.Name = "tbTarjeta";
            this.tbTarjeta.Size = new System.Drawing.Size(100, 20);
            this.tbTarjeta.TabIndex = 14;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(10, 60);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 13);
            this.label2.TabIndex = 13;
            this.label2.Text = "Fecha vencimiento:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(10, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(63, 13);
            this.label1.TabIndex = 12;
            this.label1.Text = "Nro Tarjeta:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(10, 86);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(28, 13);
            this.label3.TabIndex = 20;
            this.label3.Text = "PIN:";
            // 
            // FrmCambio
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 311);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.tbNuevoPIN);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.btAceptar);
            this.Controls.Add(this.tbPIN);
            this.Controls.Add(this.tbFecVenc);
            this.Controls.Add(this.tbTarjeta);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.Name = "FrmCambio";
            this.Text = "FrmCambio";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem retiroToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem consultaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cambioDeToolStripMenuItem;
        private System.Windows.Forms.TextBox tbNuevoPIN;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btAceptar;
        private System.Windows.Forms.TextBox tbPIN;
        private System.Windows.Forms.TextBox tbFecVenc;
        private System.Windows.Forms.TextBox tbTarjeta;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
    }
}
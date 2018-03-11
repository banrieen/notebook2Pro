using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Hello world ");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Text = "This is a Applicaton";
            this.BackColor = Color.FromArgb(255, 255, 0);
            //this.label1.Left += 200;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.label1.Text = e.X + "," +e.Y;
        }
        
        private void Form1_TextChanged(object sender, EventArgs e)
        {
            textBox2.Text = textBox1.Text;
        }


    }
}

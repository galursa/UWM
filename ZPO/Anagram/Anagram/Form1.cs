using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Anagram
{
    
    public partial class Anagram : Form
    {
        public Anagram()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string slowoZagadka = slowo1.Text;
            string slowoWynik = slowo2.Text;

            char[] litery = slowoWynik.ToArray();
            Array.Sort(litery);
            slowoWynik = new String(litery);

            string rezultatPrzegrana ="Przegrałeś. Słowa się niezgadzają";
            string rezultatWygrana = "Brawo. Odgadłeś słowo";
            bool roznica=false;

            if(slowoZagadka.Length!=slowoWynik.Length)
            {
                MessageBox.Show(rezultatPrzegrana, "Wynik", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            else
            {
                for(int i=0;i<slowoZagadka.Length;i++)
                {
                    if(slowoZagadka.ElementAt(i)!=slowoWynik.ElementAt(i))
                    {
                        roznica = false;
                    }
                    else
                    {
                        roznica = true;
                    }
                }
                if(roznica==false)
                {
                    MessageBox.Show(rezultatPrzegrana, "Wynik", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
                else
                {
                    MessageBox.Show(rezultatWygrana, "Wynik", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
            }

        }

        private void Anagram_Load(object sender, EventArgs e)
        {
            Anagramy nowyAnagram = new Anagramy();
            slowo1.Text = nowyAnagram.sortujLitery();
            slowo1.Enabled = false;
           this.ActiveControl = slowo2;
        }
    }

    public class Anagramy
    {
        //public List<string> listaSlow;
        private string slowo;
        public Anagramy()
        {
            this.slowo = "kajak";
        }
        #region toDoKonstruktor
        /*  public Anagramy()
        {
         * listaSlow = new List<string>();
            this.listaSlow.Add("kajak");
            this.listaSlow.Add("rower");
            this.listaSlow.Add("kolarz");
            this.listaSlow.Add("kawior");
            this.listaSlow.Add("ekran");
        }
        */
        #endregion
        public string losowanieSlowa()
        {
            return this.slowo;
            #region wlasciweLosowanie
            /*
            int iloscSlow = this.listaSlow.Count();
            Random generator = new Random();
            int indeksSlowa = generator.Next(1, iloscSlow);
            return this.listaSlow.ElementAt(indeksSlowa);
             */
            #endregion
        }

        public string sortujLitery()
        {
            char[] litery=this.slowo.ToArray();
            Array.Sort(litery);
            return new string(litery);
        }

        public void sprawdzSlowo()
        {

        }
    }


}

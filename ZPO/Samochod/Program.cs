using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Samochód
{
    class Samochod
    {
        private string Marka;
        private int LiczbaKol;
        private float Predkosc;
        private string Kolor;
        private int Rocznik;
        public static string rodzaj = "Osobowy";

        public Samochod(string Marka, int kola, float Predkosc, string kolor, int Rocznik)
        {
            this.Marka = Marka;
            this.LiczbaKol = kola;
            this.Predkosc = Predkosc;
            this.Kolor = kolor;
            this.Rocznik = Rocznik;
        }

        public Samochod()
        {               
        }

        public Samochod(string Marka, int kola, float Predkosc)
        {
            this.Marka = Marka;
            this.LiczbaKol = kola;
            this.Predkosc = Predkosc;
            this.Kolor = "Czarny";
            this.Rocznik = 2016;
        }

        public void Jedz(int koniec)
        {
            for (int i = 0; i <= koniec; i+=10)
            {
                this.Predkosc = i;
                Console.WriteLine("Jadę z prędkością: " + this.Predkosc + " km/h");
            }
        }
        public void Hamuj()
        {
            for (int i = (int)this.Predkosc; i >= 0; i -= 10)
            {
                this.Predkosc = i;
                Console.WriteLine("Hamuję z prędkością: " + this.Predkosc + " km/h");
            }
        }
        public void Wyswietl()
        { //to do poprawienie o sprawdzanie czy metody sa puste
            if (this.Marka == null)
            {
                Console.WriteLine("Samochód nie ma zdefiniowanych wartości");
            }
            else
            {
                Console.WriteLine(this.Kolor + " samochód marki " + this.Marka + " jedzie z prędkością " + this.Predkosc);
                Console.WriteLine("Ilość kół w samochodzie do " + this.LiczbaKol);
                Console.WriteLine("Rocznik Samochodu " + this.Rocznik);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Samochod audi = new Samochod();
            Samochod opel = new Samochod("Astra",4,120);
            Samochod fiat = new Samochod("126p", 4, 120, "biały", 1980);
            Samochod kart = new Samochod("GoKart", 3, 60, "szary", 2017);
            Samochod lazik = new Samochod("SegWay", 2, 10);
         
         //   Console.WriteLine("Rodzaj samochodu {0}",Samochod.rodzaj);
            List<Samochod> listaSamochodow = new List<Samochod>();
            listaSamochodow.Add(audi);
            listaSamochodow.Add(opel);
            listaSamochodow.Add(fiat);
            listaSamochodow.Add(kart);
            listaSamochodow.Add(lazik);

            foreach(Samochod egzemplarz in listaSamochodow)
            {
                egzemplarz.Wyswietl();
            }

            Console.ReadKey();
        }
    }
}

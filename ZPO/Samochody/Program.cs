using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Samochody
{
    class Samochod
    {
        private string Marka;
        private int LiczbaKol;
        private float Predkosc;
        private string Kolor;
        private int Rocznik;
        public Samochod(string varmarka, int varliczbaKol, float varpredkosc, string varkolor = "Czarny", int varRocznik = 2016)
        {
            this.Marka = varmarka;
            this.LiczbaKol = varliczbaKol;
            this.Predkosc = varpredkosc;
            this.Kolor = varkolor;
            this.Rocznik = varRocznik;
        }

        public void Jedz()
        {
            Console.WriteLine("Jadę z predkością "+this.Predkosc);
        }
        public void Hamuj()
        {
            int start = (int)this.Predkosc;
            for(int i=start; i>=0; i-=10)
            {
                this.Predkosc = (float)i;
                Console.WriteLine("Hamuje. Moja prędkość "+this.Predkosc);
            }
            Console.WriteLine("Zahamowałem");
        }
        public void WyswietlInfo()
        {
            Console.Write("Samochód "+this.Marka+" ma "+this.LiczbaKol+" kola.\n");
            Console.Write("Ma kolor: "+this.Kolor+". Rocznik: "+this.Rocznik+"\n");
        }
        public void WyswietlWRuchu()
        {
            Console.Write("{0} samochód marki {1} jedzie z prędkością {2}.",this.Kolor,this.Marka,this.Predkosc);
            Console.Write("Ilość kół w samochodzie do {0}.",this.LiczbaKol);
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Samochod opel = new Samochod("Astra", 4, (float)65.20);
            Samochod maluch = new Samochod("Fiat", 4, (float)60, "różowy", 1978);
            Samochod ford = new Samochod("Fiesta", 4, (float)120, "granatowy", 2000);
            List<Samochod> listaSamochodow = new List<Samochod>();
            listaSamochodow.Add(opel);
            listaSamochodow.Add(maluch);
            listaSamochodow.Add(ford);
            foreach(Samochod sm in listaSamochodow)
            {
                sm.Jedz();
                sm.WyswietlInfo();
                sm.WyswietlWRuchu();
                sm.Hamuj();
            }
            Console.ReadKey();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Koncerty
{
    class Program
    {
        class Koncerty
        {
            DateTime dataKoncertu;
            public Koncerty(DateTime data)
            {
                dataKoncertu = data;
            }
            public string NowyKoncert()
            {
                return dataKoncertu.ToLongDateString();
            }
        }

        //sealed blokuje dziedziczenie klasy
        public sealed class KoncertySingleton
        {
            //prywatne statyczne pole, gdzie przechowujemy utworzony ewentualnie obiekt domyślnie ustawione na null
            private static KoncertySingleton instance = null;
            private DateTime dataKoncertu;
            //konstruktor private lub protected, nie będzie można używać operatora new
            private KoncertySingleton(DateTime data) {
                dataKoncertu = data;
            }
            //Publiczna statycznametoda, która zwraca obiekt swojej klasy 
            //i tworzy ten obiekt w sytuacji gdy go nie ma
            public static KoncertySingleton Instance
            {
                get
                {
                    if (instance ==null)
                    {
                        instance = new KoncertySingleton(DateTime.Now);
                    }
                    return instance;
                }
            }
            //nasza dodatkowa metoda
            public string NowyKoncert()
            {
                return dataKoncertu.ToLongDateString();
            }
        }

        //bezpieczniejsza klasa z blokowaniem tworzenia nowych intsancji
        public sealed class KoncertySingletonLock
        {
            //prywatne statyczne pole, gdzie przechowujemy utworzony ewentualnie obiekt domyślnie ustawione na null
            private static KoncertySingletonLock instance = null;
            //Tworzymy wspóldzielnoy obiekt by potem go wykorzystąć do tego, że:
            //Wątki blokują wspóldzielnony object i sprawdzają czy instanajca została utworzona przed tworzeniem instancji.
        
            private static readonly object padlock = new object();
            private DateTime dataKoncertu;
            //konstruktor private lub protected, nie będzie można używać operatora new
            private KoncertySingletonLock(DateTime data)
            {
                dataKoncertu = data;
            }
            //Publiczna statycznametoda, która zwraca obiekt swojej klasy 
            //i tworzy ten obiekt w sytuacji gdy go nie ma
            public static KoncertySingletonLock Instance
            {
                get
                {
                    lock (padlock)
                    {
                        if (instance == null)
                        {
                            instance = new KoncertySingletonLock(DateTime.Now);
                        }
                        return instance;
                    }
                    
                }
            }
            //nasza dodatkowa metoda
            public string NowyKoncert()
            {
                return dataKoncertu.ToLongDateString();
            }
        }

        static void Main(string[] args)
        {
            DateTime data = new DateTime(2018, 2, 21);
            DateTime data2 = new DateTime(2018, 4, 21);
            Koncerty DepecheMode = new Koncerty(data);
            Koncerty ZenonMartyniuk = new Koncerty(data2);
            DepecheMode.NowyKoncert();
            ZenonMartyniuk.NowyKoncert();
            Console.WriteLine(DepecheMode.NowyKoncert());
            Console.WriteLine(ZenonMartyniuk.NowyKoncert());
            //Użycie Singletonu
            Console.WriteLine(KoncertySingleton.Instance.NowyKoncert());
            Console.ReadKey();
        }
    }
}

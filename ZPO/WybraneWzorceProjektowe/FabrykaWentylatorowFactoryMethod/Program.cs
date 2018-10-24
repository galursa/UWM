using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WentylatorSimpleFactory
{
    // na podstawie kodu ze strony: https://www.codeproject.com/articles/1131770/factory-patterns-simple-factory-pattern
    enum TypWentylatora
    {
        Stojacy,
        Sufitowy,
        Nawiewny
    }

    interface IWentylator
    {
        void Wlacz();
        void Wylacz();
    }

    

    class WentylatorNawiewny : IWentylator, IFabrykaWentylatorow
    {
        public IWentylator ZbudujWentylator()
        {
            IWentylator wentylator = new WentylatorNawiewny();
            return wentylator;
        }

        void IWentylator.Wlacz()
        {
            Console.WriteLine("Wlaczam WentylatorNawiewny");
        }

        void IWentylator.Wylacz()
        {
            Console.WriteLine("Wylaczam WentylatorNawiewny");
        }
    }
    class WentylatorStojacy : IWentylator, IFabrykaWentylatorow
    {
        public IWentylator ZbudujWentylator()
        {
            IWentylator wentylator = new WentylatorStojacy();
            return wentylator;
        }

        void IWentylator.Wlacz()
        {
            Console.WriteLine("Wlaczam WentylatorStojący");
        }

        void IWentylator.Wylacz()
        {
            Console.WriteLine("Wylaczam WentylatorStojący");
        }
    }

    interface IFabrykaWentylatorow
    {
        /* produkujemy wentylatory wiec poniższa metoda będzie zwracać typ IWentylator a przyjmuje 
         * parametr TypWentylatora */
        IWentylator ZbudujWentylator();
    }

    class WentylatorSufitowy: IWentylator, IFabrykaWentylatorow
    {
        public IWentylator ZbudujWentylator()
        {
            IWentylator wentylator = new WentylatorSufitowy();
            return wentylator;
        }

        void IWentylator.Wlacz()
        {
            Console.WriteLine("Wlaczam WentylatorSufitowy");
        }

        void IWentylator.Wylacz()
        {
            Console.WriteLine("Wylaczam WentylatorSufitowy");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            IFabrykaWentylatorow fabrykaWentylatorw = new WentylatorSufitowy();
            IWentylator smiglo = fabrykaWentylatorw.ZbudujWentylator();
            smiglo.Wlacz();
            Console.ReadKey();
            smiglo.Wylacz();
            Console.ReadKey();
        }
    }
}

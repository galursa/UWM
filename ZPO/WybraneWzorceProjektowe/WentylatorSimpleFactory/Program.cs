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

    class WentylatorSufitowy : IWentylator
    {
        void IWentylator.Wlacz()
        {
            Console.WriteLine("Wlaczam WentylatorSufitowy");
        }

        void IWentylator.Wylacz()
        {
            Console.WriteLine("Wylaczam WentylatorSufitowy");
        }
    }

    class WentylatorNawiewny : IWentylator
    {
        void IWentylator.Wlacz()
        {
            Console.WriteLine("Wlaczam WentylatorNawiewny");
        }

        void IWentylator.Wylacz()
        {
            Console.WriteLine("Wylaczam WentylatorNawiewny");
        }
    }
    class WentylatorStojacy : IWentylator
    {
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
        IWentylator ZbudujWentylator(TypWentylatora typ);
    }

    class FabrykaWentylatorow : IFabrykaWentylatorow
    {
        public IWentylator ZbudujWentylator(TypWentylatora typ)
        {
            switch(typ)
            {
                case TypWentylatora.Stojacy:
                    return new WentylatorStojacy();
                case TypWentylatora.Sufitowy:
                    return new WentylatorSufitowy();
                case TypWentylatora.Nawiewny:
                    return new WentylatorNawiewny();
                default:
                    return new WentylatorStojacy();
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            IFabrykaWentylatorow simpleFactory = new FabrykaWentylatorow();
            //tworzymy wiatrak z wykorzystaniem simpleFactory
            IWentylator wiatrak = simpleFactory.ZbudujWentylator(TypWentylatora.Stojacy);
            //używamy obiekt
            wiatrak.Wlacz();
            Console.ReadKey();
            wiatrak.Wylacz();
            Console.ReadKey();
        }
    }
}

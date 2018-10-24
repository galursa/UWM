using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WeatherObserver
{
    interface IWeatherObserver
    {
        void update();
    }
    
    interface IWeatherSubject
    {
        void attach(IWeatherObserver wo);
        void detach(IWeatherObserver wo);
        void notify();
    }

    class Weather : IWeatherSubject
    {
        //lista obiektów, które będą obserwować obiekty tej klasy 
        private List<IWeatherObserver> observers = new List<IWeatherObserver>();
        //Pola klasy
        private int Temperature;
        private int Humidity;
        private int Pressure;
        public void attach(IWeatherObserver wo)
        {
            observers.Add(wo);
        }

        public void detach(IWeatherObserver wo)
        {
            observers.Remove(wo);
        }

        public void notify()
        {
            foreach(var item in observers)
            {
                item.update();
            }
        }
        public int getTemperature()
        {
            return Temperature; 
        }
        public int getHumidity()
        {
            return Humidity;
        }
        public int getPressure()
        {
            return Pressure;
        }

        public void addVariables(int temp, int hum, int press)
        {
            this.Temperature = temp;
            this.Humidity = hum;
            this.Pressure = press;
        }
    }

    class WeatherObserver: IWeatherObserver
    {
        //Prywatne pola do przechowywania wartości
        private int observerTemperature;
        private int observerHumidity;
        private int observerPressure;
        //referencja do obserwowanego obiektu
        private Weather actualWeather;
        //definiujemy konstruktor i przypisujemy mu obiekt
        public WeatherObserver(Weather we)
        {
            actualWeather = we;
        }
        public void update()
        {
            observerTemperature = actualWeather.getTemperature();
            observerHumidity = actualWeather.getHumidity();
            observerPressure = actualWeather.getPressure();
            Console.WriteLine("Temperature: {0}, Humidity: {1}, Pressure: {2}",
                observerTemperature, observerHumidity, observerPressure);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
               //Tworzymy obiekt 
                Weather todayWeather = new Weather();
                //Tworzymy obserwatorów dla niego
                WeatherObserver observer1 = new WeatherObserver(todayWeather);
                WeatherObserver observer2 = new WeatherObserver(todayWeather);

                todayWeather.attach(observer1);
                todayWeather.attach(observer2);

                //Dopisujemy dane do pogody
                todayWeather.addVariables(20, 75, 1300);

                //Powiadamiamy obserwatorów
                todayWeather.notify();
                todayWeather.detach(observer1);
                Console.WriteLine();
                todayWeather.addVariables(15, 30, 1500);
                todayWeather.notify();
                Console.ReadKey();
        }
    }
}

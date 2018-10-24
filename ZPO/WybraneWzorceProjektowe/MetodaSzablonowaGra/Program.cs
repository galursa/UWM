using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetodaSzablonowaGra
{
    /*Tworzymy Szablon do Gier */
    abstract class Game
    {
        /* Hook methods. Concrete implementation may differ in each subclass*/
        protected int playersCount;
        protected abstract void initializeGame();
        protected abstract void makePlay(int player);
        protected abstract bool endOfGame();
        protected abstract void printWinner();
        /* A template method : */
        public void playOneGame(int playersCount)
        {
            this.playersCount = playersCount;
            initializeGame();
            int j = 0;
            while (!endOfGame())
            {
                makePlay(j);
                j = (j + 1) % playersCount;
            }
            printWinner();
        }
    }

    class PapierKamienNozyce : Game
    {
        private int winner;
        private int nrUzytkownika;
        private int nrKomputera;
        protected override bool endOfGame()
        {
            if (winner == 0)
            {
                return false;
            }
            else
            {
                if (nrKomputera == nrUzytkownika)
                {
                    winner = 4;
                }
                else if (nrUzytkownika == 1)
                {
                    if (nrKomputera == 2)
                    {
                        winner = 1;
                    }
                    else
                    {
                        winner = 2;
                    }
                }
                else if (nrUzytkownika == 2)
                {
                    if (nrKomputera == 1)
                    {
                        winner = 2;
                    }
                    else
                    {
                        winner = 1;
                    }
                }
                else if (nrUzytkownika == 3)
                {
                    if (nrKomputera == 1)
                    {
                        winner = 1;
                    }
                    else
                    {
                        winner = 2;
                    }
                }
            }
            return true;
        }

        protected override void initializeGame()
        {
            Console.WriteLine("Gra: papier, kamień, nożyce.");
            winner = 0;
        }

        protected override void makePlay(int player)
        {
           switch (player)
            {
                case 0:
                    Console.WriteLine("Podaj opcje:");
                    Console.WriteLine("1. Papier");
                    Console.WriteLine("2. Kamień");
                    Console.WriteLine("3. Nożyce");
                    string czytaj = Console.ReadLine();
                    nrUzytkownika = Int32.Parse(czytaj);
                    winner = 0;
                    break;
                case 1:
                    Random rnd = new Random();
                    nrKomputera = rnd.Next(1, 4);
                    winner = 5;
                    break;
                default:
                    break;
            } 
        }

        protected override void printWinner()
        {
            switch (winner)
            {
                case 1:
                    Console.WriteLine("Brawo wygrałeś użytkowniku!");
                    break;
                case 2:
                    Console.WriteLine("Wygrał komputer");
                    break;
                default:
                    Console.WriteLine("Tym razem remis");
                    break;
            }
        }
    }
    class PomyslOLiczbie : Game
    {
        private int roznica;
        private bool koniecGry;
        protected override bool endOfGame()
        {
            switch (koniecGry)
            {
                case false:
                    return false;
                case true:
                    return true;
                default:
                    return false;
                  
            }
        }

        protected override void initializeGame()
        {
            Console.WriteLine("Pomyśl o liczbie");
            koniecGry = false;
        }

        protected override void makePlay(int player)
        {
            Console.WriteLine("Pomnóż ją przez samą siebie i zapamiętaj");
            Console.WriteLine("Wciśnij dowolny klawisz kiedy będziesz gotowy");
            Console.ReadKey();
            Console.WriteLine("Odejmij 1 od liczby, o której pomyślałeś na początku. Otrzymany wynik pomnóż przez siebie samego i zapamiętaj.");
            Console.WriteLine("Wciśnij dowolny klawisz kiedy będziesz gotowy");
            Console.ReadKey();
            Console.WriteLine("Policz różnicę między zapamiętanymi liczbami i podaj mi ją");
            Console.Write("Twoja różnica: ");
            string odczyt = Console.ReadLine();
            roznica = Int32.Parse(odczyt);
            koniecGry = true;

        }

        protected override void printWinner()
        {
            int odgadnietaLiczba = (roznica + 1) / 2;
            Console.WriteLine("Twoja liczba to: {0}", odgadnietaLiczba);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            PapierKamienNozyce rozgrywka = new PapierKamienNozyce();
            rozgrywka.playOneGame(2);
            Console.ReadKey();
            PomyslOLiczbie rozgrywkaLiczba = new PomyslOLiczbie();
            rozgrywkaLiczba.playOneGame(2);
            Console.ReadKey();
        }
    }
}

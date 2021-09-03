using System;

namespace CargoShip
{
    class Program
    {
        static void Main(string[] args)
        {
            Ship ship = new Ship();

            Console.WriteLine("Welcome to cargo loader.");
            Console.WriteLine("The aim of the game is to load up the ship with the maximum number of vehicles you can.");
            Console.WriteLine("The weight of a bike is 3 units, car is 5, lorry is 11 and a train is 7 ");

            while (ship.Capacity != ship.getShipLoad())
            {
                Console.WriteLine("---------------");
                Console.WriteLine($"The ship capacity is {ship.Capacity}");
                Console.WriteLine("The ship has:");
                Console.WriteLine($"{ship.CycleCount} bikes, {ship.CarCount} cars, {ship.LorryCount} Lorries and {ship.TrainCount} trains");
                Console.WriteLine($"The ship currently has {ship.getShipLoad()} total units on board");
                Console.WriteLine("---------------");
                Console.WriteLine($"How many bikes would you like to put on board?: ");
                int x = int.Parse(Console.ReadLine());
                ship.CycleCount = x;
                Console.WriteLine($"How many cars would you like to put on board?: ");
                x = int.Parse(Console.ReadLine());
                ship.CarCount = x;
                Console.WriteLine($"How many lorries would you like to put on board?: ");
                x = int.Parse(Console.ReadLine());
                ship.LorryCount = x;
                Console.WriteLine($"How many trains would you like to put on board?: ");
                x = int.Parse(Console.ReadLine());
                ship.TrainCount = x;
            }
            Console.WriteLine("Cool You did it!");

        }
    }
}

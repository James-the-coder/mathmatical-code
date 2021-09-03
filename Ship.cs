using System;
using System.Collections.Generic;
using System.Text;

namespace CargoShip
{
    class Ship
    {
        public const int CycleWeight = 3;
        public const int CarWeight = 5;
        public const int TrainWeight = 7;
        public const int LorryWeight = 11;
        public const int MaxWeight = 10;

        public int Capacity { get; set; }
        public int CycleCount { get; set; }
        public int CarCount { get; set; }
        public int TrainCount { get; set; }
        public int LorryCount { get; set; }

        Random random = new Random();

        public int getShipLoad()
        {
            return CarCount * CarWeight + CycleCount * CycleWeight + LorryCount * LorryWeight + TrainCount * TrainWeight;
        }

        public Ship()
        {
            CycleCount = 0;
            LorryCount = 0;
            TrainCount = 0;
            CarCount = 0;

            Capacity = random.Next(MaxWeight) * CycleWeight + random.Next(MaxWeight) * CarWeight + random.Next(MaxWeight) * LorryWeight + random.Next(MaxWeight) * TrainWeight;
        }

        public int overUnder()
        {
            return Capacity - getShipLoad();
        }

        public override string ToString()
        {
            return ($"Capacity = {Capacity}, CurrentLoad = {getShipLoad()}");
        }

    }
}

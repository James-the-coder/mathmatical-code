using System;
using System.Numerics;

namespace factorial_digits
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                BigInteger factorial = 1;
                int total = 0;
                Console.WriteLine("Enter the number: ");
                int num = int.Parse(Console.ReadLine());
                for (int i = 1; i <= num; i++)
                {
                    factorial *= i;
                }
                string number = Convert.ToString(factorial);
                char[] digits = number.ToCharArray();
                foreach (char digit in digits)
                {
                    string stringDigit = Convert.ToString(digit);
                    int intDigit = Convert.ToInt32(stringDigit);
                    total += intDigit;
                }
                Console.WriteLine($"{num} factorial is {factorial}");
                Console.WriteLine($"The sum of the digits is {total}");
            }
            
        }
    }
}

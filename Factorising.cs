using System;
using System.Collections.Generic;

namespace Factorisor
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>();
            Console.WriteLine("Linear Equation Factorising");
            Console.WriteLine("Enter the equation: ");
            string equation = Console.ReadLine();
            numbers = LocateNumbers(equation);
            int a = numbers[0];
            int b = numbers[1];
            int result  = HighestCommonFactor(a,b);
            Console.WriteLine($"{result}({a/result}x + {b/result})");
        }

        static List<int> LocateNumbers(string eq)
        {
            List<int> numbers_ = new List<int>();
            string num = string.Empty;
            for (int i = 0; i < eq.Length; i++)
            {
                if (Char.IsDigit(eq[i]))
                {
                    num += eq[i];
                }
                else
                {
                    if (num.Length > 0)
                    {
                        numbers_.Add(Convert.ToInt32(num));
                    }
                    num = string.Empty;
                }
            }
            numbers_.Add(Convert.ToInt32(num));
            return numbers_;
        }

        static int HighestCommonFactor(int a, int b)
        {
            
            if (b == 0)
            {
                return a;
            }
            return HighestCommonFactor(b, a % b);
        }
    }
}

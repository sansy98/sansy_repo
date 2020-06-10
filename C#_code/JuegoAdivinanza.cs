using System;

namespace Tutoriales_20
{
    class Program
    {
        public static void Main(string[] args)
        {
            Random num = new Random();
            int randnum = num.Next(0, 100);
            int guess = 101;
            int tries = 6;

            while (tries != 0 && guess != randnum)
            {
                tries--;
                Console.WriteLine("Make a guess! You have " + tries + " tries left");
                guess = int.Parse(Console.ReadLine());
                if (guess < randnum) { Console.WriteLine(guess + " is lower than the solution!"); }
                else if (guess > randnum) { Console.WriteLine(guess + " is higher than the solution!"); }
            }

            if (tries == 0)
            {
                Console.WriteLine("You are out of attempts!");
            }
            else Console.WriteLine("Correct! You've won!");
        }
    }
}

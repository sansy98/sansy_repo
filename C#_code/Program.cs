using System;

namespace Calculadora
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.Write("Introduce el primer número: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("Introduce el operador: ");
            string operand = Console.ReadLine();
            Console.Write("Introduce el segundo número: ");
            double num2 = double.Parse(Console.ReadLine());

            switch(operand)
            {
                case "+":
                    Console.WriteLine(addition(num1, num2));
                    break;
                case "-":
                    Console.WriteLine(substraction(num1, num2));
                    break;
                case "*":
                    Console.WriteLine(multiplication(num1, num2));
                    break;
                case "/":
                    Console.WriteLine(fraction(num1, num2));
                    break;
                case "^":
                    Console.WriteLine(power(num1, num2));
                    break;
                case "#":
                    Console.WriteLine(root(num1, num2));
                    break;
            }

            double addition(double x, double y) => x + y;

            double substraction(double x, double y) => x - y;

            double multiplication(double x, double y) => x * y;

            double fraction(double x, double y) => x / y;

            double power(double x, double y) => Math.Pow(x, y);

            double root(double x, double y) => Math.Pow(x, 1 / y);
        }
    }
}

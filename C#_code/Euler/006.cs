using System;
using System.Linq;

namespace Euler006
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int on = 0;
            int off = 0;
           
            foreach (int i in Enumerable.Range(1, 100))
            {
                on += (int)Math.Pow(i, 2);
                off += i;
            }
            Console.WriteLine(Math.Pow(off, 2) - on);
        }
    }
}
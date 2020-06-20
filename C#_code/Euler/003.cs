using System;

namespace Euler003
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine(PrimDecomposer(600851475143));
        }

        public static int PrimDecomposer(long lnum)
        {
            int i = 2;
            while (lnum > 1)
            {
                if (lnum % i == 0) lnum /= i;
                else i++;
            }
            return i;
        } 
    }
}


using System;
using System.Linq;

namespace Euler002   //Fibonacci
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int[] r = new int[] { 1 };
            int n = 1;
            int prev = 1;
            int res = 0;

            while (n < 4000000)
            {
                n += prev;
                prev = n - prev;
                r = r.Concat(new int[] { n }).ToArray();
            }

            foreach (int i in r) if (i % 2 == 0) res += i;
            Console.WriteLine(res);
        }
    }
}

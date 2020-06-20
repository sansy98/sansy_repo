using System;
using System.Collections.Generic;
using System.Linq;

namespace Euler001 // 5 & 3 multiples
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            IEnumerable<int> r = Enumerable.Range(1, 999);
            int sum = 0;
            foreach (int i in r) if ((i % 3) == 0 | (i % 5) == 0) sum += i;
            Console.WriteLine(sum);
        }
    }
}
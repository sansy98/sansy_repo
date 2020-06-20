using System;
using System.Linq;

namespace Euler005
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int[] nums = Enumerable.Range(2, 19).ToArray();
            int x = 0;
            int repcount = 0;
            while (true)
            {
                x++;
                foreach (int i in nums)
                {
                    if (x % i != 0)
                    {
                        repcount = 0;
                        break;
                    }
                    else repcount++;
                }
                if (repcount == 19)
                {
                    Console.WriteLine(x);
                    break;
                }
            }
        }
    }
}
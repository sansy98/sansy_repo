using System;
using System.Linq;

namespace Euler004
{
    class MainClass
    {
        const int tac = 10;

        public static void Main(string[] args)
        {
            int[] palindromes = { };

            for (int x = 100; x < 1000; x++)
            {
                for (int y = 100; y < 1000; y++)
                {
                    int num = x * y;
                    if (IsPalindrome(num)) palindromes = palindromes.Concat(new int[] { num }).ToArray();
                }
            }
            Console.WriteLine(palindromes.Max());
        }

        public static bool IsPalindrome(int num)
        {
            int[] dig = new int[] { };
            int[] invdig = new int[] { };
            int bcknum = num;                   //"COPIA DE SEGURIDAD" DEL NUM ORIGINAL
            int idig;
            int tempmod;
            int clock = 0;

            while (true)
            {
                clock++;
                tempmod = num % tac;
                num = (num - (num % tac)) / 10;
                invdig = invdig.Concat(new int[] { tempmod }).ToArray();
                if (num < 10)
                {
                    invdig = invdig.Concat(new int[] { num }).ToArray();
                    break;
                }
            }

            num = bcknum;
            int retac = (int)Math.Pow(tac, clock);

            while (true)
            {
                idig = (num - (num % retac)) / retac;
                dig = dig.Concat(new int[] { idig }).ToArray();
                num %= retac;
                retac /= 10;
                if (retac == 1)
                {
                    dig = dig.Concat(new int[] { num }).ToArray();
                    break;
                }
            }

            string a = string.Join(string.Empty, dig);
            string b = string.Join(string.Empty, invdig);
            if (a == b) return true; return false;
        }
    }
}

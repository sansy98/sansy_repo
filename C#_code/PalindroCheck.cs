using System;

namespace PalindroCheck
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("What word do you want to check? \n");
            if (ReverChecker(Console.ReadLine())) Console.WriteLine("This word is a palindrome!");
            else Console.WriteLine("This word isn't a palindrome!");
        }

        public static bool ReverChecker(string word)
        {
            char[] charray = word.ToCharArray();
            char[] invcharray = charray;
            int r = 0;
            int c = word.Length - 1; 
            foreach (char i in invcharray) 
            {
                charray = word.ToCharArray(); //Charray value gets restored to ensure that the original array does't invert as well
                invcharray[r] = (char)charray.GetValue(c);
                r++;
                c--;
            }
            string pre = new string(charray);
            string post = new string(invcharray);
            if (pre == post) return true;
            else return false;
        }
    }
}
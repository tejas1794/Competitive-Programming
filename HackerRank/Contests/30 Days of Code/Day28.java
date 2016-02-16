/*
Day 28: RegEx, Patterns, and Intro to Databases!

Given a string, determine if it's a valid Pattern or not. The string may contain spaces.

Note: This is a java only challenge, a RegEx is only valid if you can compile it using the Pattern.compile method. You may find using a try-catch block helpful here.

Input Format

The first line of input contains an integer, T (the number of test cases). 
The T subsequent lines of test cases each contain a string of characters describing a RegEx.

Constraints 
1<=T<=100
Output Format

On a new line for each test case, print Valid if the given RegEx's syntax is correct; otherwise, print Invalid.

Sample Input

3
([A-Z])(.+)
[AZ[a-z](a-z)
batcatpat(nat
Sample Output

Valid
Invalid
Invalid
Explanation

The second and third test cases have unbalanced brackets and will throw a PatternSyntaxException when compiled. For example:

[AZ[a-z](a-z) is Invalid, but [AZ[a-z](a-z)] would be Valid. 
batcatpat(nat is Invalid, but batcatpat(nat) would be Valid.

*/

import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
   public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases-->0){
         String pattern = in.nextLine();
         try {
             Pattern.compile(pattern);
             System.out.println("Valid");
         } catch (Exception e) {
             System.out.println("Invalid");
         }
      }
   }
}
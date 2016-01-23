/**
Day 21: Generics!

Let's say you have an integer array and a string array. You have to write a single method printArray that can print all the elements of both arrays. The method should be able to accept both integer arrays or string arrays.

You are given code in the editor. Complete the code so that it prints the following lines:

1
2
3
Hello
World
Do not use method overloading because your answer will not be accepted.
*/

#include <iostream>
#include <vector>

using namespace std;

class Printer
{
    public <T> void printArray(T[] a) {
        for (T elem : a) {
            System.out.println(elem);
        }
    }
}

int main()
{
    vector<int> vInt{1, 2, 3};
    vector<string> vString{"Hello", "World"};
    
    printArray<int>(vInt);
    printArray<string>(vString);
    
    return 0;
}
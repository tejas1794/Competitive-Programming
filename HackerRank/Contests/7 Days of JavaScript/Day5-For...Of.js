/*
Task

We have created an array my_array whose elements are strings. Your task is to print the elements which are palindromes.

Constraints

0=size of array=1000=size of array=100 
0=size of each string=1000=size of each string=100
Hint

You can learn about how to reverse a string in place, here.

Note

Do not declare the variable my_array
*/

//Write your code below this line.

for(var str of my_array){
    if(str == str.split('').reverse().join('')){
        console.log(str);
    }
}
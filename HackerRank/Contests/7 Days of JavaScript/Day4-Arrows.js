/*Task

You are given a variable, my_function. Your task is to assign it with an arrow function. 
The my_function should take an array as its parameter and return an array with all its even elements incremented by 11, and odd elements decremented by 11.

Note

DON'T use function instead of an arrow function.
DON'T print anything on the console.
Replace the blank (_________) with an arrow function.
The name of the array parameter can be anything. For example, some_array.
*/

// write the correct arrow function here

var my_function = (some_array) => some_array.map( (item) => item % 2 === 0? ++item: --item);

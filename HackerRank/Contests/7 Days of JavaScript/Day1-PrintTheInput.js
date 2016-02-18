/*
Task

Use what you learned in the previous challenge to complete the processDataprocessData function by printing the inputinput parameter to the console.

Input Format

The first and only line of input contains a string.

Constraints

String length ≤500≤500
Output Format

Print inputinput to the console.

Sample Input

How many chickens does it take to cross the road?
Sample Output

How many chickens does it take to cross the road? 
*/

function processData(input) {
    //Enter your code here
    console.log(input);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});

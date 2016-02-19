/*
Task

In this example, you are given a single line consisting of property type values of a car in the following order:

TypeName ModelName ColorName
These values are assigned to an object car that has the properties type, model and color (read the code in the editor carefully to learn how that is done). Your task is to complete the code to print the object.

Sample Input

Fiat 500 White
Sample Output

{ type: 'Fiat', model: '500', color: 'White' }
*/

function printObjectProperty(myObject) {
  //Write your code here
    console.log(myObject);
} 

// The below code is to show how to create an Object. 
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    var obj = _input.split(' ');
    var myObject = new Object;
    myObject.type = obj[0];
    myObject.model = obj[1];
    myObject.color = obj[2];

    printObjectProperty(myObject);
});

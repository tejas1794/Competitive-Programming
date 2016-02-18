/*Write a function that prints Hello World! in the console below. */

function processData(input) {
    //Enter your code here
    var my_string = "Hello World!";
    console.log(my_string);
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

/*Write a JavaScript program to generate the pattern below, composed of the following characters: / and \.

/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\
/\/\/\/\/\/\/\

Input Format

No input is required to complete this challenge.*/

function processData(input) {
    console.log(Array(15).join(Array(8).join("\u2571\u2572")+'\n'));
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

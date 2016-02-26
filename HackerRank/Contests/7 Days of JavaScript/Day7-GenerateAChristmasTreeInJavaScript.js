/*Write a JavaScript program to generate the Christmas Tree pattern below. The tree should be composed of zeroes (0), and it must be topped with an asterisk (*).

        *
        0
       000
      00000
     0000000
    000000000
   00000000000
  0000000000000
 000000000000000
00000000000000000
Note: The leftmost 00 should be aligned with the left edge and there should not be any blank spaces preceding it on the last line.

Input Format

No input is required to complete this challenge.
*/

function processData(input) {
   var loveTree = `        *
        0
       000
      00000
     0000000
    000000000
   00000000000
  0000000000000
 000000000000000
00000000000000000
`
    console.log(loveTree);  
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

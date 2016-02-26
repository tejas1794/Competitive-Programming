/*Mark and Jane are very happy after having their first kid, and Mark wants to buy some toys for him. There are NN different toys, tagged with their prices, but he has only $K$K. He wants to buy the maximum number of toys for his son.

You are Mark's best friend and have to help him buy as many toys as possible.

Input Format

The first line contains two integers, NN and KK separated by a space. 
The next line contains NN space separated integers indicating the price of each toy.

Output Format

Output an integer that denotes the maximum number of toys Mark can buy with $K$K.

Constraints 
1<=N<=1051<=N<=105 
1<=K<=1091<=K<=109 
1<=price of any toy<=1091<=price of any toy<=109 
A toy can't be bought multiple times.

Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only 44 toys at the most. These toys have the following prices: 1,12,5,101,12,5,10.*/

function processData(input) {
    // Split the function at the new line.
    var rows = input.split('\n');
    var cash = rows[0].split(' ').map(Number)[1];
    var arr = rows[1].split(' ').map(Number);
    arr = arr.sort(function(a, b){return a-b}); 
    var numofToys = 0;
    while(cash>=0) {
        cash -= arr[numofToys];
        numofToys++;
    }
    
    // must denote -1 to compesate for the extra loop pass
    console.log(numofToys-1);
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

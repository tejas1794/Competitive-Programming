/*You are given N numbers. Store them in an array and find the second largest number.

Input Format

The first line contains NN, the size of array AA.
The second line contains NN space separated elements of array AA.

Output Format

Output the value of the second largest number in array AA.

Sample Input

5
2 3 6 6 5
Sample Output

5
*/

function processData(myArray) {
    var max_number = 0;
    var second_max_number = 0;
    for(var i = 0;i<myArray.length;i++){
        if(myArray[i]>max_number){
            max_number = myArray[i];
        }
    }
    for(var j = 0;j<myArray.length;j++){
        if(myArray[j]>second_max_number && myArray[j]<max_number){
            second_max_number = myArray[j];
        }
    }
    console.log(second_max_number);
}


// tail starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input.split('\n')[1].split(' ').map(Number));
});



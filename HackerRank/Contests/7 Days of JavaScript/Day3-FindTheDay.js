/*Write a JavaScript function to get the day of a particular date.

Input Format

Several lines of input containing dates in MM/DD/YYYY format. 
The program should end when it encounters -1-1.

Output Format

Print the day of the week indicated by the date for each line of input on a separate line.

Sample Input

10/11/2009
11/10/2010
-1
Sample Output

Sunday
Wednesday
*/

function findDay(myDate) {
    // Return day for date myDate(MM/DD/YYYY)
    // Note that myDate contains the date in string format
    if(myDate != -1){
        var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
         var d = new Date(myDate);
        console.log(days[d.getDay()]);
    }
} 

// tail starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    var dates = _input.split('\n');

    for (var i = 0; i < dates.length - 1; i++) {
        findDay(dates[i]);
    }
});

/*You are given a matrix with mm rows and nn columns of cells, each of which contains either 11 or 00. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. The connected and filled (i.e. cells that contain a 11) cells form a region. There may be several regions in the matrix. Find the number of cells in the largest region in the matrix.

Input Format
There will be three parts of t input:
The first line will contain mm, the number of rows in the matrix.
The second line will contain nn, the number of columns in the matrix.
This will be followed by the matrix grid: the list of numbers that make up the matrix.

Output Format
Print the length of the largest region in the given matrix.

Constraints
0<m<100<m<10
0<n<100<n<10

Sample Input:

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output:

5
Task: 
Write the complete program to find the number of cells in the largest region.

Explanation

X X 0 0
0 X X 0
0 0 X 0
1 0 0 0  
The X characters indicate the largest connected component, as per the given definition. There are five cells in this component.*/

function findN(r, c, maxr, maxc, lelarray){

    if(r >= maxr) r = maxr-1;
    if(c >= maxc) c = maxc-1;
    if(r < 0) r = 0;
    if(c < 0) c = 0;

    count = 0;
    var val = lelarray[r][c];
    if(val == -69) return 0; 
    if(val == 0) return 0;
    if(val == 1){
        count++;
        lelarray[r][c] = -69; 

        count += findN(r+1, c, maxr, maxc, lelarray);
        count += findN(r-1, c, maxr, maxc, lelarray);
        count += findN(r, c+1, maxr, maxc, lelarray);
        count += findN(r, c-1, maxr, maxc, lelarray);
        count += findN(r+1, c+1, maxr, maxc, lelarray);
        count += findN(r-1, c-1, maxr, maxc, lelarray);
        count += findN(r-1, c+1, maxr, maxc, lelarray);
        count += findN(r+1, c-1, maxr, maxc, lelarray);
    }
    return count;
}

function processData(input) {

    var lines = input.split("\n");
    var r = Number(lines[0]);
    var c = Number(lines[1]);
    var arr = Array();
    var cur = 2;
    while(r - arr.push(lines[cur].split(" ").map(Number)) > 0) { cur++; }

    var counts = Array();
    for(var i = 0; i < r; i++){
        for(var j = 0; j < c; j++){
            if(arr[i][j] == 1){
                counts.push(findN(i, j, r, c, arr));
            }
        }
    }

    var result = 0;
    for(var i = 0; i < counts.length; i++){
        if(counts[i] >= result){
            result = counts[i];
        }
    }
    console.log(result);
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

/*Task

We have declared a global variable index. Your task is to edit the given code so that the value of the global variable doesn't change.*/

//Global variable index has been declared and initialized
//Edit the code below.
console.log("The global index (before for-loop) is : ", index);

for(let index = 0; index < N; index++){
    console.log("The local index is : ",index);
}

console.log("The global index (after for-loop) is : ",index);

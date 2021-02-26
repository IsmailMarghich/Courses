/*we can use loops to execute blocks of code multiple times*/
/*for loops are loops that keep executing code until the condition statement becomes false*/
for (let n = 0; n < 5; n++){ /*n will increase each run of the loop, and the loop will stop after n is not less than 5*/
    console.log("loop number: ", n);
}
let list = [1,2,3,4,5]
for (let i in list) { /*a for in loop will create a loop that executes as many times as there is entries in an array*/
    console.log(list[i]) /*each loop we log an index from the list*/
}
let condition = 0;
while (condition < 5){ /*while loops continue running code as long as the condition is satisfied*/
    console.log("while loop number: ", condition);
    condition++;
}
let docondition = 5;
do { /*do while loops are similar, but the code is run before checking the condition*/
    console.log(docondition);
    docondition--;
}while (docondition > 0);
list.forEach(function (i){ /*theres also the for each loop, which is the easiest way to loop in an array*/
    console.log("for each", i);
})
list.forEach(function(i, index){ /*we can get the index by assigning a second parameter to the function*/
    console.log("at index ", index, "value =", i); /*this logs the index of the array with its value*/
})
/*map, filter and reduce are handy js methods*/
let array = [1,2,3,4];
/*a map can iterate over an array and apply a function to it, in this case doubling numbers*/
let double_array = array.map((num)=> num * 2);

console.log(double_array);
/*we can use filter to add a condition for putting items into an array*/
let filter_array = array.filter(num => num > 2) /*wil put items that are above value of 2 in the array*/
console.log(filter_array);

/*we can use reduce to iterate over an array and store the items in an accumulator*/
let reduced_array = array.reduce((accumulator, num)=>{
    return accumulator + num /*this will sum up the array*/
}, 0); /*0 is the start of accumulator we can set*/
console.log(reduced_array); /*returns sum of array*/
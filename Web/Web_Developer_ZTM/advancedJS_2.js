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
/*we can use classes to make objects based on a blue print, classes contain variables and methods
* we make an instance of a class with a constructor*/
class Player {
    constructor(name, xp, clan) { /*takes 3 arguments*/
        this.name = name; /*this refers to this object, it sets the argument as variables of the object*/
        this.xp = xp;
        this.clan = clan;
    }
    introduce(){ /*this method we can call and it displays information about the object*/
        console.log(`Hello I am ${this.name}, I come from the ${this.clan} clan and my xp is ${this.xp}`)
    }
}
let Levi = new Player("Levi", 100, "Ackerman") /*we create an instance of a class with new keyword*/
Levi.introduce();
/*we can also add a child class to the class above, which inherits its variables and methods*/
class Wizard extends Player{ /*extends means it inherits from the class*/
    constructor(name, xp, clan, type) { /*a constructor with an extra variable*/
        super(name, xp, clan, type); /*super refers to the class above to construct with its arguments*/
        this.type = type; /*we assign our additional argument from child class to the object*/
    }
    battlecry(){
        console.log(`I am a ${this.type} wizard `)
    }
}
let wizard_levi = new Wizard("Wizard Levi", 100, "Ackerman", "Fire");
wizard_levi.introduce();
wizard_levi.battlecry();
/*we will now go over modern javascript features that were added recently*/
/*ES7 2016*/
let string = "Hello";
console.log(string.includes('e'));/*.includes method returns true if a string or array contains the argument*/
console.log(2**2); /*we can use ** to square, 2 to the power of 2*/

/*ES8 2017*/
console.log(string.padStart(10)); /*pad tart and padend add spaces to the beginning or end of strings, based on length of string*/
console.log(string.padEnd(10) + "end"); /*10 - 5 = 5 spaces*/

/*lets say we have an object that stores data and we wanna print its data*/
let object = {
    name1 : 'John',
    name2 : 'James',
    name3 : 'Jonatan'
}
Object.keys(object).forEach((key) => { /*.keys allows use to access the keys of an object like an array*/
    console.log(key, object[key]) /*loop to print all keys and values in an object*/
}) /*there is an easier way to do these however */
Object.values(object).forEach(value => { /*.values can only access values*/
    console.log(value);
})
Object.entries(object).forEach(name => { /*.entries logs them as arrays, which allows us to perform array methods on them*/
    console.log(name);
})
/*ES9 2018*/

/*ES10 2019*/
let list = [1,[2,3],[4,5]]; /*lets say we have an array with nested arrays*/
console.log(list.flat()); /*.flat will remove the nested ones and make it as if there is no nested arrays*/

let trim_start = "    hello"
let trim_end = "hello      "
console.log(trim_start.trimStart()); /*trim start removes spaces from start of string*/
console.log(trim_end.trimEnd()); /*trim start removes spaces from end of string*/

/*we can convert a 2d array into key value pairs stored in an object*/
let userarray = [["Bob",5],["James", 7],["Patrick", 9]];
let obj = Object.fromEntries(userarray);
console.log(Object.entries(obj));

let string1 = "5";

try { /*try this block of code*/
    let error = true - string1 /*invalid operation*/
} catch{ /*if there is an error, run this code*/
    console.log("Error!!");
}


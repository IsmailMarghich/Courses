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

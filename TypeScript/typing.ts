/*with type annotations in typescript we can tell the compiler that a variable or function should be a certain type*/
/*primitive types, types by default in javascript*/
let word: string = "hello";
let number: number = 5;
let bool: boolean = true;
let empty: void;
/*object types, user made types*/
/*every variable in javascript has a type, even objects and functions*/

/*objects can have types as well*/
let today: Date = new Date();
let myNumbers: number[] = [1, 2, 3, 4, 5]; /*an array with only integers*/
class Car {}
let car: Car = new Car(); /*a variable of type Car class*/
/*object literal*/
let point: { x: number; y: number } = {
  x: 10 /*we add tying by adding an annotation to the properties*/,
  y: 20,
};
/*typing on objects*/
const profile = {
  name: "bob",
  age: 25,
  coords: {
    lat: 2,
    long: 57,
  },
  setAge(age: number): void {
    this.age = age;
  },
};
const {
  /*we can add typing to destructuring by specifying the structure of the object and its types*/
  age,
}: {
  age: number;
} = profile;
/*destructuring an object from an object*/
const {
  /*destructuring*/ coords: { lat, long },
}: { coords: { lat: number; long: number } } = profile; /*structure and typing*/

/*functions*/
/*function return values, as well as the arguments can have types*/
const drawNumber = (max: number): number => {
  return Math.floor(
    Math.random() * max
  ); /*draws a random number based on a maximum set from user*/
};
/*void type means nothing*/
const voidFunc = (i: number): void => {
  console.log(
    "I dont return anything, so my return type is void, here is my number tho",
    i
  );
};
/*types are used by the compiler to detect errors before running our code
 * types also allow other developers to more easily understand what the point of a function or variable is*/
/*type inference refers to typescript automatically assigning types to values, we dont have to implicitly add types everytime
 * but sometimes the typescript compiler cant figure it out itself:*/
const json =
  '{"X":false, "Z":50}'; /*1, a JSON string that stores coordinates, typescript has no idea what types these values are*/
const coordinates: { X: number; Z: number } = JSON.parse(
  json
); /*we can add typing to the object were parsing our JSON into*/
console.log(coordinates);

/*2, declaring a variable on one line and initializing it later*/
let words = ["red", "green", "blue"];
let foundWord: boolean; /*we have to add typing here ourselves because the variable is given a value in the loop below*/
words.forEach((item) => {
  if (item === "green") {
    foundWord = true;
  }
});
/*3, variable whose type cannot be found correctly*/
let numbers = [-1, 2, 10];
let numberAboveZero: number[] = []; /* = false*/ /*if we set out future array as false, typescript will assign that type, but it wil give us errors*/
numbers.forEach((item) => {
  if (item >= 0) {
    numberAboveZero.push(item);
  }
});

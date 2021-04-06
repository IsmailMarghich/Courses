/*tuples is a data structure similar to arrays and object that hold values, but the order of a tuple cant be changed*/
/*this is handy when we want to make sure the order of a data structure stays the same, e.g sugar amount first*/
/*a normal object*/
const drink = {
  color: "brown",
  carbonated: true,
  sugar: 40,
};
/*^ we can freely change the values and order of values in this object*/
/*we can add typing for the order of an array, effectively becoming a tuple*/
const pepsi: [string, boolean, number] = ["brown", true, 40];
/*repeating the above tuple definition can become annoying, so we can make our own type instead*/
type Drink = [string, boolean, number];
/*we can now keep using our own type to turn arrays into tuples, but we can use our own types for everything!*/
const sprite: Drink = ["clear", true, 60];
const tea: Drink = ["green", false, 0];
/*a use case for tuples could be, using a tuple to store data from a CSV, in a CSV file order matters a lot*/
/*however there isn't too many other use cases for tuples but it is still a way to showcase user made types*/

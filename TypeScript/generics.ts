/*not generic*/
const addOne = (a: number): number => {
  return a + 1;
};
/*lets say we want this function to add more to the argument*/
const addTwo = (a: number): number => {
  return a + 2;
};
/*this is silly and takes a while, we can pass arguments to solve this*/

const add = (a: number, b: number): number => {
  return a + b;
};
/*for classes we can do the same with generics, take the example below*/
class HoldNumber {
  data: number;
}
class HoldString {
  data: string;
}
const holdNumber = new HoldNumber();
holdNumber.data = 123;
const holdString = new HoldString();
holdString.data = "123";
/*we have to constantly make new classes if we want data to be different, this is a problem*/
/*we can add a type argument with <>*/
class HoldAnything<TypeOfData> {
  data: TypeOfData;
}
/*now the property of the class can hold any type that we pass to it*/
const holdBool = new HoldAnything<boolean>();
/*pass boolean type as argument, now data is of type boolean*/
holdBool.data = true;

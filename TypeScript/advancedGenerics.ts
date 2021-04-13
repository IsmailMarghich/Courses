/*generic classes*/
/*lets say we have 2 classes that are identical in nature, but with different types*/
class ArrayOfNumbers {
  constructor(public collection: number[]) {}
  get(index: number): number {
    return this.collection[index];
  }
}
class ArrayOfStrings {
  constructor(public collection: string[]) {}
  get(index: number): string {
    return this.collection[index];
  }
}
/*with generics, we can make a universal array*/
class GenericArray<T> {
  constructor(public collection: T[]) {}
  get(index: number): T {
    return this.collection[index];
  }
}

const genericArray = new GenericArray<boolean>([false, true, false]);
console.log(genericArray.get(0));

/*generic functions, again we see that these are very similar*/
function printString(arr: string[]): void {
  arr.forEach((item) => {
    console.log(item);
  });
}
function printNumbers(arr: number[]): void {
  arr.forEach((item) => {
    console.log(item);
  });
}
/*generic function*/
function genericPrint<T>(arr: T[]): void {
  arr.forEach((item) => {
    console.log(item);
  });
}
genericPrint<string>(["1", "2", "3"]);
/*we don't have to specify the type argument ourselves, typescript can figure this out by itself too*/
genericPrint([4, 5, 6]);
/*but ideally we want to do this, since typescript isn't always able to guess the type correctly*/

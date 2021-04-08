import { Sorter } from "./Sorter";
export class NumbersCollection extends Sorter {
  constructor(public data: number[]) {
    super();
  }
  get length(): number {
    /*get allows us to use the length as a variable*/
    return this.data.length;
  }
  /*this function will return true or false depending on whether we need to swap the numbers*/
  compare(leftIndex: number, rightIndex: number): boolean {
    return this.data[leftIndex] > this.data[rightIndex];
  }
  swap(leftIndex: number, rightIndex: number): void {
    /*if left element is bigger than right element, swap*/
    const leftHand = this.data[leftIndex];
    this.data[leftIndex] = this.data[rightIndex];
    this.data[rightIndex] = leftHand;
  }
}
const collection = new NumbersCollection([1, 2, 3]);
console.log(collection.length);

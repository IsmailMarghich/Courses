/*our class for a string that can be sorted*/
import { Sorter } from "./Sorter";
export class CharacterCollection extends Sorter {
  constructor(public data: string) {
    super();
  }
  get length(): number {
    return this.data.length;
  }
  compare(leftIndex: number, rightIndex: number): boolean {
    return (
      /*we can sort strings just like numbers, but we need to use lowercase because Z > a*/
      this.data[leftIndex].toLocaleLowerCase() >
      this.data[rightIndex].toLocaleLowerCase()
    );
  }
  swap(leftIndex: number, rightIndex: number): void {
    /*we cant directly change strings so we separate the string into an array of characters*/
    const characters = this.data.split("");

    const leftHand = characters[leftIndex];
    characters[leftIndex] = characters[rightIndex];
    characters[rightIndex] = leftHand;

    this.data = characters.join(
      ""
    ); /*turn the character array back into a string*/
  }
}

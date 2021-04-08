/*in this project we will make a program than can sort lots of different datastructures using bubble sort
 * by using typescript classes and interfaces we want to be able to sort arrays, strings and linked lists*/
/*with this interface we will make sure that the classes we pass to our sorter are able to be sorted properly*/
interface Sortable {
  length: number;
  compare(leftIndex: number, rightIndex: number): boolean;
  swap(leftIndex: number, rightIndex: number): void;
}
/*we can use abstract classes instead to pass down methods before they are implemented, abstract classes cannot be initialized, they are blueprints
 * this way we can use the sorter within the collection classes rather than having to make sort objects in index.ts*/
export abstract class Sorter {
  abstract compare(leftIndex: number, rightIndex: number): boolean;
  abstract swap(leftIndex: number, rightIndex: number): void;
  abstract length: number;
  sort(): void {
    const { length } = this; /*get the length of array*/

    for (let i = 0; i < length; i++) {
      for (let j = 0; j < length - i - 1; j++) {
        if (this.compare(j, j + 1)) {
          this.swap(j, j + 1);
        }
      }
    }
  }
}

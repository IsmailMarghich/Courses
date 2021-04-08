/*a linked list is a data structure that consists of nodes that contain a value and a reference to the next node
 * a linked list has a head which points to the first node and the final node points to null*/
import { Sorter } from "./Sorter";
class LNode {
  next: LNode | null = null;
  constructor(public data: number) {}
}

export class LinkedList extends Sorter {
  head: LNode | null = null;

  add(data: number): void {
    const node = new LNode(data);

    if (!this.head) {
      /*if we dont have a head, we create one*/
      this.head = node;
      return;
    }
    /*if we do have a head, we wanna go to the end of the linked list by checking the .next property of a node*/
    let tail = this.head;
    while (tail.next) {
      tail = tail.next;
    }
    /*when we find the tail, we add our node as the new tail*/
    tail.next = node;
  }
  get length(): number {
    /*this will get the length of our linked list*/
    if (!this.head) {
      return 0;
    }

    let length = 1;
    let node = this.head; /*attack to first node*/
    while (node.next) {
      /*iterate until the end and increment length variable*/
      length++;
      node = node.next;
    }
    return length;
  }
  at(index: number): LNode {
    /*function to find a node at index*/
    if (!this.head) {
      throw new Error("index out of bounds");
    }
    let counter = 0;
    let node: LNode = this.head;
    while (node) {
      /*iterate over list until our indexes match*/
      if (counter === index) {
        return node;
      }
      counter++;
      node = node.next;
    }
    throw new Error("index out of bounds");
  }

  compare(leftIndex: number, rightIndex: number): boolean {
    if (!this.head) {
      throw new Error("List is empty");
    }
    return (
      this.at(leftIndex).data > this.at(rightIndex).data
    ); /*compare the data of left and right using our at method*/
  }
  swap(leftIndex: number, rightIndex: number): void {
    /*find left and right nodes*/
    const leftNode = this.at(leftIndex);
    const rightNode = this.at(rightIndex);
    /*swap nodes values*/
    const leftHand = leftNode.data;
    leftNode.data = rightNode.data;
    rightNode.data = leftHand;
  }
  print(): void {
    if (!this.head) {
      return;
    }
    let node = this.head;
    while (node) {
      /*iterate over list as long as we have nodes and print node data*/
      console.log(node.data);
      node = node.next;
    }
  }
}

/*this program will sort different types of datastructures using a Sorter abstract class and by adding methods to datastructures*/
import { NumbersCollection } from "./NumbersCollections";
import { CharacterCollection } from "./CharactersCollections";
import { LinkedList } from "./LinkedLists";

const characterCollection = new CharacterCollection("greetings");
const numbersCollection = new NumbersCollection([10, 3, -5, 20, 99, 900]);
const linkedList = new LinkedList();

linkedList.add(500);
linkedList.add(2);
linkedList.add(-1);
linkedList.add(33);
linkedList.add(79);

characterCollection.sort();
numbersCollection.sort();
linkedList.sort();

console.log(characterCollection.data);
console.log(numbersCollection.data);
linkedList.print();

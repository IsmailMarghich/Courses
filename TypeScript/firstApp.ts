/*In this file we will fetch some data from an API with Axios, and we use an interface and type annotation to check for errors*/
/*This is 2 examples of why we wanna use TypeScript*/
import axios from "axios";

interface Todo {
  /*what we expect to have in a variable that uses the interface Todo*/
  id: number;
  title: string;
  completed: boolean;
}

const url: string = "http://jsonplaceholder.typicode.com/todos/1";
axios.get(url).then((response) => {
  const todo = response.data as Todo; /**/
  console.log(
    "ID:",
    todo.id
  ); /*if we make a typo or mistake, Ts will tell us it does not match our todo interface*/
  console.log("Title:", todo.title);
  console.log("Completed:", todo.completed);
  logTodo(todo.id, todo.title, todo.completed);
});

const logTodo = (id: number, title: string, completed: boolean) => {
  /*use type annotation to ensure the right arguments are passed*/
  console.log(id, title, completed);
};

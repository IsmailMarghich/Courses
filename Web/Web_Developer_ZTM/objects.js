/*objects are a collection of variables and functions, they are similar to classes in other languages*/
let user = {
    name: "Jean", /*our collection of variables of this object*/
    age: 20,
    hobby: "Martial arts",
    isMarried: false,
    introduce: function (){  /*a function that can only be used on the object*/
        console.log("My name is ", user.name); /*this will print out the data of the user*/
        console.log("I am ", user.age, "years old");
        console.log("My hobby is ", user.hobby);
        if (this.isMarried){ /*if the user is married, log. this refers to this object*/
            console.log("I am married")
        }else { /*otherwise we log he is not married*/
            console.log("I am not married")
        }
    }
};
console.log(user.age);
user.introduce();
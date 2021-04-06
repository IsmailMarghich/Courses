class Vehicle {
  drive(): void {
    /*class methods are public by default and can be called by anyone*/
    console.log("vroom vroom");
  }
  protected honk(): void {
    /*protected methods can be called within the class and subclasses of this class*/
    console.log("beep");
  }
  private secret(): string {
    /*private methods can be only be called within the function*/
    return "im from a private method";
  }
  public useSecret(): void {
    /*this method can use the private method above*/
    console.log(this.secret());
  }
}

const vehicle = new Vehicle();
vehicle.drive();
vehicle.useSecret();
/*classes can inherit variables and methods from other classes using extend*/

class Truck extends Vehicle {
  color: string;
  /*we can overload methods that are inherited*/
  constructor(color: string) {
    /*we can add typing to class constructors too*/
    super(); /*call super because this is a child class*/
    this.color = color; /*set color of the car, if we add public before color we dont have to initialize with this.*/
  }
  honk(): void {
    console.log("boop");
  }
  myColor(): string {
    return this.color;
  }
}
/*truck can use all methods from vehicle now*/
const truck = new Truck("orange");
truck.drive();
truck.honk(); /*this used the overloaded method from Truck class*/
console.log(truck.myColor());

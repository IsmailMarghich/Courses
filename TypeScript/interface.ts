/*an interface creates a type, an describes the the property names and types of values of an object
 * basically, custom type + names and types of variables*/

const oldCar = {
  name: "civic",
  year: 2000,
  broken: true,
  summary(): string {
    return `name: ${this.name}`;
  },
};
/*adding type annotations for objects are long, confusing and hard to read, interfaces can solve this*/
const printCar = (vehicle: { name: string; year: number; broken: boolean }) => {
  console.log(vehicle.name, vehicle.year, vehicle.broken);
};
printCar(oldCar);
/*our interface for a vehicle*/
interface Vehicle {
  name: string;
  year: number;
  broken: boolean;
  summary(): string;
}
/*now its much more readable, and re-usable*/
const printVehicle = (vehicle: Vehicle) => {
  console.log(vehicle.name, vehicle.year, vehicle.broken);
};
printVehicle(oldCar);
/*we can re-use even more code with interfaces when we have more objects*/
/*the object doesnt have to be completely the same as the interface, just has to at least have all the interface values*/
const myVehicle = {
  name: "opel",
  year: 2003,
  broken: false,
  extraVariable: "this does not have to be in the interface for it to pass",
  summary(): string {
    return `name: ${this.name}`;
  },
};
printVehicle(
  myVehicle
); /*satisfies the interface, no need to do extra checking our own*/

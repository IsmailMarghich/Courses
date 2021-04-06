/*typed arrays are arrays where each element is a consistent type of value
 * usually typescript will be able to tell the types of an array by looking at its elements, but not when the array is emtpy*/
/*these arrays will be automatically typed by typescript*/
const carBrand = ["ferrari", "lamborghini", "opel"];
const dates = [new Date(), new Date()];
/*when extracting from a typed array, ts will assign types*/
const myCar = carBrand[0];
/*it will prevent us from adding incompatible values to array*/
/*carBrand.push(100); this will error because its a number being pushed to a string array*/
/*when using functions like map, reduce or for each, ts will also add types automatically*/
carBrand.forEach((car) => {
  return car;
});
/*when there is multiple types in an array, ts will automatically add flexible typing*/
const importantDates: (Date | string)[] = [
  new Date(),
  "6-4-2021",
]; /*with | we can add new types*/

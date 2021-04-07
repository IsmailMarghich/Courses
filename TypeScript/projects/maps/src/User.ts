import faker from "faker"; /*we are going to be using the faker module to randomly generate data for our app*/
export class User {
  /*our user class that gets constructed using randomized data from faker API*/
  name: string;
  location: {
    lat: number;
    lng: number;
  };
  constructor() {
    this.name = faker.name.firstName();
    this.location = {
      /*generate lat and lng using faker, convert to float since they return strings*/
      lat: parseFloat(faker.address.latitude()),
      lng: parseFloat(faker.address.longitude()),
    };
  }
  markerContent(): string {
    return `
    <div>
    <h1>${this.name}</h1>
    </div>`;
  }
}

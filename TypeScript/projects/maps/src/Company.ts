import faker from "faker";

export class Company {
  companyName: string;
  catchPhrase: string;
  location: {
    lat: number;
    lng: number;
  };
  constructor() {
    this.companyName = faker.company.companyName();
    this.catchPhrase = faker.company.catchPhrase();
    this.location = {
      /*generate lat and lng using faker, convert to float since they return strings*/
      lat: parseFloat(faker.address.latitude()),
      lng: parseFloat(faker.address.longitude()),
    };
  }
  markerContent(): string {
    return `
    <div>
    <h1>${this.companyName}</h1>
    <h3>${this.catchPhrase} </h3>
    </div>`;
  }
}

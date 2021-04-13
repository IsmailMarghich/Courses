import fs from "fs";

export abstract class CsvFileReader<T> {
  data: T[] = [];

  constructor(public filename: string) {}
  abstract mapRow(row: string[]): T;
  read(): void {
    this.data = fs
      .readFileSync(this.filename, {
        encoding: "utf-8",
      })
      .split("\n") /*split the array into lines per match*/
      .map((row: string): string[] => {
        /*then we split each piece of data per line*/
        return row.split(
          ","
        ); /*now we return an array where each element is an array of each piece of data*/
      })
      /*converting to proper format*/
      .map(this.mapRow);
  }
}

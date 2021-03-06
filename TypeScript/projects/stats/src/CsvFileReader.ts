import fs from "fs";

export class CsvFileReader {
  data: string[][] = [];

  constructor(public filename: string) {}
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
      });
  }
}

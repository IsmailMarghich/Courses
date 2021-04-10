import fs from "fs";
import { dateStringToDate } from "./utils";
import { MatchResult } from "./MatchResult";

type MatchData = [Date, string, string, number, number, MatchResult, string];

export class CsvFileReader {
  data: MatchData[] = [];
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
      })
      /*converting to proper format*/
      .map(
        (row: string[]): MatchData => {
          return [
            dateStringToDate(row[0]),
            row[1],
            row[2],
            parseInt(row[3]),
            parseInt(row[4]),
            row[5] as MatchResult /*H, A or D*/,
            row[6],
          ];
        }
      );
  }
}

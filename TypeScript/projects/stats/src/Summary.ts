/*in this file we will add functionality where the user can see a summary of the csv file*/
import { MatchData } from "./MatchData";

export interface Analyzer {
  run(matches: MatchData[]): string;
}

export interface OutputTarget {
  print(report: string): void;
}

export class Summary {
  constructor(public analyzer: Analyzer, public outputTarget: OutputTarget) {}

  buildPrintReport(matches: MatchData[]): void {
    const output = this.analyzer.run(matches); /*analyze the data*/
    this.outputTarget.print(output); /*print the data to the user*/
  }
}

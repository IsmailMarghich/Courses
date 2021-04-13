import { OutputTarget } from "../Summary";
import { MatchData } from "../MatchData";

export class ConsoleReport implements OutputTarget {
  print(report: string): void {
    console.log(report);
  }
}

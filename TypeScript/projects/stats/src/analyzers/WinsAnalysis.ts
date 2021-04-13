import { Analyzer } from "../Summary";
import { MatchData } from "../MatchData";
import { MatchResult } from "../MatchResult";

export class WinsAnalysis implements Analyzer {
  constructor(public team: string) {}
  run(matches: MatchData[]): string {
    let wins = 0;
    for (let match of matches) {
      /*iterate over each row*/
      if (match[1] === this.team && match[5] === MatchResult.HomeWin) {
        /*when man united wins as home team*/
        wins++;
      } else if (match[2] === this.team && match[5] === MatchResult.AwayWin) {
        /*when man united wins as away team*/
        wins++;
      }
    }
    return `Team ${this.team} won ${wins} games`;
  }
}

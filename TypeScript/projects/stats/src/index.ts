/*in this file we will load, parse, analyze and report soccer match data using various libraries*/
import { CsvFileReader } from "./CsvFileReader";
import { MatchResult } from "./MatchResult";
const reader = new CsvFileReader("src/football.csv");

reader.read();

/*we can use enums to count wins of teams and show to other developers that these values are related*/

let manUnitedWins = 0;
for (let match of reader.data) {
  /*iterate over each row*/
  if (match[1] === "Man United" && match[5] === MatchResult.HomeWin) {
    /*when man united wins as home team*/
    manUnitedWins++;
  } else if (match[2] === "Man United" && match[5] === MatchResult.AwayWin) {
    /*when man united wins as away team*/
    manUnitedWins++;
  }
}
console.log(`Manchester united won ${manUnitedWins} games`);

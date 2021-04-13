/*in this file we will load, parse, analyze and report soccer match data using various libraries*/
import { MatchReader } from "./MatchReader";
import { CsvFileReader } from "./CsvFileReader";
import { ConsoleReport } from "./reportTargets/ConsoleReport";
import { WinsAnalysis } from "./analyzers/WinsAnalysis";
import { Summary } from "./Summary";
import { HtmlReport } from "./reportTargets/HtmlReport";
/*create an object that satisfies DataReader interface*/
const csvFileReader = new CsvFileReader("src/football.csv");
/*create an instance of match reader and pass something that satisfies DataReader interface*/
const matchReader = new MatchReader(csvFileReader);
matchReader.load();

const winAnalysis = new WinsAnalysis("Wolves");

const summarize = new Summary(winAnalysis, new ConsoleReport());
summarize.buildPrintReport(matchReader.matches);
const summarizeHtml = new Summary(winAnalysis, new HtmlReport());
summarizeHtml.buildPrintReport(matchReader.matches);

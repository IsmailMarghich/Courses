import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

/*Interface that describes the response of the wikimedia api response, this will be used for error checking*/
interface WikipediaResponse {
  query: {
    search: {
      title: string;
      snippet: string;
      pageid: number;
    }[];
  };
}
/*if we get the wrong data or something else bad happens, typescript will refer to the interface, rather than compiled js files.
 * which are not useful to us.*/
/*it will also allow us to catch errors in our app.component.ts file, where we access the response.*/
@Injectable({
  providedIn: 'root',
})
export class WikipediaService {
  url =
    'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=space&utf8=&format=json';
  constructor(private httpclient: HttpClient) {}

  search(term: string) {
    return this.httpclient.get<WikipediaResponse>(
      'https://en.wikipedia.org/w/api.php',
      {
        params: {
          action: 'query',
          format: 'json',
          list: 'search',
          utf8: '1',
          srsearch: term,
          origin: '*',
        },
      }
    );
  }
}

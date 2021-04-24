import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class WikipediaService {
  url =
    'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=space&utf8=&format=json';
  constructor(private httpclient: HttpClient) {}

  search(term: string) {
    return this.httpclient.get('https://en.wikipedia.org/w/api.php', {
      params: {
        action: 'query',
        format: 'json',
        list: 'search',
        utf8: '1',
        srsearch: term,
        origin: '*',
      },
    });
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface apiResponse {
  urls: {
    regular: string;
  };
}

@Injectable({
  providedIn: 'root',
})
export class PhotosService {
  apiKey = 'AEY0Xzs0_wqYVDaKnFY4EnpU1mnxRx1cVEE6wZY2gJc';
  url = 'https://api.unsplash.com/photos/random';

  constructor(private http: HttpClient) {}

  getPhoto() {
    return this.http.get<apiResponse>(this.url, {
      headers: {
        Authorization: `Client-ID ${this.apiKey}`,
      },
    });
  }
}

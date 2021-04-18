import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  posts = [
    {
      title: 'Neat Tree',
      imageUrl: 'assets/tree.jpg',
      username: 'Nature',
      content: 'I saw this neat tree while on my walk.',
    },
    {
      title: 'Snowy mountain',
      imageUrl: 'assets/mountain.jpg',
      username: 'Mountain_Climber',
      content: 'This mountain is huge!',
    },
    {
      title: 'Mountain Biking',
      imageUrl: 'assets/biking.jpg',
      username: 'biker1337',
      content: 'Went on a lovely bike ride today.',
    },
  ];
}

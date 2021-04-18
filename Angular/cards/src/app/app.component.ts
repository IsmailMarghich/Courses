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
      imageUrl:
        'https://www.gardeningknowhow.com/wp-content/uploads/2010/09/tree-with-hole.png',
      username: '@Nature',
      content: 'I saw this neat tree while on my walk.',
    },
    {
      title: 'Snowy mountain',
      imageUrl:
        'https://desenio.nl/bilder/artiklar/zoom/11634_2.jpg?imgwidth=435&qt=',
      username: '@Mountain_Climber',
      content: 'This mountain is huge!',
    },
    {
      title: 'Mountain Biking',
      imageUrl:
        'https://s14761.pcdn.co/wp-content/uploads/2020/09/Propain-spindrift-cf-2021-enduro-test-review36-810x551.jpg',
      username: '@biker1337',
      content: 'Went on a lovely bike ride today.',
    },
  ];
}

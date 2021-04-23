import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mods-home',
  templateUrl: './mods-home.component.html',
  styleUrls: ['./mods-home.component.css'],
})
export class ModsHomeComponent implements OnInit {
  modalOpen = false;
  items = [
    { title: 'Why are we using Angular?', content: 'Because it is great' },
    { title: 'Will you get a job?', content: 'Hopefully' },
    {
      title: 'Am I having fun writing all these placeholder texts?',
      content: 'Yes',
    },
  ];
  constructor() {}

  ngOnInit(): void {}
  onClick() {
    this.modalOpen = !this.modalOpen;
  }
}

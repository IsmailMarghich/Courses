import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-collections-home',
  templateUrl: './collections-home.component.html',
  styleUrls: ['./collections-home.component.css'],
})
export class CollectionsHomeComponent implements OnInit {
  data = [
    { name: 'James', age: 24, job: 'Designer' },
    { name: 'John', age: 32, job: 'Senior Developer' },
    { name: 'Jay', age: 19, job: 'Junior Developer' },
  ];
  /*we use headers so we dont mess up our table when we add more values to data array*/
  headers = [
    { key: 'name', label: 'Name' },
    { key: 'age', label: 'Age' },
    { key: 'job', label: 'Job' },
  ];
  constructor() {}

  ngOnInit(): void {}
}

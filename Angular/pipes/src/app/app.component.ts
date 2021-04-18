import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  name: string;
  date: string;
  amount: number;
  height: number;
  miles: number;

  onMilesChange(e) {
    this.miles = parseFloat(e.target.value);
  }

  onHeightChange(e) {
    this.height = parseFloat(e.target.value);
  }

  onNameChange(e) {
    this.name = e.target.value;
  }
  onDateChange(e) {
    this.date = e.target.value;
  }

  onAmountChange(e) {
    this.amount = parseFloat(e.target.value);
  }
}

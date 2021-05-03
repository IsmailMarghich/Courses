import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MathValidators } from '../math-validators';

@Component({
  selector: 'app-equation',
  templateUrl: './equation.component.html',
  styleUrls: ['./equation.component.css'],
})
export class EquationComponent implements OnInit {
  mathForm = new FormGroup(
    {
      a: new FormControl(this.randomNumber()) /*first & second number*/,
      b: new FormControl(this.randomNumber()),
      answer: new FormControl('') /*user input*/,
    },
    [MathValidators.addition('answer', 'a', 'b')]
  );
  constructor() {}

  get a() {
    /*getter methods so the program can use this to refer to the variables easily*/
    return this.mathForm.value.a;
  }
  get b() {
    return this.mathForm.value.b;
  }

  ngOnInit(): void {
    this.mathForm.statusChanges.subscribe((value) => {
      if (value === 'INVALID') {
        return;
      }
      /*if user input is valid, we reset our form*/
      this.mathForm.setValue({
        a: this.randomNumber(),
        b: this.randomNumber(),
        answer: '',
      });
    });
  }

  randomNumber() {
    return Math.floor(Math.random() * 10);
  }
}

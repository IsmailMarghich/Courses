import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MathValidators } from '../math-validators';
import { delay, filter, scan } from 'rxjs/operators';

@Component({
  selector: 'app-equation',
  templateUrl: './equation.component.html',
  styleUrls: ['./equation.component.css'],
})
export class EquationComponent implements OnInit {
  secondsPerSolution = 0;
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
    this.mathForm.statusChanges
      .pipe(
        /*only reset form when the user enters the correct number*/
        filter((value) => value === 'VALID'),
        delay(100) /*delay resetting form so user can see its answer*/,
        scan(
          (acc) => {
            return {
              numberSolved: acc.numberSolved + 1,
              startTime: acc.startTime,
            };
          },
          { numberSolved: 0, startTime: new Date() }
        )
      )
      .subscribe(({ numberSolved, startTime }) => {
        this.secondsPerSolution =
          (new Date().getTime() - startTime.getTime()) / numberSolved / 1000;

        /*if user input is valid (correct solution), we reset our form*/
        this.mathForm.patchValue({
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

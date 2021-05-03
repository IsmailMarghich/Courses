import { AbstractControl } from '@angular/forms';

export class MathValidators {
  /*this class contains validators for our math game, the methods are static, so we don't need to create an instance of the class
   * to use the validators*/
  static addition(target: string, sourceOne: string, sourceTwo: string) {
    return (form: AbstractControl) => {
      const sum = form.value[target];
      const firstNumber = form.value[sourceOne];
      const secondNumber = form.value[sourceTwo];

      if (firstNumber + secondNumber === parseInt(sum)) {
        return null;
      }
      return { addition: true };
    };
  }

  static subtraction() {}
}

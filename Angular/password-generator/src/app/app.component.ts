import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  includeLetters = false;
  includeNumbers = false;
  includeSymbols = false;
  passwordLength = 0;
  password = '';

  useLetters() {
    this.includeLetters = !this.includeLetters;
  }
  useNumbers() {
    this.includeNumbers = !this.includeNumbers;
  }
  useSymbols() {
    this.includeSymbols = !this.includeSymbols;
  }

  changeLength(e) {
    this.passwordLength = parseInt(e.target.value);
  }
  onButtonClick() {
    const numbers = '1234567890';
    const letters = 'abcdefghijklmnopqrstuvwxz';
    const symbols = '!@#$%^&*()';

    let validChars = '';
    if (this.includeLetters) {
      validChars += letters;
    }
    if (this.includeNumbers) {
      validChars += numbers;
    }
    if (this.includeSymbols) {
      validChars += symbols;
    }
    let generatedPassword = '';
    for (let i = 0; i < this.passwordLength; i++) {
      const index = Math.floor(Math.random() * validChars.length);
      generatedPassword += validChars[index];
    }
    this.password = generatedPassword;
  }
}

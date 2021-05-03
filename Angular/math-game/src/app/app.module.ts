import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {ReactiveFormsModule} from "@angular/forms";
import { AppComponent } from './app.component';
import { EquationComponent } from './equation/equation.component';
import { AnswerHelpDirective } from './answer-help.directive';

@NgModule({
  declarations: [
    AppComponent,
    EquationComponent,
    AnswerHelpDirective
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
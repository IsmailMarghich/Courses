import { Directive, ElementRef, Input } from '@angular/core';
/*in this file we will make our own custom attribute directive to replace the nglcass directive provided by angular*/
@Directive({
  selector: '[appCustom]',
})
export class CustomDirective {
  constructor(private element: ElementRef) {}

  /*we get an object with classnames as keys and expressions as values*/
  @Input('appCustom') set classNames(classObject: any) {
    for (let key in classObject) {
      /*for every class name*/
      if (classObject[key]) {
        /*we check whether expression is true or false, and depending on that we add class to the element*/
        this.element.nativeElement.classList.add(key);
      } else {
        this.element.nativeElement.classList.remove(key);
      }
    }
  }
}

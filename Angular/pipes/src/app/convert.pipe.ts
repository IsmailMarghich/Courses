import { Pipe, PipeTransform } from '@angular/core';
/*we can make our own pipes in angular, the purpose of this one is to convert from miles to meters and kilometers*/
@Pipe({
  name: 'convert',
})
export class ConvertPipe implements PipeTransform {
  transform(value: number, unit: string): any {
    if (!value) {
      return '';
    }
    switch (unit) {
      case 'km':
        return value * 1.609344;
      case 'm':
        return value * 1.609344 * 1000;
      default:
        /*we can add our own errors to our pipe*/
        throw new Error('target unit is not supported');
    }
  }
}

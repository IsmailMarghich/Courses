import { FormControl } from '@angular/forms';
/*this will check our expiration date field in our credit card app*/
export class DateFormControl extends FormControl {
  setValue(value: string | null, options: any) {
    if (!value) {
      /*if no value is passed, reset string*/
      super.setValue('', { ...options, emitModelToViewChange: true });
      return;
    }

    if (value.match(/[^0-9|\/]/gi)) {
      super.setValue(this.value, { ...options, emitModelToViewChange: true });
      return;
    }

    if (value.length > 5) {
      super.setValue(this.value, { ...options, emitModelToViewChange: true });
      return;
    }

    if (value.length == 2 && this.value.length === 3) {
      super.setValue(value, { ...options, emitModelToViewChange: true });
      return;
    }

    if (value.length === 2) {
      super.setValue(value + '/', { ...options, emitModelToViewChange: true });
      return;
    }
    super.setValue(value, { ...options, emitModelToViewChange: true });
  }
}

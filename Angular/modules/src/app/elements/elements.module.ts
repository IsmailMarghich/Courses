import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ElementsRoutingModule } from './elements-routing.module';
import { ElementsHomeComponent } from './elements-home/elements-home.component';

@NgModule({
  declarations: [ElementsHomeComponent],
  exports: [ElementsHomeComponent],
  imports: [CommonModule, ElementsRoutingModule],
})
export class ElementsModule {}

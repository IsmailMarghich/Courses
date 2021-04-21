import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CollectionsRoutingModule } from './collections-routing.module';
import { CollectionsHomeComponent } from './collections-home/collections-home.component';

@NgModule({
  declarations: [CollectionsHomeComponent],
  exports: [],
  imports: [CommonModule, CollectionsRoutingModule],
})
export class CollectionsModule {}

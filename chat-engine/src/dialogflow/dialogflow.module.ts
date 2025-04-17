import { Module } from '@nestjs/common';
import { DialogflowService } from './dialogflow.service';

@Module({
  providers: [DialogflowService]
})
export class DialogflowModule {}

import { Module } from '@nestjs/common';
import { DialogflowModule } from './dialogflow/dialogflow.module';
import { ConfigModule } from '@app/config';
import { DatabaseModule } from '@app/database';
import { FileModule } from './file/file.module';

@Module({
  imports: [
    ConfigModule, 
    DatabaseModule, 
    DialogflowModule, 
    // KafkaModule, 
    FileModule
  ],
})
export class AppModule {}

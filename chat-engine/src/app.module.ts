import { Module } from '@nestjs/common';
import { DialogflowModule } from './dialogflow/dialogflow.module';
import { ConfigModule } from '@app/config';
import { DatabaseModule } from '@app/database';
import { KafkaModule } from './kafka/kafka.module';
import { AppController } from './app.controller';
import { FileModule } from './file/file.module';

@Module({
  imports: [ConfigModule, DatabaseModule, DialogflowModule, KafkaModule, FileModule],
  controllers: [AppController],
})
export class AppModule {}

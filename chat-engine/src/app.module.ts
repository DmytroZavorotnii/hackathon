import { Module } from '@nestjs/common';
import { DialogflowModule } from './dialogflow/dialogflow.module';
import { ConfigModule } from '@app/config';
import { DatabaseModule } from '@app/database';
import { KafkaModule } from './kafka/kafka.module';
import { AppController } from './app.controller';

@Module({
  imports: [ConfigModule, DatabaseModule, DialogflowModule, KafkaModule],
  controllers: [AppController],
})
export class AppModule {}

import { Module } from '@nestjs/common';
import { KafkaService } from './kafka.service';
import { KafkaController } from './kafka.controller';
import { ClientsModule } from '@nestjs/microservices';
import { KafkaClientNames, kafkaConfig, KafkaGroupNames, KafkaServiceNames } from '@app/config';

@Module({
  imports: [
    ClientsModule.register([
      kafkaConfig(
        KafkaServiceNames.CHAT_ENGINE,
        KafkaClientNames.CHAT_ENGINE,
        KafkaGroupNames.CHAT_ENGINE,
      ),
  ]),],
  providers: [KafkaService],
  controllers: [KafkaController],
  exports: [KafkaService],
})
export class KafkaModule {}

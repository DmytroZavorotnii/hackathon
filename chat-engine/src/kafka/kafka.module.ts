import { Module } from '@nestjs/common';
import { KafkaService } from './kafka.service';
import { KafkaController } from './kafka.controller';
import { ClientsModule } from '@nestjs/microservices';
import { KafkaClientNames, kafkaConfig, KafkaGroupNames, KafkaServiceNames } from '@app/config';
import { ProducerService } from './producer.service';
import { DialogflowModule } from 'src/dialogflow/dialogflow.module';
import { FileModule } from 'src/file/file.module';

@Module({
  imports: [
    DialogflowModule,
    FileModule,
    ClientsModule.register([
        kafkaConfig(
          KafkaServiceNames.CHAT_ENGINE,
          KafkaClientNames.CHAT_ENGINE,
          KafkaGroupNames.CHAT_ENGINE,
        ),
    ]),
  ],
  providers: [KafkaService, ProducerService],
  controllers: [KafkaController],
  exports: [KafkaService],
})
export class KafkaModule {}


import { Injectable, Logger } from '@nestjs/common';
import { ProducerService } from './producer.service';
import { DialogflowService } from 'src/dialogflow/dialogflow.service';
import { KafkaTopics } from '@app/config';

@Injectable()
export class KafkaService {
    private readonly logger = new Logger(KafkaService.name);

    constructor(
        private readonly producerService: ProducerService,
        private readonly dialogflowService: DialogflowService,
    ) {}

    async askDialogflow(query: string) {
        const response = await this.dialogflowService.ask(query)
        this.logger.debug(`Dialogflow response: ${response}`);
        return response;
    }

    async sendMessage(topic: KafkaTopics) {
        this.logger.debug('sendKafkaMessage');
        await this.producerService.sendMessage(topic);
    }

    emitMessage(topic: string) {
        this.producerService.emitMessage(topic);
    }
}

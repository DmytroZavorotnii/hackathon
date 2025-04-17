import { Controller, Get, Logger } from '@nestjs/common';
import { KafkaService } from './kafka/kafka.service';

@Controller()
export class AppController {
    private readonly logger = new Logger(AppController.name);

    constructor(private readonly producerService: KafkaService) {}

    @Get('send')
    sendKafkaMessage() {
        return this.producerService.sendMessage();
    }
}

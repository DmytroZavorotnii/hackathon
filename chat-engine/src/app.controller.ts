import { Body, Controller, Get, Logger, Post } from '@nestjs/common';
import { KafkaService } from './kafka/kafka.service';

@Controller('/api/v1/app')
export class AppController {
    private readonly logger = new Logger(AppController.name);

    constructor(private readonly kafkaService: KafkaService) {}

    @Get('send')
    sendKafkaMessage() {
        return this.kafkaService.sendMessage();
    }

    @Get('emit')
    emitKafkaMessage() {
        return this.kafkaService.emitMessage();
    }

    @Post('dialogflow')
    async aksDialogflow(@Body() body: { query: string }) {
        return {
            answer: await this.kafkaService.askDialogflow(body.query)
        }
    }

}

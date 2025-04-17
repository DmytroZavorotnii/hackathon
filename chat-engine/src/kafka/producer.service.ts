import { KafkaServiceNames } from "@app/config";
import { Inject, Injectable } from "@nestjs/common";
import { ClientKafka } from "@nestjs/microservices";

@Injectable()
export class ProducerService {
    constructor(@Inject(KafkaServiceNames.CHAT_ENGINE) private readonly client: ClientKafka) {}

    async onModuleInit() {
        this.client.subscribeToResponseOf('test-topic');
        await this.client.connect();
        console.log('Kafka connected ✅');
    }

    sendMessage() {
        return this.client.send('test-topic', {
            key: 'key1',
            value: JSON.stringify({ message: 'Hello from NestJS!' }),
            headers: {
                'custom-header': 'header-value',
            },
        });
    }

    emitMessage() {
        return this.client.emit('test-emit', {
            key: 'key1',
            value: JSON.stringify({ message: 'Emit from NestJS!' }),
            headers: {
                'custom-header': 'header-value',
            },
        });
    }
}
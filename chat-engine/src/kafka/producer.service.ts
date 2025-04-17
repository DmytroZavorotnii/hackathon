import { KafkaServiceNames, KafkaTopics } from "@app/config";
import { Inject, Injectable, Logger } from "@nestjs/common";
import { ClientKafka } from "@nestjs/microservices";

@Injectable()
export class ProducerService {
    private readonly logger = new Logger(ProducerService.name);

    constructor(@Inject(KafkaServiceNames.CHAT_ENGINE) private readonly client: ClientKafka) {}

    async onModuleInit() {
        this.client.subscribeToResponseOf('test-topic');
        this.client.subscribeToResponseOf('file.upload');
        this.client.subscribeToResponseOf(KafkaTopics.FILE_DELETE);
        this.client.subscribeToResponseOf(KafkaTopics.ASK_DIALOGFLOW);
        this.client.subscribeToResponseOf(KafkaTopics.FILE_ALL);
        this.client.subscribeToResponseOf(KafkaTopics.AVAILABLE_TOPICS);

        await this.client.connect();
        console.log('Kafka connected ✅');
    }

    async sendMessage(topic: KafkaTopics) {
        this.logger.debug('sendKafkaMessage', topic);
        return this.client.send('file.upload', 
            {
                key: 'key1',
                value: JSON.stringify({
                    "topic": "єВідновленняТест2",
                    "content": "Base64",
                    "filename": "file2.pdf"
                })
        });
    }

    emitMessage(topic: string) {
        this.logger.debug('emitKafkaMessage', topic);
        return this.client.emit(topic, {
            key: 'key1',
            value: JSON.stringify({
                "topic": "єВідновленняТест2",
                "content": "Base64",
                "filename": "file2.pdf"
            })
        });
    }
}
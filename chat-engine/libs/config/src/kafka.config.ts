import { EnvironmentEnums } from "@app/interfaces";
import { ClientProviderOptions, Transport } from "@nestjs/microservices";

const kafkaConfig = (name: string, clientId: string, groupId: string): ClientProviderOptions => {
    return {
        name: name,
        transport: Transport.KAFKA,
        options: {
            client: {
                clientId: clientId,
                brokers: process.env[EnvironmentEnums.KAFKA_BROKERS].split(','),
                connectionTimeout: 3000,
                authenticationTimeout: 3000,
                requestTimeout: 3000,
            },
            consumer: {
                groupId: groupId,
            }
        }
    }
}

enum KafkaServiceNames {
    CHAT_ENGINE = 'CHAT_ENGINE',
}

enum KafkaClientNames {
    CHAT_ENGINE = 'chat-engine',
}

enum KafkaGroupNames {
    CHAT_ENGINE = 'chat-engine-consumer',
}

enum KafkaTopics {
    TEST_TOPIC = 'test-topic',
    TEST_EMIT = 'test-emit',
    GET_SUMMARY = 'get.summary',
    AVAILABLE_TOPICS = 'available.topics',
    FILE_ALL = 'file.all',
    FILE_UPLOAD = 'file.upload',
    FILE_DELETE = 'file.delete',
    ASK_DIALOGFLOW = 'ask.dialogflow',
}

export { kafkaConfig, KafkaServiceNames, KafkaClientNames, KafkaGroupNames, KafkaTopics };
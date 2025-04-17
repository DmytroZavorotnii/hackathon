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

}

export { kafkaConfig, KafkaServiceNames, KafkaClientNames, KafkaGroupNames, KafkaTopics };
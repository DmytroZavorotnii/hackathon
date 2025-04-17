import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Logger } from '@nestjs/common';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';
import { KafkaClientNames,  KafkaGroupNames } from '@app/config';
import { EnvironmentEnums } from '@app/interfaces';
import { ConfigService } from '@nestjs/config';

async function bootstrap() {
    const httpApp = await NestFactory.create(AppModule);
    const configService = httpApp.get(ConfigService);
    const logger = new Logger("NestExpressApplication")

    const SERVICE_PORT = configService.get<number>(EnvironmentEnums.SERVICE_PORT, 8001);

    const kafkaApp = await NestFactory.createMicroservice<MicroserviceOptions>(AppModule, 
        {
            transport: Transport.KAFKA,
            options: {
                client: {
                    clientId: KafkaClientNames.CHAT_ENGINE,
                    brokers: process.env[EnvironmentEnums.KAFKA_BROKERS].split(','),
                    connectionTimeout: 3000,
                    authenticationTimeout: 3000,
                    requestTimeout: 3000,
                },
                consumer: {
                    groupId: KafkaGroupNames.CHAT_ENGINE,
                }
            }
        }
    );

    await httpApp.listen(SERVICE_PORT, () => {logger.log(`HTTP server is running on port ${SERVICE_PORT} ✅`);});
    await kafkaApp.listen();
    logger.log("Server started ✅")
}
bootstrap();

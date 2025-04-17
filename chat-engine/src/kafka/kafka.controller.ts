import { KafkaTopics } from '@app/config';
import { IAllFilesMessage, IAskDialogflowMessage, IUploadFileMessage } from '@app/interfaces';
import { Controller, Logger } from '@nestjs/common';
import { MessagePattern,  Payload } from '@nestjs/microservices';
import { KafkaService } from './kafka.service';
import { FileService } from 'src/file/file.service';

@Controller()
export class KafkaController {
    private readonly logger = new Logger(KafkaController.name);

    constructor(
        private readonly kafkaService: KafkaService,
        private readonly fileService: FileService,
    ) {}

    @MessagePattern(KafkaTopics.AVAILABLE_TOPICS)
    availableKnowledge() {
        return {
            topics: [
                "єВідновлення",
                "Соціальна підтримка",
                "ВПО",
                "Субсидії",
                "Притулок",
            ]
        }
    }

    // ! ADMIN ROLE
    // перелік назв файлів
    @MessagePattern(KafkaTopics.FILE_ALL)
    fileAll(@Payload() message: IAllFilesMessage) {
        return this.fileService.getAll(message.topic);
    }

    // ! ADMIN ROLE
    @MessagePattern('file.upload')
    uploadFile(@Payload() message: IUploadFileMessage) {
        this.logger.debug('uploadFile', JSON.stringify(message));
        return this.fileService.uploadFile(
            message.topic,
            message.content,
            message.filename
        );
    }

    // ! ADMIN ROLE
    @MessagePattern(KafkaTopics.FILE_DELETE)
    deleteFile(@Payload() message: any) {
        return {
            message: message,
        }
    }

    @MessagePattern(KafkaTopics.ASK_DIALOGFLOW)
    askDialogflow(@Payload() message: IAskDialogflowMessage) {
        this.logger.debug('askDialogflow', JSON.stringify(message));

        return { 
            answer: this.kafkaService.askDialogflow(message.message)
        }
    }
}

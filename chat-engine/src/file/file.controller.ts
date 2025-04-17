import { Body, Controller, Get, Param, Post, Query } from '@nestjs/common';
import { FileService } from './file.service';
import { IUploadFileMessage } from '@app/interfaces';

@Controller('api/v1/file')
export class FileController {
    constructor(
        private readonly fileService: FileService,
    ) {}

    @Get(':fileId')
    async getFile(@Param('fileId') fileId: string) {
        return await this.fileService.getFile(fileId);
    }

    @Get()
    async getAll(@Query('topic') topic: string) {
        return await this.fileService.getAll(topic);
    }

    @Post()
    async uploadFile(@Body() body: IUploadFileMessage) {
        return await this.fileService.uploadFile(body.topic, body.content, body.filename);
    }

    @Get('topics')
    async topics() {
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
}

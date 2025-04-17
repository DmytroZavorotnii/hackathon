import { Body, Controller, Post } from '@nestjs/common';
import { DialogflowService } from './dialogflow.service';

@Controller('/api/v1/dialogflow')
export class DialogflowController {
    constructor(
        private readonly dialogflowService: DialogflowService,
    ){}

    @Post()
    async aks(@Body() body: { query: string }) {
        return {
            answer: await this.dialogflowService.ask(body.query)
        }
    }
}

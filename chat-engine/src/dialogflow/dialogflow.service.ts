import { EnvironmentEnums } from '@app/interfaces';
import dialogflow, { SessionsClient } from '@google-cloud/dialogflow';
import { google } from '@google-cloud/dialogflow/build/protos/protos';
import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { v4 as uuid } from 'uuid';

@Injectable()
export class DialogflowService {
    private readonly sessionClient: SessionsClient;
    private readonly sessionPath: string;

    constructor(
        private readonly configService: ConfigService,
    ) {
        const sessionId = uuid();

        const DIALOG_FLOW_CONFIG = configService.get(
            EnvironmentEnums.DIALOG_FLOW_CONFIG
        );
        
        this.sessionClient = new dialogflow.SessionsClient({
            credentials: DIALOG_FLOW_CONFIG,
        });
        this.sessionPath = this.sessionClient.projectAgentSessionPath(
            DIALOG_FLOW_CONFIG.project_id,
            sessionId,
        );
    }

    public async ask(message: string): Promise<string> {
        const request: google.cloud.dialogflow.v2.IDetectIntentRequest = {
            session: this.sessionPath,
            queryInput: {
                text: {
                    text: message,
                    languageCode: 'en-US',
                },
            },
        };
        const [response] = await this.sessionClient.detectIntent(request);
        const textResponse =
            response.queryResult?.fulfillmentText ||
            'Can you please ask me something else?';
        return textResponse;
    };
}

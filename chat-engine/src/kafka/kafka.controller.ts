import { Controller } from '@nestjs/common';
import { Ctx, KafkaContext, MessagePattern,  Payload } from '@nestjs/microservices';

@Controller()
export class KafkaController {
    @MessagePattern('test-topic')
    handleMessage(@Payload() message: any, @Ctx() context: KafkaContext) {
        console.log('Received message:', message);
        const originalMessage = context.getMessage();
        const partition = context.getPartition();
        const { headers, timestamp } = originalMessage;
        console.log('Headers:', headers);
        console.log('Timestamp:', timestamp);
        console.log('Partition:', partition);
        console.log('Original message:', originalMessage);
        return {
            message: 'Message received successfully',
        }
    }
}

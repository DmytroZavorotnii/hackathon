import { Global, Module } from '@nestjs/common';
import { ConfigModule as NestConfigModule } from '@nestjs/config';
import dialogFlowConf from './dialog-flow-conf';

@Global()
@Module({
    imports: [NestConfigModule.forRoot({
        isGlobal: true,
        load: [dialogFlowConf]
    })],
})
export class ConfigModule {}

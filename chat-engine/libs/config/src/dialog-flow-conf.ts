import { EnvironmentEnums } from '@app/interfaces';
import { readFileSync } from 'fs';
import { join } from 'path';

const DIALOG_FLOW_CONFIG_FILENAME = 'dialog-flow.json';

export default (): any => {
    const dialogFlow = {};
    try {
        const content = readFileSync(
            join(__dirname, '..', DIALOG_FLOW_CONFIG_FILENAME),
            'utf8'
        );

        dialogFlow[EnvironmentEnums.DIALOG_FLOW_CONFIG] = JSON.parse(content);
        dialogFlow[EnvironmentEnums.DIALOG_FLOW_ENABLED] = true;
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    } catch (error) {
        dialogFlow[EnvironmentEnums.DIALOG_FLOW_ENABLED] = false;
    } finally {
        return dialogFlow as Record<string, any>;
    }
};

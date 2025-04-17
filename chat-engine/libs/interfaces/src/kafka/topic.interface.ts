interface IAskDialogflowMessage {
    message: string;
}

interface IAllFilesMessage {
    topic: string;
}

interface IUploadFileMessage {
    topic: string;
    filename: string;
    content: string;
}

export { IAskDialogflowMessage, IAllFilesMessage, IUploadFileMessage };
import { PrismaService } from '@app/database';
import { Injectable } from '@nestjs/common';

@Injectable()
export class FileService {
  constructor(private readonly prisma: PrismaService) {}

    async getFile(id: string) {
        return this.prisma.file.findUnique(
            {
                where: {
                    id: id,
                },
            }
        )
    }

    async getAll(topic: string) {
        if (!!topic) {
            return this.prisma.file.findMany({
                where: {
                    topic: topic,
                },
            })
        } else return this.prisma.file.findMany()
    }
  
    async uploadFile(topic: string, content: string, filename: string) {
        return await this.prisma.file.create({
            data: {
                topic,
                filename: filename,
                content: content,
            },
        })
    }
}

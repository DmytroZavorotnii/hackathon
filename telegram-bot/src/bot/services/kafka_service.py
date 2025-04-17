from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
from loguru import logger
from typing import AsyncGenerator, Optional


class KafkaService:
    def __init__(
        self,
        bootstrap_servers: str,
        topic: str,
        group_id: Optional[str] = None
    ):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.group_id = group_id

        self._producer: Optional[AIOKafkaProducer] = None
        self._consumer: Optional[AIOKafkaConsumer] = None

    async def start_producer(self):
        self._producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await self._producer.start()
        logger.info("Kafka producer started")

    async def stop_producer(self):
        if self._producer:
            await self._producer.stop()
            logger.info("Kafka producer stopped")

    async def send_message(self, message: str):
        if not self._producer:
            raise RuntimeError("Producer not started")

        await self._producer.send_and_wait(self.topic, message.encode("utf-8"))
        logger.debug(f"Message sent to Kafka: {message}")

    async def start_consumer(self):
        if not self.group_id:
            raise ValueError("group_id is required to consume messages")

        self._consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )
        await self._consumer.start()
        logger.info("Kafka consumer started")

    async def stop_consumer(self):
        if self._consumer:
            await self._consumer.stop()
            logger.info("Kafka consumer stopped")

    async def consume_messages(self) -> AsyncGenerator[str, None]:
        if not self._consumer:
            raise RuntimeError("Consumer not started")

        try:
            async for msg in self._consumer:
                decoded = msg.value.decode("utf-8")
                logger.debug(f"Consumed message: {decoded}")
                yield decoded
        finally:
            await self.stop_consumer()


import asyncio
import pytest
import pytest_asyncio
from bot.services.kafka_service import KafkaService
from loguru import logger

TOPIC = "test-topic"
GROUP_ID = "test-group"
BOOTSTRAP_SERVERS = "localhost:29092"


@pytest_asyncio.fixture
async def kafka_service_producer():
    service = KafkaService(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        topic=TOPIC
    )
    await service.start_producer()
    try:
        yield service
    finally:
        await service.stop_producer()

@pytest_asyncio.fixture
async def kafka_service_consumer():
    service = KafkaService(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        topic=TOPIC,
        group_id=GROUP_ID
    )
    await service.start_consumer()
    try:
        yield service
    finally:
        await service.stop_consumer()


@pytest.mark.asyncio
async def test_kafka_producer(kafka_service_producer: KafkaService):
    await kafka_service_producer.send_message("test-message")


@pytest.mark.asyncio
async def test_kafka_consumer_reads_message(
    kafka_service_producer: KafkaService,
    kafka_service_consumer: KafkaService
):
    test_message = "hello from kafka test"

    await kafka_service_producer.send_message(test_message)

    async for message in kafka_service_consumer.consume_messages():
        if message == test_message:
            assert message == test_message
            break

import pika

from console import log_debug
from setup import setup


def callback(ch, method, properties, body):
    log_debug(f"Received: {body.decode()}")
    pass


def timepulse():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=setup.host,
            credentials=pika.PlainCredentials(
                username=setup.user, password=setup.password
            ),
        )
    )
    channel = connection.channel()
    channel.exchange_declare(setup.exchange, exchange_type="fanout")

    queue = channel.queue_declare(queue="", exclusive=True)
    queue_name = queue.method.queue

    channel.queue_bind(exchange=setup.exchange, queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

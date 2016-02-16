#-*- coding: utf-8 -*-
import pika
import settings
import sys

_connections = {}
_is_channel_initialized = False
_exchange = 'commonrail'

def get_connection():

    global _is_channel_initialized

    for mq_key, mq_data in settings.AMQP.iteritems():
        connection = _connections.get(mq_key)

        if connection and not connection.is_closed:
            continue

        _connections[mq_key] = pika.BlockingConnection(pika.ConnectionParameters(
            host=mq_data['host'],
            port=mq_data['port'],
            virtual_host=mq_data['virtual_host'],
            credentials=pika.credentials.PlainCredentials(
                mq_data['username'],
                mq_data['password'],
            ),
        ))

        _init_channel(_connections[mq_key])

    _is_channel_initialized = True

    return _connections


def _init_channel(connection):

    if _is_channel_initialized:
        return

    channel = connection.channel()
    channel.exchange_declare(exchange=_exchange, durable=True)
    channel.queue_declare(
        queue='events',
        durable=True,
        auto_delete=True,
        arguments={'x-message-ttl': 3600000},
    )

    channel.queue_bind(
        exchange=_exchange,
        queue='events',
        routing_key='event',
    )

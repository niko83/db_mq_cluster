#-*- coding: utf-8 -*-
import aioamqp
import pika
import pickle

import settings


_connections = {}
_async_connections = {}
_is_channel_initialized = False


EXCHANGE = 'commonrail'
ROUTING_KEY = 'event'


async def get_async_connections():

    if _async_connections:
        return _async_connections
    for mq_key in settings.AMQP:
        mq_data = settings.AMQP[mq_key]

        transport, protocol = await aioamqp.connect(
            host=mq_data['host'],
            login=mq_data['username'],
            password=mq_data['password'],
            virtualhost=mq_data['virtual_host'],
        )

        channel = await protocol.channel()
        _async_connections[mq_key] = (transport, protocol, channel)
    return _async_connections

async def broadcast(event_type, data):

    connections = await get_async_connections()
    for transport, protocol, channel in connections.values():
        await channel.basic_publish(
            payload=pickle.dumps(data),
            exchange_name=EXCHANGE,
            routing_key=ROUTING_KEY
        )

def get_connection():

    global _is_channel_initialized

    for mq_key, mq_data in settings.AMQP.items():
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
        _connections[mq_key].close()

    _is_channel_initialized = True

    return _connections


def _init_channel(connection):

    if _is_channel_initialized:
        return

    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, durable=False)

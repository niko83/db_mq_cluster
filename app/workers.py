import pickle

import aioamqp

import settings
from amqp import ROUTING_KEY, EXCHANGE
from utils import bloom


QUEUE = 'events_receiver_%s' % settings.HOSTNAME


async def callback(channel, body, envelope, properties):
    bloom.add_uuid_to_db(*pickle.loads(body))


async def receive(loop):

    mq_data = settings.AMQP[1]
    transport, protocol = await aioamqp.connect(
        host=mq_data['host'],
        login=mq_data['username'],
        password=mq_data['password'],
        virtualhost=mq_data['virtual_host'],
        loop=loop,
    )
    channel = await protocol.channel()

    await channel.queue_declare(
        queue_name=QUEUE,
        durable=True,
        exclusive=True,
    )
    await channel.queue_bind(
        exchange_name=EXCHANGE,
        queue_name=QUEUE,
        routing_key=ROUTING_KEY
    )

    await channel.basic_consume(callback, queue_name=QUEUE)

import amqp
import db
from uuid import uuid4
import random
import events
from utils.bloom import add_uuid_to_db


async def run(data):
    uuid = str(uuid4())

    pools = await db.get_async_connections()

    shard_key = random.choice(list(pools.keys()))
    email = data.get('email', [''])[-1]

    result = await db.async_execute(
        shard_key,
        "INSERT INTO users (uuid, email) VALUES (%s, %s)",
        (uuid, uuid+email)  #@FIXME remove email unique hardcode
    )

    add_uuid_to_db(uuid, shard_key)

    await amqp.broadcast (
        events.EVENTS_TYPE.ADD_USER,
        data=(uuid, shard_key)
    )
    return result

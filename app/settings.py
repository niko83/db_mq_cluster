
BLOOM_ERROR_RATE = 0.001
SHARD_CAPACITY = 1000000

DB = {}
for shard_number in range(1, 3):
    DB[shard_number] = {
        'database': 'docker',
        'password': 'docker',
        'username': 'docker',
        'host': 'db%s.containers.example.com' % shard_number,
        'port': 5432,
    }

AMQP = {}
for shard_number in range(1, 2):
    AMQP[shard_number] = {
        'virtual_host': '/docker',
        'password': 'docker',
        'username': 'docker',
        'host': 'mq%s.containers.example.com' % shard_number,
        'port': 5672,
    }

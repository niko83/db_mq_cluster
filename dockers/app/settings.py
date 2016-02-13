

DB = {}
for shard_number in xrange(1, 5):
    DB[shard_number] = {
        'name': 'docker_db',
        'password': 'docker',
        'username': 'docker',
        'host': 'db%s.containers.example.com' % shard_number,
    }

AMQP = {}
for shard_number in xrange(1, 4):
    AMQP[shard_number] = {
        'virtual_host': '/docker',
        'password': 'docker',
        'username': 'docker',
        'host': 'mq%s.containers.example.com' % shard_number,
        'port': 5672,
    }

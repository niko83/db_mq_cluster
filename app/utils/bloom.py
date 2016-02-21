from pybloom import BloomFilter
import settings
import db
import sys
import os

_filters = {
    'uuid_in_db': {}
}


for db_key in settings.DB:
    _filters['uuid_in_db'][db_key] = BloomFilter(
        capacity=settings.SHARD_CAPACITY,
        error_rate=settings.BLOOM_ERROR_RATE,
    )

def has_db_uuid(db_key, uuid):
    pass


def add_uuid_to_db(uuid, db_key):
    _filters['uuid_in_db'][db_key].add(uuid)


def restore_bloom_keys():
    sql = "SELECT uuid, id from users WHERE id > %s order by id ASC LIMIT 1000"
    sys.stdout.write('start restore bloom filter' + os.linesep)
    for db_key in settings.DB:
        max_row_id = 0
        while True:
            all_rows_processed = True
            for uuid, row_id in db.execute(db_key, sql, (max_row_id, ), fetch=True):
                all_rows_processed = False
                max_row_id = row_id
                add_uuid_to_db(uuid, db_key)
            if all_rows_processed:
                break

    sys.stdout.write(('finish restore bloom filter: max row_id = %s' + os.linesep) % max_row_id)

restore_bloom_keys()




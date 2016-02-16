import psycopg2
import psycopg2.extras
import settings

_connections = {}


def get_connections():

    for db_key, db_data in settings.DB.iteritems():
        connection = _connections.get(db_key)
        if connection and not connection.closed:
            continue

        _connections[db_key] = psycopg2.connect(
            database=db_data['database'],
            user=db_data['username'],
            password=db_data['password'],
            host=db_data['host'],
            port=db_data['port'],
        )
        _connections[db_key].set_session(autocommit=True)
        _init_db(_connections[db_key])

    return _connections


def _init_db(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            uuid uuid,
            email text UNIQUE,
            score bigint default 0,
            created_at timestamp default NOW(),
            PRIMARY KEY (uuid)
        );
        """
    )
    cursor.close()

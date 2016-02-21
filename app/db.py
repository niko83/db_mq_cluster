import psycopg2
import psycopg2.extras
import settings
import aiopg

_connections = {}
_async_connections = {}




async def get_async_connections():
    if _async_connections:
        return _async_connections

    for db_key, db_data in settings.DB.items():
        _async_connections[db_key] = await aiopg.create_pool(
            dsn='dbname={database} user={username} password={password} host={host}'.format(**db_data)
        )

    return _async_connections

def get_connections():

    for db_key, db_data in settings.DB.items():
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


def execute(conn_key, sql, params, fetch=False):
    conn = get_connections()[conn_key]
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(sql, params)
    if fetch:
        data = cursor.fetchall()
    cursor.close()
    return data if fetch else None


async def async_execute(conn_key, sql, params, fetch=False):
    pools = await get_async_connections()
    pool = pools[conn_key]

    async with pool.acquire() as conn:
        async with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            await cur.execute(sql, params)
            if fetch:
                data = await cursor.fetchall()
                return data


def _init_db(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            uuid uuid,
            id serial UNIQUE,
            email text UNIQUE,
            score bigint default 0,
            created_at timestamp default NOW(),
            PRIMARY KEY (uuid)
        );
        """
    )
    cursor.close()

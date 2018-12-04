import redis
from redis import Redis


class RedisHandler:

    def __init__(self, host="localhost", port=6379, db=0):
        self.conn: Redis = redis.Redis(host, port, db)

    def __repr__(self):
        return self.conn.__repr__()


from aioredis import Redis, from_url


class RedisCache:

    def __init__(self):
        self.redis = from_url("redis://127.0.0.0:6379/0")

    async def set(self, key, value):
        return await self.redis.set(key, value)

    async def get(self, key):
        return await self.redis.get(key)

from app.classes.redis_class import Redis


def main():
    redis_cache = RedisCache()
    redis_cache.set("Name", "Lasha")
    redis_cache.get("Name")


if __name__ == "__main__":
    main()

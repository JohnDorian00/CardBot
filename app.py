from redis import Redis

redis = Redis(host='redis', port=6379)


def test():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This webpage has been viewed " + counter + " time(s)"


if __name__ == "__main__":
    print('Hello from bot ', test())

import os
from redis import StrictRedis

redis_pass = os.environ['REDIS_PASSWORD']
token = os.environ['TOKEN']


redis = StrictRedis(host='redis', port=6379, password='test2')


def test():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This webpage has been viewed " + counter + " time(s)"


if __name__ == "__main__":
    print('pass is ', redis_pass)
    print('token is ', token)
    print('Hello from bot ', test())

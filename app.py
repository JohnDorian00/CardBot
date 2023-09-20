import sys
from redis import StrictRedis

redis = StrictRedis(host='redis', port=6379, password='test2')


def test():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This webpage has been viewed " + counter + " time(s)"


if __name__ == "__main__":
    print('pass is ', sys.argv[1])
    print('Hello from bot ', test())

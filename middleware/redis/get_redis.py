import redis

r = redis.Redis(host='localhost', port=6379, db=0)

output = r.hgetall('2')
print(output['ct'.encode('utf-8')])

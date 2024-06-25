import redis
import time
start_time = time.time()
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
for i in range(10000):
    r.set('foo'+str(i), 'bar'+str(time.time()))
    r.get('foo'+str(i))
print("--- %s seconds ---" % (time.time() - start_time))

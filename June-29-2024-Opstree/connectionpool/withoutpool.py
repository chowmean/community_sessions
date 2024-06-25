import redis
import time
start_time = time.time()
r = redis.Redis(host='localhost', port=6379, db=0, max_connections=0)
for i in range(10000):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo'+str(i), 'bar'+str(time.time()))
    r.get('foo'+str(i))
    r.close()
print("--- %s seconds ---" % (time.time() - start_time))

import requests
import time
start_time = time.time()


for i in range(10):
    r = requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    print(r.text)
print("--- %s seconds ---" % (time.time() - start_time))
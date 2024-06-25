import logging
import requests
import time
start_time = time.time()

# Calling psutil.cpu_precent() for 4 seconds



logging.basicConfig(level=logging.DEBUG)
s=requests.session()
for i in range(10):
    r = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    print(r.text)
print("--- %s seconds ---" % (time.time() - start_time))
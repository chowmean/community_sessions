from dataclasses import replace
from xml import dom
import requests
import time
start_time = time.time()
from urllib.parse import urlparse

import socket
import pydig

# Basic query
def resolve(name):
    return pydig.query(name, 'A')

dns_cache ={}

def myreq(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    print(domain)
    if domain in dns_cache:
        print('got dns')
        url = dns_cache[domain]
        replaced = parsed._replace(netloc=url)
        url = replaced.__str__()
        url =replaced.geturl()
        r = requests.get(url)
        print(r.text)
        
    else:
        print('resolving dns')
        data = resolve(domain)
        dns_cache[domain] = data[0]
        print(dns_cache)

for i in range(10):
    myreq('http://httpbin.org/cookies/set/sessioncookie/123456789')
print("--- %s seconds ---" % (time.time() - start_time))


#sudo tcpdump -i any port 53  -v
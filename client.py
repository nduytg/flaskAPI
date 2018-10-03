import requests
from hashlib import md5
import time
import pprint

SecretKey = 'Qi3mnN9b3UougbpqFvsGruSir0tKPlhc'
domain = 'http:/localhost:80/api/tasks'

user = 'nduytg'
time = str(int(time.time()))
sign = md5((time + user + SecretKey).encode('utf-8')).hexdigest()

print(time)
print(sign)

r = requests.post(domain, data={'user': user, 'taskID': taskID, 'time': time, 'sign': sign})
print(r.status_code, r.reason)
print(r.content)

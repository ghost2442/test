import requests
import time
while(True):
  s = 'https://frantic-architect.firebaseio.com/railway.json'
  r = requests.patch(s,json={'s',int(time.time())})
  print(r)
  time.sleep(3)
  

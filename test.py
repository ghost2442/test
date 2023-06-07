from telethon.sync import TelegramClient
from flask import Flask
#import logging
#logging.basicConfig(level=logging.DEBUG)
app=Flask(__name__)
@app.route('/')
def man():
  print('lets go')
  result='none'
  try:
    c=TelegramClient('73',73636,'7373737737338')
    c.connect()
    result='connected'
  except Exception as e:
    result=str(e)
  return result


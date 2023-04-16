from telethon.sync import TelegramClient
#import logging
#logging.basicConfig(level=logging.DEBUG)


client = TelegramClient('19', 12899094, '335e73259ab7fe48c3d12e4139f6dfa0')

client.connect()
print('connected')
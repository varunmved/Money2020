import requests
import json
import calendar
import time
import random 
from firebase import firebase


firebase = firebase.FirebaseApplication('https://baemoney2020.firebaseio.com', None)

def putAppleWatch(firebase):
    a = calendar.timegm(time.gmtime())
    b = random.randint(80,100)
    data = {str(a):str(b)}
    data2 = {'a':'b'}
    print(data)
    print(data2)
    #result = firebase.post('/watch',a,{'print':'pretty'},{'X_FANCY_HEADER': 'VERY FANCY'})
    result = firebase.post('/watch',data)
    #result = firebase.post('/watch',a)
    

def getFromAppleWatch(firebase):
    result = firebase.get('/watch',None)
    a=(json.dumps(result))
    print(a)
    

def processAppleWatch():
    print('ayy')

def putToFirebase():
    print('lmao')

for i in range (0,60):
    time.sleep(1)
    putAppleWatch(firebase)
#getFromAppleWatch(firebase)

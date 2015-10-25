import requests
import json
import calendar
import time
import random 
import numpy
from firebase import firebase


firebase = firebase.FirebaseApplication('https://baemoney2020.firebaseio.com', None)

def putAppleWatch(firebase):
    a = calendar.timegm(time.gmtime())
    b = random.randint(80,100)
    data = {str(a):str(b)}
    #result = firebase.post('/watch',a,{'print':'pretty'},{'X_FANCY_HEADER': 'VERY FANCY'})
    result = firebase.post('/watch',data)
    #result = firebase.post('/watch',a)
    

def getFromAppleWatch(firebase):
    result = firebase.get('/watch',None)
    #a=(json.dump(result))
    a = result
    print(a)
    timeList = []
    hrList = []
    #print(a.itervalues().next())
    for value in a.iteritems():
        second=(value[1])
        time = str(second.keys())
        lenTime = len(time)
        time = time[3:lenTime-2]
        time = int(time)
        timeList.append(time)
        hr = str(second.values())
        hrLen  = len(hr)
        hr = hr[3:hrLen-2]
        hr = int(hr)
        hrList.append(hr)
    
    elapsedTime = max(timeList) - min(timeList)
    avghr = numpy.average(hrList)
    maxhr = max(hrList)
    print(elapsedTime)
    print(maxhr)



def processAppleWatch():
    print('ayy')

def putToFirebase():
    print('lmao')

def startHeartRateGen():
    for i in range (0,5):
        time.sleep(1)
        putAppleWatch(firebase)

startHeartRateGen()
getFromAppleWatch(firebase)

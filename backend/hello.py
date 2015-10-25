import string
import requests
import json
import calendar
import time
import random 
import numpy
import fitbit
import names
from firebase import firebase


firebase = firebase.FirebaseApplication('https://baemoney2020.firebaseio.com', None)
def createBeacon():
    beaconStr = 'beacon' + str(random.randint(0,10))
    return beaconStr

def createName():
    user = str(names.get_full_name())
    user.replace(" ", "_")
    return user

def putAppleWatch(beacon,user):
    userPostStr = '/'+ beacon + '/' + user
    a = calendar.timegm(time.gmtime())
    b = random.randint(80,100)
    data = {str(a):str(b)}
    result = firebase.post(userPostStr,data)
    

def getFromAppleWatch(beacon,user):
    userPostStr = '/' + beacon + '/' + user
    result = firebase.get(userPostStr,None)
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
    print(avghr)

def putBeacon():
    N = 10
    #beaconId = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    #result = firebase.post('/beacon',beaconId)
    

def startHeartRateGen():
    for i in range (0,25):
        beacon = createBeacon()
        for k in range (0,25):
            name = createName()
            for j in range (0,25):
                putAppleWatch(beacon,name)
            getFromAppleWatch(beacon,name)
startHeartRateGen()
#getFromAppleWatch()
putBeacon()

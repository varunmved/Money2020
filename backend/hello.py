import string
import requests
import json
import calendar
import time
import random 
import numpy as np
import fitbit
import names
from firebase import firebase
requests.packages.urllib3.disable_warnings()

beaconList = []
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
    avghr = np.average(hrList)
    maxhr = max(hrList)
    print(elapsedTime)
    print(maxhr)
    print(avghr)

def putBeacon():
    N = 10
    #beaconId = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    #result = firebase.post('/beacon',beaconId)
    

def startHeartRateGen():
    for i in range (0,10):
        beacon = createBeacon()
        beaconList.append(beacon)
        for k in range (0,5):
            name = createName()
            for j in range (0,5):
                putAppleWatch(beacon,name)
            getFromAppleWatch(beacon,name)

def analyzeBeacons(): 
    for i in range(0,10):
        beaconStr = '/beacon' +str(i) 
        result = firebase.get(beaconStr,None)
        print(result.keys())
        print(result.values())
        print(i)
        #keys = np.fromiter(iter(result.keys()), dtype=float)
        #vals = np.fromiter(iter(result.values()), dtype=float)
        
    #print(len(l)) 
    #for j in (0,len(l)):
    #(l[0])
#startHeartRateGen()

analyzeBeacons()

putBeacon()

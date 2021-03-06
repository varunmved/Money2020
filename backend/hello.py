import string
import requests
import json
import calendar
import time
import random 
import numpy as np
import fitbit
import names
import base64
import plotly.plotly as py
import plotly.graph_objs as go
import securenet as securenet
from firebase import firebase
requests.packages.urllib3.disable_warnings()

beaconList = []

firebase = firebase.FirebaseApplication('https://baemoney2020.firebaseio.com', None)

def encodesSecurenet(securenetID,securenetPass):
    a = base64.encodestring(securenetID + ':' + securenetPass)
    out = 'Basic ' + a 
    url = 'https://gwapi.demo.securenet.com/api/Payments/Charge'
    r = requests.get(url,headers=out)

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
    x = []
    y = []
    trace = go.Scatter(x.append(int(a)), y.append(b), mode = 'lines+markers')      

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
    for i in range(0,11):
        beaconStr = '/beacon' +str(i) 
        result = firebase.get(beaconStr,None)
        #print(result.keys())
        print(str(result.values()))
        #print(i)
        #keys = np.fromiter(iter(result.keys()), dtype=float)
        #vals = np.fromiter(iter(result.values()), dtype=float)
    #print(len(l)) 
    #for j in (0,len(l)):
    #(l[0])

def securenetProcess():
    securenet.authorize({
    "amount": 11.00,
    "card": {
    "number": "4444 3333 2222 1111",
    "cvv": "999",
    "expiration_date": "04/2016",
    "address": {
    "line1": "123 Main St.",
    "city": "Austin",
    "state": "TX",
    "zip": "78759"
    },
    "first_name": "Jack",
    "last_name": "Test"
    },
    "extended_information": {
    "type_of_goods": "PHYSICAL"
    } , 
    "developerApplication": {
        "developerId": 12345678,
        "version": "1.2"
      }
    })

#startHeartRateGen()
#analyzeBeacons()
#putBeacon()
#securenetProcess()
securenetID = '8005236'
securenetPass = 'Yn4ma5uS7nww'
#encodesSecurenet(securenetID,securenetPass)
securenetProcess()
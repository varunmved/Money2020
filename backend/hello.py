import requests
import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://baemoney2020.firebaseio.com', None)


def getFromAppleWatch(firebase):
    result = firebase.get('/users',None)
    a= json.dumps(result)
    print(a[0])

def processAppleWatch():
    print('ayy')

def putToFirebase():
    print('lmao')


getFromAppleWatch(firebase)

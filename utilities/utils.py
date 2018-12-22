import pyotp
import base64
import uuid
from random import randint
from datetime import datetime, timedelta

totp = pyotp.TOTP('base32secret3232')

def getOTP():
    return totp.now()

def isEmpty(value):
    return len(str(value).strip())==0

def isValidMDN(value):
    return (len(value)==10)

def getEncodedValue(value):
    return base64.b64encode(bytes(value, 'utf-8'))

def getDecodedValue(value):
    return base64.b64decode(bytes(value, 'utf-8'))

def getRandomId():
    return uuid.uuid1().hex

def generateUniqueId():
    n = 12
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def dateSerializer(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    
def getFormattedKey(key):
        splittedList = key.split(sep="_")
        i = 1
        while i < len(splittedList):
            splittedList[i] = splittedList[i][0].upper()+splittedList[i][1:]
            i += 1
        return (''.join(splittedList))
    
def getServerDateTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getNextStartDateTime(startDate):
    return (datetime.strptime(startDate,"%Y-%m-%d %H:%M:%S") + timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")


    
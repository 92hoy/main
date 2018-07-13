#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist

from backend.models import CmsManager

# license check
import sys
import base64
import subprocess
import hashlib
from Crypto.Cipher import AES
from datetime import datetime

class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

def getUUID():
    result = subprocess.check_output ("blkid /dev/sda1" , shell=True)
    result = str(result)
    uuid_idx = result.find('UUID')
    result = result[uuid_idx:]
    uuid_idx = result.find('"')
    result = result[uuid_idx+1:]
    result = result[:36]
    uuid = result
    return uuid

def getHostname():
    hostname = subprocess.check_output ("hostname" , shell=True)
    hostname = str(hostname)
    hostname = hostname[hostname.find("'")+1:]
    hostname = hostname[:hostname.find("'")-2]
    return hostname

def getSystemTime():
    system_time = subprocess.check_output ("date +'%Y-%m-%d'" , shell=True)
    system_time = str(system_time)
    system_time = system_time[system_time.find("'")+1:]
    system_time = system_time[:system_time.find("'")-2]
    origin_time = system_time
    return origin_time

def createRawData(uuid, hostname):
    rawData = (uuid + "h4ppyy" + hostname).encode('utf-8')
    return rawData

def createEncData(rawData):
    encData = hashlib.sha224(rawData).hexdigest()
    return encData

def convertTime(t):
    system_time = t.split('-')
    year = int(system_time[0])
    mon = int(system_time[1])
    day = int(system_time[2])
    today = datetime(year, mon, day)
    return today

def checkLicense(license):
    uuid = getUUID()
    hostname = getHostname()
    system_time = getSystemTime()
    rawData = createRawData(uuid, hostname)
    encData = createEncData(rawData)

    key = '12345678901234567890123456789012'
    cipher = AESCipher(key)
    decrypted = cipher.decrypt(license)
    decrypted = decrypted.split('h4ppyy')
    check_data = decrypted[0]
    check_time = decrypted[1]

    system_time = convertTime(system_time)
    check_time = convertTime(check_time)

    if system_time > check_time:
        print("finish")
        return "finish"
    else:
        if check_data == encData:
            print("success")
            return "success"
        else:
            print("error")
            return "error"

def login(request):

    if request.is_ajax():

        inputId = request.POST.get('inputId')
        inputPw = request.POST.get('inputPw')
        license = settings.LICENSE
        licenseStatus = checkLicense(license)
        print(licenseStatus)

        if inputId =='' and inputPw == '' :
            return JsonResponse({'result':'error0'})

        print("----------------------> s")
        print("inputId = ", inputId)
        print("inputPw = ", inputPw)
        print("----------------------> e")

        try:
            userObject = CmsManager.objects.get(user_id=inputId)
            if userObject.user_pwd == inputPw:
                request.session['user_id'] = userObject.user_id
                request.session['user_name'] = userObject.user_name
                request.session['language'] = userObject.language
                request.session['user_role'] = userObject.user_role
                request.session[translation.LANGUAGE_SESSION_KEY] = userObject.language
                translation.activate(userObject.language)

                return JsonResponse({'result':'success'})
            else:
                return JsonResponse({'result':'error2'})
        except ObjectDoesNotExist:
            return JsonResponse({'result':'error1'})

    context = {}

    return render(request, 'login/login.html', context)

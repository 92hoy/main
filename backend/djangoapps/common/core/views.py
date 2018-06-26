#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.conf import settings

#UTIL
import json
import requests
import xmltodict

#from backend.djangoapps.common.core.views import coreJson
def coreJson():
    f = open(settings.CORE_APIJSON_PATH, 'r')
    rawData = f.read()
    print(rawData)
    f.close()
    jsonData = json.loads(rawData)
    print("------------------------------------------> API")
    print(jsonData['api']['ipAddress'])
    print(jsonData['api']['port'])
    print(jsonData['api']['useHttps'])
    print(jsonData['api']['userName'])
    print(jsonData['api']['password'])
    print(jsonData['api']['ipAddress1'])
    print(jsonData['api']['port1'])
    print(jsonData['api']['useHttps1'])
    print(jsonData['api']['ldapAddress'])
    print(jsonData['api']['ldapPort'])
    print(jsonData['api']['domainName'])
    print("------------------------------------------> account")
    print(jsonData['account']['defaultTimeZone'])
    print(jsonData['account']['cmsAdminUrl'])
    print(jsonData['account']['jitter'])
    print(jsonData['account']['packetLoss'])
    print(jsonData['account']['userName'])
    print(jsonData['account']['password'])
    print(jsonData['account']['uiTemplate'])
    print(jsonData['account']['cisocoSparkId'])
    print(jsonData['account']['cloudWebExSiteName'])
    print(jsonData['account']['cloudWebExId'])
    print(jsonData['account']['cloudWebExPwd'])
    print("------------------------------------------> callcommand")
    print(jsonData['callcommand']['txVideoMute'])
    print(jsonData['callcommand']['rxVideoMute'])
    print(jsonData['callcommand']['txAudioMute'])
    print(jsonData['callcommand']['rxAudioMute'])
    print(jsonData['callcommand']['presentationContributionAllowed'])
    print(jsonData['callcommand']['presentationViewingAllowed'])
    print(jsonData['callcommand']['videoMode'])

    return jsonData

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

#from backend.djangoapps.common.api.views import api_command
@csrf_exempt
def ccChange(request):

    mode = request.POST.get('mode') # txVideoMute
    flag = request.POST.get('flag') # on

    print("mode = ", mode)
    print("flag = ", flag)

    f = open(settings.CORE_APIJSON_PATH, 'r')
    rawData = f.read()
    f.close()
    jsonData = json.loads(rawData)

    print(jsonData)

    if mode == 'txVideoMute':
        if flag == 'on':
            jsonData['callcommand']['txVideoMute'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['txVideoMute'] = 'false'
    elif mode == 'videoMode':
        if flag == 'on':
            jsonData['callcommand']['videoMode'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['videoMode'] = 'false'
    elif mode == 'txAudioMute':
        if flag == 'on':
            jsonData['callcommand']['txAudioMute'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['txAudioMute'] = 'false'
    elif mode == 'rxAudioMute':
        if flag == 'on':
            jsonData['callcommand']['rxAudioMute'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['rxAudioMute'] = 'false'
    elif mode == 'presentationContributionAllowed':
        if flag == 'on':
            jsonData['callcommand']['presentationContributionAllowed'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['presentationContributionAllowed'] = 'false'
    elif mode == 'presentationViewingAllowed':
        if flag == 'on':
            jsonData['callcommand']['presentationViewingAllowed'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['presentationViewingAllowed'] = 'false'
    elif mode == 'rxVideoMute':
        if flag == 'on':
            jsonData['callcommand']['rxVideoMute'] = 'true'
        elif flag == 'off':
            jsonData['callcommand']['rxVideoMute'] = 'false'

    print(jsonData)
    rawData = json.dumps(jsonData)

    f = open(settings.CORE_APIJSON_PATH, 'w')
    f.write(rawData)
    f.close()

    return JsonResponse({'return':'success'})

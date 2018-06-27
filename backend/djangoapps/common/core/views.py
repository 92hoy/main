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

@csrf_exempt
def envChange(request):

    api_server = request.POST.get('api_server')
    api_port = request.POST.get('api_port')
    use_https = request.POST.get('use_https')
    api_username = request.POST.get('api_username')
    api_password = request.POST.get('api_password')
    api_server_callbridge = request.POST.get('api_server_callbridge')
    api_port_callbridge = request.POST.get('api_port_callbridge')
    use_https_callbridge = request.POST.get('use_https_callbridge')
    time_zone = request.POST.get('time_zone')
    cisco_cms_url = request.POST.get('cisco_cms_url')
    jitter = request.POST.get('jitter')
    packetloss = request.POST.get('packetloss')
    spark_id = request.POST.get('spark_id')
    web_sitename = request.POST.get('web_sitename')
    web_id = request.POST.get('web_id')
    web_password = request.POST.get('web_password')
    ui_template = request.POST.get('ui_template')

    print("api_server = ", api_server)
    print("api_port = ", api_port)
    print("use_https = ", use_https)
    print("api_username = ", api_username)
    print("api_password = ", api_password)
    print("api_server_callbridge = ", api_server_callbridge)
    print("api_port_callbridge = ", api_port_callbridge)
    print("use_https_callbridge = ", use_https_callbridge)

    print("time_zone = ", time_zone)
    print("cisco_cms_url = ", cisco_cms_url)
    print("jitter = ", jitter)
    print("packetloss = ", packetloss)
    print("spark_id = ", spark_id)
    print("web_sitename = ", web_sitename)
    print("web_id = ", web_id)
    print("web_password = ", web_password)
    print("ui_template = ", ui_template)

    f = open(settings.CORE_APIJSON_PATH, 'r')
    rawData = f.read()
    f.close()
    jsonData = json.loads(rawData)

    jsonData['api']['ipAddress'] = api_server
    jsonData['api']['port'] = api_port
    jsonData['api']['useHttps'] = use_https
    jsonData['api']['userName'] = api_username
    jsonData['api']['password'] = api_password
    jsonData['api']['ipAddress1'] = api_server_callbridge
    jsonData['api']['port1'] = api_port_callbridge
    jsonData['api']['useHttps1'] = use_https_callbridge
    #jsonData['api']['ldapAddress'] =
    #jsonData['api']['ldapPort'] =
    #jsonData['api']['domainName'] =
    jsonData['account']['defaultTimeZone'] = time_zone
    jsonData['account']['cmsAdminUrl'] = cisco_cms_url
    jsonData['account']['jitter'] = jitter
    jsonData['account']['packetLoss'] = packetloss
    #jsonData['account']['userName'] =
    #jsonData['account']['password'] =
    jsonData['account']['uiTemplate'] = ui_template
    jsonData['account']['cisocoSparkId'] = spark_id
    jsonData['account']['cloudWebExSiteName'] = web_sitename
    jsonData['account']['cloudWebExId'] = web_id
    jsonData['account']['cloudWebExPwd'] = web_password

    rawData = json.dumps(jsonData)

    f = open(settings.CORE_APIJSON_PATH, 'w')
    f.write(rawData)
    f.close()

    return JsonResponse({'return':'success'})

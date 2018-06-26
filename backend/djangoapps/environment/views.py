#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

from backend.djangoapps.common.core.views import coreJson

# 호출 상태
def environment(request):

    jsonData = coreJson()
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

    context = {}
    context['api_ipAddress'] = jsonData['api']['ipAddress']
    context['api_port'] = jsonData['api']['port']
    context['api_useHttps'] = jsonData['api']['useHttps']
    context['api_userName'] = jsonData['api']['userName']
    context['api_password'] = jsonData['api']['password']
    context['api_ipAddress1'] = jsonData['api']['ipAddress1']
    context['api_port1'] = jsonData['api']['port1']
    context['api_useHttps1'] = jsonData['api']['useHttps1']

    context['account_defaultTimeZone'] = jsonData['account']['defaultTimeZone']
    context['account_cmsAdminUrl'] = jsonData['account']['cmsAdminUrl']
    context['account_jitter'] = jsonData['account']['jitter']
    context['account_packetLoss'] = jsonData['account']['packetLoss']
    context['account_userName'] = jsonData['account']['userName']
    context['account_password'] = jsonData['account']['password']
    context['account_uiTemplate'] = jsonData['account']['uiTemplate']
    context['account_cisocoSparkId'] = jsonData['account']['cisocoSparkId']
    context['account_cloudWebExSiteName'] = jsonData['account']['cloudWebExSiteName']
    context['account_cloudWebExId'] = jsonData['account']['cloudWebExId']
    context['account_cloudWebExPwd'] = jsonData['account']['cloudWebExPwd']

    return render(request, 'environment/environment.html', context)

# 호출 상태
def license(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'environment/license.html', context)

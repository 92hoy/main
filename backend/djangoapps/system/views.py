#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

from backend.djangoapps.common.core.views import coreJson

# 호출 상태
def cdr(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/cdr.html', context)

# 네트워크 상태
def ldap(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/ldap.html', context)

# 시스템 상태
def account(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/account.html', context)

# 시스템 상태
def endPoint(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/endPoint.html', context)

# 시스템 상태
def endPointGroup(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/endPointGroup.html', context)

# 시스템 상태
def acanoClient(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/acanoClient.html', context)

# 시스템 상태
def logoManagement(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/logoManagement.html', context)

# 시스템 상태
def commandManagement(request):

    jsonData = coreJson()
    print(jsonData['callcommand']['txVideoMute'])
    print(jsonData['callcommand']['rxVideoMute'])
    print(jsonData['callcommand']['txAudioMute'])
    print(jsonData['callcommand']['rxAudioMute'])
    print(jsonData['callcommand']['presentationContributionAllowed'])
    print(jsonData['callcommand']['presentationViewingAllowed'])
    print(jsonData['callcommand']['videoMode'])

    context = {}
    context['cc_txVideoMute'] = jsonData['callcommand']['txVideoMute']
    context['cc_rxVideoMute'] = jsonData['callcommand']['rxVideoMute']
    context['cc_txAudioMute'] = jsonData['callcommand']['txAudioMute']
    context['cc_rxAudioMute'] = jsonData['callcommand']['rxAudioMute']
    context['cc_presentationContributionAllowed'] = jsonData['callcommand']['presentationContributionAllowed']
    context['cc_presentationViewingAllowed'] = jsonData['callcommand']['presentationViewingAllowed']
    context['cc_videoMode'] = jsonData['callcommand']['videoMode']

    return render(request, 'system/commandManagement.html', context)

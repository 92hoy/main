#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

# 호출 상태
def callStatus(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'monitoring/callStatus.html', context)

# 네트워크 상태
def networkStatus(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'monitoring/networkStatus.html', context)

# 시스템 상태
def systemStatus(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'monitoring/systemStatus.html', context)

#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

# 호출 상태
def liveVod(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'streamService/liveVod.html', context)

# 호출 상태
def trafficStatistics(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'streamService/trafficStatistics.html', context)

# 호출 상태
def conversionStatistics(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'streamService/conversionStatistics.html', context)

# 호출 상태
def serverMonitoring(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'streamService/serverMonitoring.html', context)

# 호출 상태
def recording(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'streamService/recording.html', context)
